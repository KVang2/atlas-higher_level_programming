-- Creates server user having all privileges on server
-- Password set to user_0d_1-pwd
CREATE USER if not exist 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;