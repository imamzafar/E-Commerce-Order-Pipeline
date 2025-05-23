
  create or replace   view ecommerce_db.analytics.stg_shipments
  
   as (
    SELECT *
FROM raw.shipments
  );

