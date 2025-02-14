from datetime import date, timedelta
import psycopg2
from config import config
import json
from datetime import date

# Function to insert a date into the DimDateTable
def db_insert_dim_date(date_value: date, weekday: str, year: int, quarter: int, month: int):
    command = (
        """
        INSERT INTO DimDateTable (date, weekday, year, quarter, month) 
        VALUES (%s, %s, %s, %s, %s);
        """
    )
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                cur.execute(command, (date_value, weekday, year, quarter, month))
                conn.commit()
                result = {"success": f"Inserted date: {date_value}"}
                return json.dumps(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


# Function to generate the DimDateTable for a given year
def generate_dates_for_year(start_year: int):
    start_date = date(start_year, 1, 1)
    end_date = date(start_year, 12, 31)
    current_date = start_date

    while current_date <= end_date:
        weekday = current_date.strftime('%A')  # Day of the week
        month = current_date.month
        year = current_date.year
        quarter = (month - 1) // 3 + 1  # Quarter calculation
        
        # Insert the date into the table
        db_insert_dim_date(current_date, weekday, year, quarter, month)

        # Move to the next day
        current_date += timedelta(days=1)


# Generate dates for last year and this year
generate_dates_for_year(date.today().year - 1)  # Last year
generate_dates_for_year(date.today().year)  # This year
