-- Create database (hbtn_0d_usa) and table (states)
-- Include id INT unique, name VARCHAR(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    name VACHAR(256) NOT NULL,
    PRIMARY KEY (id)
);