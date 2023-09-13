-- Test table.

CREATE DATABASE IF NOT EXISTS `app_template`;

USE app_template;

CREATE TABLE `item` (
  `int_id` int unsigned AUTO_INCREMENT,
  `id` varchar(36) NOT NULL,
  `title` varchar(256) DEFAULT NULL,
  `properties` text,
  PRIMARY KEY (`id`),
  KEY `int_id` (`int_id`)
);
