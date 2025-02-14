
    # Insert Book
    db_insert_dim_book("The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's Sons", "English", 15.99, "Fiction")

    # Insert Store
    db_insert_dim_store("Bookstore A", "USA", "New York", "Retail")

    # Insert Customer
    db_insert_dim_customer("USA", "New York", "1985-06-15", "M")

    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(1, "Gold", True, today)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(1, 1200.00, 2024)

# Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 1, 1, 1, 1, 12.99, 2, 2.00, 25.98, "Percentage", "Credit Card")


 # Insert Book
    db_insert_dim_book("1984", "George Orwell", "Secker & Warburg", "English", 12.99, "Dystopian")

    # Insert Store
    db_insert_dim_store("Bookstore B", "USA", "Los Angeles", "Retail")

    # Insert Customer
    db_insert_dim_customer("USA", "Los Angeles", "1992-11-30", "F")

    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(2, "Silver", True, today)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(2, 800.00, 2024)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 2, 2, 2, 2, 10.99, 1, 1.00, 9.99, "Flat", "Debit Card")


    # Insert Book
    db_insert_dim_book("To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.", "English", 18.50, "Fiction")

    # Insert Store
    db_insert_dim_store("Bookstore C", "Canada", "Toronto", "Online")

    # Insert Customer
    db_insert_dim_customer("Canada", "Toronto", "1990-03-22", "M")

    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(3, "Bronze", True, today)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(3, 450.00, 2024)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 3, 3, 3, 3, 18.50, 3, 0.00, 55.50, "None", "PayPal")


    # Insert Book
    db_insert_dim_book("Pride and Prejudice", "Jane Austen", "T. Egerton", "English", 10.75, "Romance")

    # Insert Store
    db_insert_dim_store("Bookstore D", "UK", "London", "Retail")

    # Insert Customer
    db_insert_dim_customer("UK", "London", "1980-01-05", "F")

    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(4, "Silver", True, today)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(4, 700.00, 2024)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 4, 4, 4, 4, 10.75, 5, 1.50, 53.75, "Percentage", "Credit Card")


    # Insert Book
    db_insert_dim_book("Moby-Dick", "Herman Melville", "Harper & Brothers", "English", 25.99, "Adventure")

    # Insert Store
    db_insert_dim_store("Bookstore E", "USA", "Chicago", "Online")

    # Insert Customer
    db_insert_dim_customer("USA", "Chicago", "1975-09-10", "M")

    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(5, "Gold", True, today)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(5, 1500.00, 2024)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 5, 5, 5, 5, 25.99, 2, 3.00, 48.98, "Flat", "Credit Card")


    # Insert Book
    db_insert_dim_book("The Catcher in the Rye", "J.D. Salinger", "Little, Brown and Company", "English", 13.50, "Classic")

    # Insert Store
    db_insert_dim_store("Bookstore F", "USA", "San Francisco", "Retail")

    # Insert Customer
    db_insert_dim_customer("USA", "San Francisco", "1995-04-12", "F")

    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(6, "Bronze", True, today)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(6, 350.00, 2024)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 6, 6, 6, 6, 13.50, 1, 1.00, 12.50, "Percentage", "Debit Card")

    # Insert Book
db_insert_dim_book("The Hobbit", "J.R.R. Tolkien", "George Allen & Unwin", "English", 22.95, "Fantasy")

# Insert Store
db_insert_dim_store("Bookstore G", "Australia", "Sydney", "Retail")

# Insert Customer
db_insert_dim_customer("Australia", "Sydney", "1988-12-05", "M")

# Insert Loyalty Level History (active)
db_insert_dim_loyalty_level_history(7, "Silver", True, today)

# Insert Customer Yearly Summary
db_insert_dim_customer_yearly_summary(7, 950.00, 2024)

# Insert Sales (today)
db_insert_fact_sales(sale_date_id, 7, 7, 7, 7, 22.95, 2, 4.00, 41.90, "Percentage", "Credit Card")


# Insert Book
db_insert_dim_book("Wuthering Heights", "Emily Brontë", "Thomas Cautley Newby", "English", 14.99, "Romance")

# Insert Store
db_insert_dim_store("Bookstore H", "USA", "Seattle", "Retail")

# Insert Customer
db_insert_dim_customer("USA", "Seattle", "1994-07-30", "F")

# Insert Loyalty Level History (active)
db_insert_dim_loyalty_level_history(8, "Bronze", True, today)

