-- Task 3: List all tables in the current database
SELECT TABLE_NAME AS "Table Name"
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = DATABASE();
