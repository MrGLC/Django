

CREATE TABLE `test_table` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `test_table` VALUES
('1', 'Sample data 1'),
('2', 'Sample data 2');
