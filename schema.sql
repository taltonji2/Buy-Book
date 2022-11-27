CREATE DATABASE [IF NOT EXIST] `buy_book_schema` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE book (
  id INT NOT NULL AUTO_INCREMENT,
  bibliography_id INT NOT NULL,
  PRIMARY KEY (book_id),
  FOREIGN KEY (bibliography_id) REFERENCES bibliography(id);
);

CREATE TABLE bibliography (
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  author VARCHAR(50) NOT NULL,
  genre VARCHAR(50),
  description VARCHAR(500),
  publisher VARCHAR(100),
  publication_year VARCHAR(4),
  page_count INT,
  volume INT,
  PRIMARY KEY (id);
);