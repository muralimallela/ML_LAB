CREATE DATABASE IF NOT EXISTS `SampleDB`;
USE `SampleDB`;

CREATE TABLE `students` (
  `sid` varchar(10) DEFAULT NULL,
  `sname` varchar(10) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
);

INSERT INTO `students` (`sid`, `sname`, `age`) VALUES
('s521', 'Jhon Bob', 23),
('s522', 'Dilly', 22),
('s523', 'Kenney', 25),
('s524', 'Herny', 26);
