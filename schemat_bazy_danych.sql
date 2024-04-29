CREATE TABLE `Books` (
  `book_id` int,
  `title` varchar(255),
  `author` varchar(255),
  `release_date` date,
  `publishing_house` varchar(255),
  `summary` varchar(255),
  `pages` int
);

CREATE TABLE `Users` (
  `user_id` int,
  `username` varchar(255),
  `email` varchar(255),
  `password` varchar(255),
  `books2return` int
);

CREATE TABLE `RentBook` (
  `user_id` int,
  `book_id` int,
  `rent_date` date,
  `deadline` date
);

CREATE TABLE `Ranking` (
  `book_id` int,
  `title` varchar(255),
  `author` varchar(255),
  `avarange_rates` float
);

CREATE TABLE `Opinions` (
  `book_id` int,
  `username` varchar(255),
  `comment` varchar(255),
  `title` varchar(255),
  `rate` int
);

CREATE TABLE `BookRating` (
  `book_id` int,
  `user_id` int,
  `rate` int
);

ALTER TABLE `BookRating` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`);

ALTER TABLE `RentBook` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`);

ALTER TABLE `Opinions` ADD FOREIGN KEY (`username`) REFERENCES `Users` (`username`);

ALTER TABLE `BookRating` ADD FOREIGN KEY (`book_id`) REFERENCES `Books` (`book_id`);

ALTER TABLE `RentBook` ADD FOREIGN KEY (`book_id`) REFERENCES `Books` (`book_id`);

ALTER TABLE `Ranking` ADD FOREIGN KEY (`book_id`) REFERENCES `Books` (`book_id`);

ALTER TABLE `Opinions` ADD FOREIGN KEY (`book_id`) REFERENCES `Books` (`book_id`);

ALTER TABLE `Ranking` ADD FOREIGN KEY (`title`) REFERENCES `Books` (`title`);

ALTER TABLE `Ranking` ADD FOREIGN KEY (`author`) REFERENCES `Books` (`author`);
