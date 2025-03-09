CREATE DATABASE IF NOT EXISTS test_db;
USE test_db;

CREATE TABLE IF NOT EXISTS user_info (
    id BIGINT NOT NULL,
    name STRING NOT NULL,
    age INT NOT NULL
)
DUPLICATE KEY(id)
DISTRIBUTED BY HASH(id) BUCKETS 3
PROPERTIES (
    "replication_num" = "1"
);


INSERT INTO user_info VALUES (1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 22);

SELECT * FROM user_info;
