-- MySQL Initialization
CREATE DATABASE ai_decision_db;
CREATE TABLE decisions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    decision TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);