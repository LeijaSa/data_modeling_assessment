import psycopg2
from config import config
import json
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


def db_insert_dim_book(book_title: str, author: str, publisher: str, language: str, price: float, genre_category: str):
    command = (
        """
        INSERT INTO DimBook (book_title, author, publisher, language, price, genre_category) 
        VALUES (%s, %s, %s, %s, %s, %s);
        """
    )
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                cur.execute(command, (book_title, author, publisher, language, price, genre_category))
                conn.commit()
                result = {"success": f"Inserted book: {book_title}"}
                return json.dumps(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def db_insert_dim_store(store_name: str, store_country: str, store_city: str, store_type: str):
    command = (
        """
        INSERT INTO DimStore (store_name, store_country, store_city, store_type) 
        VALUES (%s, %s, %s, %s);
        """
    )
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                cur.execute(command, (store_name, store_country, store_city, store_type))
                conn.commit()
                result = {"success": f"Inserted store: {store_name}"}
                return json.dumps(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def db_insert_dim_customer(country: str, city: str, birth_date: date, gender: str):
    command = (
        """
        INSERT INTO DimCustomer (country, city, birth_date, gender) 
        VALUES (%s, %s, %s, %s);
        """
    )
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                cur.execute(command, (country, city, birth_date, gender))
                conn.commit()
                result = {"success": "Inserted customer in city: %s" % city}
                return json.dumps(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def db_insert_dim_loyalty_level_history(customer_id: int, loyalty_program_level: str, is_active: bool, start_date: date, end_date: date = None):
    command = (
        """
        INSERT INTO DimLoyaltyLevelHistory (customer_id, loyalty_program_level, is_active, start_date, end_date) 
        VALUES (%s, %s, %s, %s, %s);
        """
    )
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                cur.execute(command, (customer_id, loyalty_program_level, is_active, start_date, end_date))
                conn.commit()
                result = {"success": f"Inserted loyalty history for customer_id: {customer_id}"}
                return json.dumps(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)



def db_insert_dim_customer_yearly_summary(customer_id: int, total_purchases: float, year: int):
    command = (
        """
        INSERT INTO DimCustomerYearlySummary (customer_id, total_purchases, year) 
        VALUES (%s, %s, %s);
        """
    )
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                cur.execute(command, (customer_id, total_purchases, year))
                conn.commit()
                result = {"success": f"Inserted yearly summary for customer_id: {customer_id}"}
                return json.dumps(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def db_insert_fact_sales(sale_date_id: int, book_id: int, customer_id: int, store_id: int, loyalty_program_level_id: int, 
                         price_at_purchase: float, quantity: int, discount_amount: float, 
                         net_sales_amount: float, discount_type: str, payment_type: str):
    command = (
        """
        INSERT INTO FactSales (sale_date_id, book_id, customer_id, store_id, loyalty_program_level_id, 
                               price_at_purchase, quantity, discount_amount, net_sales_amount, 
                               discount_type, payment_type) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
    )
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                cur.execute(command, (sale_date_id, book_id, customer_id, store_id, loyalty_program_level_id, 
                                      price_at_purchase, quantity, discount_amount, net_sales_amount, 
                                      discount_type, payment_type))
                conn.commit()
                result = {"success": f"Inserted sale record with sale_date_id: {sale_date_id}"}
                return json.dumps(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def get_sale_date_id_for_today(day):
    
    command = "SELECT id FROM DimDateTable WHERE date = %s"
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                cur.execute(command, (day,))
                sale_date_id = cur.fetchone()[0]
                return sale_date_id
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        return None


if __name__ == "__main__":
    today = date.today()
    days_ago = today - timedelta(days=3)
    last_year = today - relativedelta(years=1)
    sale_date_id = get_sale_date_id_for_today(days_ago)

    # Insert Book
    db_insert_dim_book("The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's Sons", "English", 15.99, "Fiction")

    # Insert Store
    db_insert_dim_store("Bookstore A", "USA", "New York", "Retail")

    # Insert Customer
    db_insert_dim_customer("USA", "New York", "1985-06-15", "M")

    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(1, "Gold", True, today)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(1, 1200.00, 2025)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 1, 1, 1, 1, 12.99, 2, 2.00, 25.98, "Percentage", "Credit Card")

 

