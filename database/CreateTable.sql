CREATE TABLE IF NOT EXISTS dateTable
(
id INTEGER NOT NULL AUTO_INCREMENT,
dateGenerate VARCHAR(20) NOT NULL,
share VARCHAR(250) NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;