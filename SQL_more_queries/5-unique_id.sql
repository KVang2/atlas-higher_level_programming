-- Unique_id table
-- Contains id INT with default value 1, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id
(
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL,
    UNIQUE (id)
);