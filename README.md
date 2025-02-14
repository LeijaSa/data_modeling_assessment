# data_modeling_assessment

Proper Error handling in the service methods and scheduled updates is not implemented!


Reasoning behind my model -Key intrest is to create reports of book sales

The fact table FactSales is the central table in this model and records every individual book sale as a row. This is designed for high granularity, enabling detailed analysis of sales performance.

Why this structure?

It captures all key measurable metrics for book sales, such as price_at_purchase (new -if price changes in the book dimension), quantity and discount_amount. I added Net_sales_amount although it could be easily counted in power bi..

Columns like sale_date_id, book_id, customer_id and store_id link this table to the respective dimensions, enabling comprehensive drill-down analysis.
Payment-related attributes (e.g., discount_type and payment_type) are included for insights into payment trends and discount usage.

Book dimension stores details about books sold, such as book_title, author, publisher and genre/category.
Reporting Use Case: Enables reporting on top-performing authors, genres and publishers.

Customer dimension captures static details about customers, including country, city, birth_date, gender and status.
Reporting Use Case: Facilitates analysis of sales by customer demographics, such as age groups or geographic regions. 

Store dimension holds store-related attributes like store_name, store_city, store_country and store_type.
Reporting Use Case: Helps analyze store performance, such as identifying high-performing stores by location or type.

Task 2

The CustomerYearlySummary table aggregates customer activity by summarizing their total purchases. Table is updated daily/weekly/monthly? depending on the policy of the store. This table simplifies queries related to yearly customer performance, eliminating the need for complex aggregations on the fact table (FactSales) each time (yearly) the data is queried.

The LoyaltyLevelHistory dimension is an SCD Type 2 table that tracks changes in customer loyalty program levels over time. This ensures that any changes in loyalty levels are preserved historically. At the end of each year, the summary table is reviewed and if the total purchases exceed a certain threshold, a new record is added, while the previous record is updated with an end_date and is_active = false. If the end_date is NULL, it indicates that the loyalty level is currently active. This setup ensures that only one unique record for each loyalty level exists per customer for a given time period.
Reporting Use Case: This structure allows time-based analysis of customer behavior by loyalty level, providing insights into how customers' loyalty statuses evolve over time.
