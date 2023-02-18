-- THIS WILL BE RUN IN BIGQUERY 
CREATE VIEW `raw_bikesharing.dm_regional_manager`
AS
SELECT region_id, SUM(capacity) as total_capacity
FROM `dataengpart1.raw_bikesharing.stations`
WHERE region_id != ''
GROUP BY region_id
ORDER BY total_capacity desc
LIMIT 2;

-- THEN ACCESS VIEW WITH CODE 
SELECT * FROM `dataengpart1.raw_bikesharing.dm_regional_manager`; 
