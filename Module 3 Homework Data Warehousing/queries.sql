---------------------------------------------------------------------------------------------#
--Question 01 
SELECT
    COUNT(*) AS total_records
FROM
    `project-64bdb451-6256-421c-aa5.taxy_rides_ny.native_table_yellow`;


---------------------------------------------------------------------------------------------#
--Question 02
SELECT
  COUNT(DISTINCT PULocationID) AS distinct_pulocationids
FROM `project-64bdb451-6256-421c-aa5.taxy_rides_ny.external_yellow_2024`;


SELECT
  COUNT(DISTINCT PULocationID) AS distinct_pulocationids
FROM `project-64bdb451-6256-421c-aa5.taxy_rides_ny.native_table_yellow`;


---------------------------------------------------------------------------------------------#
--Question 03

SELECT
    PULocationID
FROM
    `project-64bdb451-6256-421c-aa5.taxy_rides_ny.native_table_yellow`;


SELECT
    PULocationID,
    DOLocationID
FROM
    `project-64bdb451-6256-421c-aa5.taxy_rides_ny.native_table_yellow`;

--Question 04
SELECT
  COUNT(*) AS total_records_zero_fare
FROM
  `project-64bdb451-6256-421c-aa5.taxy_rides_ny.native_table_yellow`
WHERE
  fare_amount = 0;

--Question 05
CREATE TABLE taxy_rides_ny.optimized_trips
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT *
FROM taxy_rides_ny.native_table_yellow;

--Questin 06
SELECT DISTINCT VendorID
FROM `project-64bdb451-6256-421c-aa5.taxy_rides_ny.native_table_yellow`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15 23:59:59';


SELECT DISTINCT VendorID
FROM `project-64bdb451-6256-421c-aa5.taxy_rides_ny.optimized_trips`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15 23:59:59';


--Question 09 
SELECT count(*) query FROM `project-64bdb451-6256-421c-aa5.taxy_rides_ny.native_table_yellow`
