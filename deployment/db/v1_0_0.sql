CREATE DATABASE IF NOT EXISTS prework;

use prework;

CREATE TABLE IF NOT EXISTS users
(
    id         int          NOT NULL AUTO_INCREMENT,
    last_name  varchar(255) NOT NULL,
    first_name varchar(255),
    age        int,
    PRIMARY KEY (id)
);

CREATE INDEX idx_fullname ON users (first_name, last_name);
