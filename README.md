# Customer-Orders-Analytics-Pipeline

This project builds a simple data pipeline to analyze customer orders.

it reads customer and order data, performs data quality checks, aggregates metrics per customer, cand outputs a final report.

Steps: 
1. Read customers and orders data from CSV files
2. Join orders with customers using LEFT JOIN
3. Identify orphan orders (orders without a valid customer)
4. Aggregate total orders and total spending per customer
5. Save final analytics report to CSV

Outputs :
- final_report.csv: customer-level metrics
- orphan_orders.csv: data quality issues
