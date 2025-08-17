-- Task 4: Full description of the BOOKS table
SELECT COLUMN_NAME AS "Column Name",
       DATA_TYPE AS "Data Type",
       IS_NULLABLE AS "Nullable",
       COLUMN_KEY AS "Key",
       COLUMN_DEFAULT AS "Default Value",
       EXTRA AS "Extra Info"
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'BOOKS';
