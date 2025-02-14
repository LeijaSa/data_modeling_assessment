-- Create DimBook table
CREATE TABLE DimBook (
    id SERIAL PRIMARY KEY,
    book_title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publisher VARCHAR(255) NOT NULL,
    language VARCHAR(50) NOT NULL,
    price NUMERIC(19, 2) NOT NULL,
    genre_category VARCHAR(100) NOT NULL
);

-- Create DimStore table
CREATE TABLE DimStore (
    id SERIAL PRIMARY KEY,
    store_name VARCHAR(255) NOT NULL,
    store_country VARCHAR(100) NOT NULL,
    store_city VARCHAR(100) NOT NULL,
    store_type VARCHAR(50) NOT NULL
);

-- Create DimCustomer table
CREATE TABLE DimCustomer (
    id SERIAL PRIMARY KEY,
    country VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    gender VARCHAR(10) NOT NULL
);

-- Create DimLoyaltyLevelHistory table
CREATE TABLE DimLoyaltyLevelHistory (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    loyalty_program_level VARCHAR(50) NOT NULL,
    is_active BOOLEAN NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    FOREIGN KEY (customer_id) REFERENCES DimCustomer(id)
);

-- Create DimCustomerYearlySummary table
CREATE TABLE DimCustomerYearlySummary (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    total_purchases NUMERIC(19, 2) NOT NULL,
    year INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES DimCustomer(id),
    UNIQUE (customer_id, year) -- Enforces uniqueness for each customer and year combination
);

-- Create DimDateTable table
CREATE TABLE DimDateTable (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    weekday VARCHAR(20),
    year INT NOT NULL,
    quarter INT NOT NULL,
    month INT NOT NULL
);

-- Create FactSales table
CREATE TABLE FactSales (
    sale_id SERIAL PRIMARY KEY,
    sale_date_id INT NOT NULL,
    book_id INT NOT NULL,
    customer_id INT NOT NULL,
    store_id INT NOT NULL,
    loyalty_program_level_id INT NOT NULL,
    price_at_purchase NUMERIC(19, 2) NOT NULL,
    quantity INT NOT NULL,
    discount_amount NUMERIC(19, 2) NOT NULL,
    net_sales_amount NUMERIC(19, 2) NOT NULL,
    discount_type VARCHAR(50) NOT NULL,
    payment_type VARCHAR(50) NOT NULL,
    FOREIGN KEY (sale_date_id) REFERENCES DimDateTable(id),
    FOREIGN KEY (book_id) REFERENCES DimBook(id),
    FOREIGN KEY (customer_id) REFERENCES DimCustomer(id),
    FOREIGN KEY (store_id) REFERENCES DimStore(id),
    FOREIGN KEY (loyalty_program_level_id) REFERENCES DimLoyaltyLevelHistory(id)
);
