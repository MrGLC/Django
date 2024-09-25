<?php

class Database {
    private $host = "db";
    private $username = "your_username";
    private $password = "your_password";
    private $database = "your_dbname";
    private $conn;

    public function __construct() {
        $this->connect();
    }

    private function connect() {
        $this->conn = new mysqli($this->host, $this->username, $this->password, $this->database);

        if ($this->conn->connect_error) {
            die("Connection failed: " . $this->conn->connect_error);
        }
    }

    public function createItem($name, $description) {
        $stmt = $this->conn->prepare("INSERT INTO items (name, description) VALUES (?, ?)");
        $stmt->bind_param("ss", $name, $description);
        $stmt->execute();
        $stmt->close();
    }

    public function readItems() {
        $sql = "SELECT id, name, description FROM items";
        $result = $this->conn->query($sql);

        if ($result->num_rows > 0) {
            while($row = $result->fetch_assoc()) {
                echo "id: " . $row["id"]. " - Name: " . $row["name"]. " - Description: " . $row["description"]. "<br>";
            }
        } else {
            echo "0 results";
        }
    }

    public function updateItem($id, $name, $description) {
        $stmt = $this->conn->prepare("UPDATE items SET name = ?, description = ? WHERE id = ?");
        $stmt->bind_param("ssi", $name, $description, $id);
        $stmt->execute();
        $stmt->close();
    }

    public function deleteItem($id) {
        $stmt = $this->conn->prepare("DELETE FROM items WHERE id = ?");
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $stmt->close();
    }

    public function __destruct() {
        $this->conn->close();
    }
}

// Example usage
$db = new Database();
$db->createItem("Test Item", "This is a test description.");
$db->readItems();
$db->updateItem(1, "Updated Item", "This is an updated description.");
$db->deleteItem(1);

