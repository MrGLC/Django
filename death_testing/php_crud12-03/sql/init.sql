CREATE TABLE items (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some initial data
INSERT INTO items (name, description) VALUES ('Sample Item 1', 'Description for item 1');
INSERT INTO items (name, description) VALUES ('Sample Item 2', 'Description for item 2');

