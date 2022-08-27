CREATE TABLE `animal` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `zoo_id` bigint(20) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `gender` int(11) DEFAULT 0,
  `number_of_legs` int(11) DEFAULT 0,
  PRIMARY KEY (`id`)
);
