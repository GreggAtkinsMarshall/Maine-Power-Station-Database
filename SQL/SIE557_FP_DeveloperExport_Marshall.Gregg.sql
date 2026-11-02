-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 05, 2026 at 05:36 PM
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
-- Table structure for table `developer`
--

CREATE TABLE `developer` (
  `Developer_ID` int(11) NOT NULL,
  `Developer_Name` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `developer`
--

INSERT INTO `developer` (`Developer_ID`, `Developer_Name`) VALUES
(1, '549 Doles Ridge Rd Solar LLC'),
(2, 'Acton H Road Solar 1, LLC'),
(3, 'AES Clean Energy'),
(4, 'AES Distributed Energy'),
(5, 'Agilitas Energy, Inc.'),
(6, 'Algonquin Northern Maine'),
(7, 'Altus Power America Management, LLC'),
(8, 'Arctaris Saddleback Solar, LLC'),
(9, 'Arevon Energy, Inc.'),
(10, 'Athens Energy, LLC'),
(11, 'BAP Grounded 2 LLC'),
(12, 'BD Solar 1 LLC'),
(13, 'BD Solar 2 LLC'),
(14, 'BD Solar Auburn LLC'),
(15, 'BD Solar Augusta LLC'),
(16, 'BD Solar Fairfield LLC'),
(17, 'BD Solar Hancock LLC'),
(18, 'BD Solar Hancock North LLC'),
(19, 'BD Solar Lewiston Junction LLC'),
(20, 'BD Solar Oxford LLC'),
(21, 'BD Solar Palmyra LLC'),
(22, 'Brassua Hydroelectric LP'),
(23, 'Brookfield Black Bear Hydro, LLC'),
(24, 'Brookfield Power New England'),
(25, 'Brookfield White Pine Hydro LLC'),
(26, 'Bucksport Generation LLC'),
(27, 'Casco Bay Energy Co LLC'),
(28, 'CleanCapital Holdings'),
(29, 'CPV Beaver Ridge Wind LLC'),
(30, 'CPV Canton Mountain Wind LLC'),
(31, 'CPV Saddleback Ridge Wind, LLC'),
(32, 'CPV Spruce Mountain Wind LLC'),
(33, 'Cross Town Energy Storage LLC'),
(34, 'Dimension Energy LLC'),
(35, 'Downeast Wind, LLC'),
(36, 'Dublin Street LLC'),
(37, 'Eagle Creek Renewable Energy, LLC'),
(38, 'Eagle Point Energy Center, LLC'),
(39, 'Eastern Maine Medical Center'),
(40, 'Easton CSG 1 LLC'),
(41, 'Ecomaine'),
(42, 'Emery Meadow Solar Station, LLC'),
(43, 'Essex Hydro Associates LLC'),
(44, 'Evergreen Wind, LLC'),
(45, 'Farmington Solar, LLC'),
(46, 'Fox Island Wind LLC'),
(47, 'FPL Energy Cape LLC'),
(48, 'FPL Energy Wyman LLC'),
(49, 'Freedom Pine Solar, LLC'),
(50, 'Great Lakes Hydro America LLC'),
(51, 'Green Mile Solar, LLC'),
(52, 'Green Mountain Power Corp'),
(53, 'Greenbacker Renewable Energy Corporation'),
(54, 'Hayworth Solar Partners, LLC'),
(55, 'Helix Maine Wind Development, LLC'),
(56, 'Hydro Kennebec LLC'),
(57, 'KEI (Maine) Power Management (II) LLC'),
(58, 'KEI (Maine) Power Management (III) LLC'),
(59, 'KEI (Maine) Power Management (IV) LLC'),
(60, 'Lewiston City of'),
(61, 'Limestone CSG 1 LLC'),
(62, 'Limestone CSG 2 LLC'),
(63, 'Livermore Falls CSG, LLC'),
(64, 'Luminace Sunbeam Development Holdings, LLC'),
(65, 'Madison Energy Holdings LLC'),
(66, 'Madison Energy Investments LLC'),
(67, 'Maine DG Solar Augusta, LLC'),
(68, 'Maine DG Solar Baldwin, LLC'),
(69, 'Maine DG Solar Harmony, LLC'),
(70, 'Maine DG Solar Monmouth, LLC'),
(71, 'Maine DG Solar Pittsfield, LLC'),
(72, 'Maine Waste to Energy'),
(73, 'Mars Hill Road Solar Farm, LLC'),
(74, 'ME CDG 004 LLC'),
(75, 'ME CDG 005 LLC'),
(76, 'ME Fort Fairfield LLC'),
(77, 'ME Sandy River LLC'),
(78, 'Merimil Ltd Partnership'),
(79, 'Messalonskee Stream Hydro LLC'),
(80, 'MEVS Clark LLC'),
(81, 'MEVS DOT, LLC'),
(82, 'Milo CSG, LLC'),
(83, 'MN8 Energy LLC'),
(84, 'Naples Casco Solar 1, LLC'),
(85, 'Nautilus Solar Solutions'),
(86, 'Navisun LLC'),
(87, 'ND Paper, Inc.'),
(88, 'NextGrid Bitterbush, LLC'),
(89, 'NextGrid Cliffrose, LLC'),
(90, 'NextGrid Corkwood, LLC'),
(91, 'NextGrid Mangrove, LLC'),
(92, 'NextGrid Mastic, LLC'),
(93, 'NextGrid Peppertree, LLC'),
(94, 'NJR Clean Energy Ventures Corporation'),
(95, 'Norridgewock River Road Solar, LLC'),
(96, 'Onward Energy'),
(97, 'Overlook Solar Partners, LLC'),
(98, 'Penobscot Narrows Solar I LLC'),
(99, 'Pisgah Mountain, LLC'),
(100, 'Pittsfiled Solar LLC'),
(101, 'REA Investments, LLC'),
(102, 'REC RWD, LLC'),
(103, 'Record Hill Wind LLC'),
(104, 'ReEnergy Livermore Falls'),
(105, 'ReEnergy Stratton LLC'),
(106, 'Relevate Power Management LLC'),
(107, 'Robbins Lumber Inc'),
(108, 'RoxWind LLC'),
(109, 'Rumford Power'),
(110, 'Samoset Solar, LLC'),
(111, 'Sanford Airport Solar, LLC'),
(112, 'Sanford ESS, LLC'),
(113, 'Sappi Fine Paper North America-Somerset'),
(114, 'Shining Solar Partners, LLC'),
(115, 'SoCore Energy LLC'),
(116, 'SOL ME Augusta 13 York Farm, LLC'),
(117, 'Solar Mule, LLC'),
(118, 'South Portland ESS, LLC'),
(119, 'Southern Power Co'),
(120, 'Standard Solar'),
(121, 'Stored Solar J&WE'),
(122, 'Three Corners Solar, LLC'),
(123, 'Three Rivers Solar Power, LLC'),
(124, 'Topsham Hydro Partners'),
(125, 'Topsham Meadow Solar Station LLC'),
(126, 'Tower Solar Partners, LLC'),
(127, 'Turner Meadow Solar Station, LLC'),
(128, 'Twin Rivers Paper Co LLC'),
(129, 'Valley Sun Solar LLC'),
(130, 'VCP Realty, LLC'),
(131, 'Walden Renewables Development LLC'),
(132, 'Walden Solar Maine V LLC'),
(133, 'Warren Meadow Solar Station, LLC'),
(134, 'WEB Silver Maple Wind LLC'),
(135, 'West Baldwin Solar Station LLC'),
(136, 'Westbound Solar 3, LLC'),
(137, 'Westbrook Energy Center'),
(138, 'WM Renewable Energy LLC'),
(139, 'Woodland Pulp LLC'),
(140, 'Wyman Hill Solar, LLC'),
(264, 'gregg'),
(265, 'gregg'),
(266, 'gregg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `developer`
--
ALTER TABLE `developer`
  ADD PRIMARY KEY (`Developer_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `developer`
--
ALTER TABLE `developer`
  MODIFY `Developer_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=267;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
