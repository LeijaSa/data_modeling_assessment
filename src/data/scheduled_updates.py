import psycopg2
from config import config
import json

# Scheduled ETL Process: A batch summary update process runs daily/ weekly?/ monthly?. 
# This process reads the new sales data from FactSales since the last update and updates each customers summary data


def db_update_customer_purchase_summary():
    read_sales_command = """
        SELECT fs.customer_id, SUM(fs.net_sales_amount) AS total_purchases, EXTRACT(YEAR FROM dt.date) AS year
        FROM FactSales fs
        JOIN DimDateTable dt ON fs.sale_date_id = dt.id
        WHERE dt.date >= CURRENT_DATE - INTERVAL '7 days'  -- Or your desired interval
        GROUP BY fs.customer_id, EXTRACT(YEAR FROM dt.date);
    """

    update_summary_command = """
        INSERT INTO DimCustomerYearlySummary (customer_id, total_purchases, year)
        VALUES (%s, %s, %s)
        ON CONFLICT (customer_id, year) DO UPDATE
        SET total_purchases = DimCustomerYearlySummary.total_purchases + EXCLUDED.total_purchases;
    """

    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                cur.execute(read_sales_command)
                sales_data = cur.fetchall()

                for row in sales_data:
                    customer_id, total_purchases, year = row
                    cur.execute(update_summary_command, (customer_id, total_purchases, year))

                conn.commit()
                result = {"success": "Customer yearly summaries updated successfully"}
                return json.dumps(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


# Scheduled ETL Process: A batch program level update process runs yearly. 
# This process reads the summaries of customers (previous year) and updates each customers program level if required

def db_update_customer_loyalty_levels():
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                # Update previous rows and insert new levels in a single transaction
                cur.execute(
                    """
                    WITH YearlySummary AS (
                    SELECT customer_id, total_purchases
                    FROM DimCustomerYearlySummary
                    WHERE year = EXTRACT(YEAR FROM CURRENT_DATE)
                ), NewLoyalty AS ( -- Calculate new loyalty levels
                    SELECT
                        ys.customer_id,
                        CASE
                            WHEN ys.total_purchases >= 1000 THEN 'Gold'
                            WHEN ys.total_purchases >= 500 THEN 'Silver'
                            ELSE 'Bronze'
                        END AS new_loyalty_level
                    FROM YearlySummary ys
                ), UpdatedLoyalty AS (
                    UPDATE DimLoyaltyLevelHistory dlh
                    SET end_date = CURRENT_DATE, is_active = FALSE
                    FROM NewLoyalty nl  -- Join with NewLoyalty to compare levels
                    WHERE dlh.end_date IS NULL  -- Only update currently active rows
                    AND dlh.customer_id = nl.customer_id
                    AND dlh.loyalty_program_level != nl.new_loyalty_level -- Only update if the level changes
                    RETURNING dlh.customer_id  -- No need to return the level
                )
                INSERT INTO DimLoyaltyLevelHistory (customer_id, loyalty_program_level, start_date, end_date, is_active)
                SELECT
                    nl.customer_id,
                    nl.new_loyalty_level,
                    CURRENT_DATE,
                    NULL,
                    TRUE
                FROM NewLoyalty nl
                WHERE NOT EXISTS (
                    SELECT 1
                    FROM DimLoyaltyLevelHistory dlh  -- Check against existing active levels
                    WHERE dlh.customer_id = nl.customer_id
                    AND dlh.loyalty_program_level = nl.new_loyalty_level
                    AND dlh.end_date IS NULL
                );
                    """
                )
                conn.commit()
                return json.dumps({"success": "Customer loyalty levels updated successfully"})
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        return json.dumps({"error": str(error)})
    

if __name__ == '__main__':
    print(db_update_customer_purchase_summary())
    print(db_update_customer_loyalty_levels())

  