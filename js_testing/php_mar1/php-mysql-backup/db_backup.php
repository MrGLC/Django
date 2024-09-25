<?php
// ========= Database Configuration =========
$dbHost = "mysql-server";           // Docker MySQL service name
$dbUsername = "backup_user";        // Database username
$dbPassword = "backup_password";    // Database password
$dbName = "backup_db";              // Name of database you want to back up

// ========= Create Connection =========
$conn = new mysqli($dbHost, $dbUsername, $dbPassword, $dbName);

// Check connection for errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// ========= Backup Process =========
$backupFileName = 'database_backup_' . date("Y-m-d_H-i-s") . '.sql';
$sqlScript = "";

// Get all table names from the database
$tables = array();
$result = $conn->query("SHOW TABLES");
if (!$result) {
    die("Error getting table names: " . $conn->error); 
}

while ($row = $result->fetch_row()) {
    $tables[] = $row[0];
}

// Generate backup SQL statements for each table
foreach ($tables as $table) {
    // Get table structure
    $result = $conn->query("SHOW CREATE TABLE `$table`");
    if (!$result) {
        die("Error getting structure for table $table: " . $conn->error);
    }
    $row = $result->fetch_row();
    $sqlScript .= "\n\n" . $row[1] . ";\n\n";

    // Get table data
    $result = $conn->query("SELECT * FROM `$table`");
    if (!$result) {
        die("Error getting data for table $table: " . $conn->error);
    }
    $numFields = $result->field_count;

    // Initialize a flag to check if the insert statement for the table is started
    $insertStatementStarted = false;
    while ($row2 = $result->fetch_assoc()) {
        // Start the insert statement if it's not started yet
        if (!$insertStatementStarted) {
            $sqlScript .= "INSERT INTO `$table` VALUES\n";
            $insertStatementStarted = true;
        } else {
            // Add a comma before starting a new row (except for the first row)
            $sqlScript .= ",\n";
        }

        $values = "(";
        for ($i = 0; $i < $numFields; $i++) {
            $fieldInfo = $result->fetch_field_direct($i);
            $row2Value = isset($row2[$fieldInfo->name]) ? $row2[$fieldInfo->name] : '';
            $escapedValue = $conn->real_escape_string($row2Value);
            $values .= ($escapedValue === NULL) ? "NULL" : "'$escapedValue'";

            if ($i < ($numFields - 1)) {
                $values .= ", ";
            }
        }
        $values .= ")";
        $sqlScript .= $values;
    }

    if ($insertStatementStarted) {
        // End the insert statement for the current table if there were any rows
        $sqlScript .= ";\n";
    }
}

// Write SQL script to file
if (!file_put_contents($backupFileName, $sqlScript)) {
    die("Error writing backup file: " . $backupFileName);
}

// Close connection
$conn->close();

echo "Database backup created successfully: " . $backupFileName;
?>

