-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 05, 2026 at 05:27 PM
-- Server version: 5.7.24
-- PHP Version: 8.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sie557_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `generation`
--

CREATE TABLE `generation` (
  `Generation_ID` int(11) NOT NULL,
  `Generation_Type` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `generation`
--

INSERT INTO `generation` (`Generation_ID`, `Generation_Type`) VALUES
(1, 'Biomass'),
(2, 'Solar'),
(3, 'Hydro'),
(4, 'Waste'),
(5, 'Wind'),
(6, 'Other'),
(7, 'Oil'),
(8, 'Gas'),
(9, 'Battery'),
(10, 'Landfill, Gas');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `generation`
--
ALTER TABLE `generation`
  ADD PRIMARY KEY (`Generation_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `generation`
--
ALTER TABLE `generation`
  MODIFY `Generation_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
