
  create or replace   view ecommerce_db.analytics.stg_orders
  
   as (
    SELECT *
FROM raw.orders
  );

