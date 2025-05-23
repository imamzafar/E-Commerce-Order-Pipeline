
  create or replace   view ecommerce_db.analytics.stg_customers
  
   as (
    SELECT *
FROM raw.customers
  );