# Insert Customer Yearly Summary
db_insert_dim_customer_yearly_summary(8, 620.00, 2024)

# Insert Sales (today)
db_insert_fact_sales(sale_date_id, 8, 8, 8, 8, 14.99, 1, 1.00, 13.99, "Flat", "Debit Card")


# Insert Book
db_insert_dim_book("Frankenstein", "Mary Shelley", "Lackington, Hughes, Harding, Mavor & Jones", "English", 19.99, "Horror")

# Insert Store
db_insert_dim_store("Bookstore I", "Canada", "Vancouver", "Online")

# Insert Customer
db_insert_dim_customer("Canada", "Vancouver", "1982-11-15", "M")

# Insert Loyalty Level History (active)
db_insert_dim_loyalty_level_history(9, "Gold", True, today)

# Insert Customer Yearly Summary
db_insert_dim_customer_yearly_summary(9, 1250.00, 2024)

# Insert Sales (today)
db_insert_fact_sales(sale_date_id, 9, 9, 9, 9, 19.99, 3, 2.00, 57.97, "Flat", "PayPal")


# Insert Book
db_insert_dim_book("Dracula", "Bram Stoker", "Archibald Constable and Company", "English", 16.50, "Horror")

# Insert Store
db_insert_dim_store("Bookstore J", "UK", "Manchester", "Retail")

# Insert Customer
db_insert_dim_customer("UK", "Manchester", "1990-02-25", "M")

# Insert Loyalty Level History (active)
db_insert_dim_loyalty_level_history(10, "Silver", True, today)

# Insert Customer Yearly Summary
db_insert_dim_customer_yearly_summary(10, 800.00, 2024)

# Insert Sales (today)
db_insert_fact_sales(sale_date_id, 10, 10, 10, 10, 16.50, 4, 1.50, 64.50, "Percentage", "Credit Card")




    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(1, 1200.00, 2025)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 1, 1, 1, 1, 12.99, 2, 2.00, 25.98, "Percentage", "Credit Card")


    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(2, 800.00, 2025)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 2, 2, 2, 2, 10.99, 1, 1.00, 9.99, "Flat", "Debit Card")


    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(3, 450.00, 2025)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 3, 3, 3, 3, 18.50, 3, 0.00, 55.50, "None", "PayPal")


    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(4, 700.00, 2025)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 4, 4, 4, 4, 10.75, 5, 1.50, 53.75, "Percentage", "Credit Card")


    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(5, 1500.00, 2025)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 5, 5, 5, 5, 25.99, 2, 3.00, 48.98, "Flat", "Credit Card")


    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(6, 350.00, 2025)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 6, 6, 6, 6, 13.50, 1, 1.00, 12.50, "Percentage", "Debit Card")


    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(7, 950.00, 2025)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 7, 7, 7, 7, 22.95, 2, 4.00, 41.90, "Percentage", "Credit Card")


    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(8, 620.00, 2025)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 8, 8, 8, 8, 14.99, 1, 1.00, 13.99, "Flat", "Debit Card")


    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(9, 1250.00, 2025)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 9, 9, 9, 9, 19.99, 3, 2.00, 57.97, "Flat", "PayPal")

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(10, 800.00, 2025)

    # Insert Sales (today)
    db_insert_fact_sales(sale_date_id, 10, 10, 10, 10, 16.50, 4, 1.50, 64.50, "Percentage", "Credit Card")
   


     # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(1, "Gold", True, last_year)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(1, 1200.00, 2025)



    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(2, "Silver", True, last_year)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(2, 800.00, 2025)



    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(3, "Bronze", True, last_year)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(3, 450.00, 2025)



    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(4, "Silver", True, last_year)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(4, 700.00, 2025)



    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(5, "Gold", True, last_year)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(5, 1500.00, 2025)



    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(6, "Bronze", True, last_year)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(6, 350.00, 2025)


    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(7, "Silver", True, last_year)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(7, 950.00, 2025)



    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(8, "Bronze", True, last_year)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(8, 620.00, 2025)


    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(9, "Gold", True, last_year)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(9, 1250.00, 2025)



    # Insert Loyalty Level History (active)
    db_insert_dim_loyalty_level_history(10, "Silver", True, last_year)

    # Insert Customer Yearly Summary
    db_insert_dim_customer_yearly_summary(10, 800.00, 2025)