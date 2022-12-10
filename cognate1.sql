-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 10, 2022 at 10:21 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cognate1`
--

-- --------------------------------------------------------

--
-- Table structure for table `2022-11-13`
--

CREATE TABLE `2022-11-13` (
  `Name` varchar(255) NOT NULL,
  `TimeIn` varchar(255) DEFAULT NULL,
  `TimeOut` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `2022-11-13`
--

INSERT INTO `2022-11-13` (`Name`, `TimeIn`, `TimeOut`) VALUES
('Art Lisboa', '05:03 PM', '06:39 PM'),
('DIGNOS,JAMES DELA CRUZ', '05:23 PM', NULL),
('Name', '05:02 PM', '06:35 PM'),
('Nayeon', '05:29 PM', NULL),
('SOTTO,ERICA C', '05:23 PM', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `2022-11-15`
--

CREATE TABLE `2022-11-15` (
  `Name` varchar(255) NOT NULL,
  `TimeIn` varchar(255) DEFAULT NULL,
  `TimeOut` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `2022-11-15`
--

INSERT INTO `2022-11-15` (`Name`, `TimeIn`, `TimeOut`) VALUES
('Art Lisboa', '03:40 PM', NULL),
('DIGNOS,JAMES DELA CRUZ', '03:41 PM', NULL),
('LISBOA,ARTMILLEN COYUCA', '03:24 PM', '07:51 PM');

-- --------------------------------------------------------

--
-- Table structure for table `2022-11-16`
--

CREATE TABLE `2022-11-16` (
  `Name` varchar(255) NOT NULL,
  `TimeIn` varchar(255) DEFAULT NULL,
  `TimeOut` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `2022-11-16`
--

INSERT INTO `2022-11-16` (`Name`, `TimeIn`, `TimeOut`) VALUES
('Art', '12:57 PM', '01:00 PM'),
('DIGNOS,JAMES DELA CRUZ', '01:07 PM', '01:33 PM'),
('face', '01:05 PM', '01:05 PM'),
('LISBOA,ARTMILLEN COYUCA', '02:36 PM', '02:52 PM'),
('nayeon', '01:00 PM', '01:00 PM'),
('test', '12:56 PM', '01:00 PM');

-- --------------------------------------------------------

--
-- Table structure for table `2022-11-17`
--

CREATE TABLE `2022-11-17` (
  `Name` varchar(255) NOT NULL,
  `TimeIn` varchar(255) DEFAULT NULL,
  `TimeOut` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `2022-11-17`
--

INSERT INTO `2022-11-17` (`Name`, `TimeIn`, `TimeOut`) VALUES
('CUMPA,REYVINCENT BLAUTA', '11:26 AM', '11:04 PM'),
('DIGNOS,JAMES DELA CRUZ', '11:23 AM', '11:05 PM'),
('LISBOA,ARTMILLEN COYUCA', '11:19 AM', '11:22 AM');

-- --------------------------------------------------------

--
-- Table structure for table `2022-11-18`
--

CREATE TABLE `2022-11-18` (
  `Name` varchar(255) NOT NULL,
  `TimeIn` varchar(255) DEFAULT NULL,
  `TimeOut` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `2022-11-18`
--

INSERT INTO `2022-11-18` (`Name`, `TimeIn`, `TimeOut`) VALUES
('CUMPA,REYVINCENT BLAUTA', '10:46 AM', '10:47 AM'),
('ROXAS,JEZAIL GIVA', '11:05 AM', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `2022-11-28`
--

CREATE TABLE `2022-11-28` (
  `Name` varchar(255) NOT NULL,
  `TimeIn` varchar(255) DEFAULT NULL,
  `TimeOut` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `2022-12-10`
--

CREATE TABLE `2022-12-10` (
  `Name` varchar(255) NOT NULL,
  `TimeIn` varchar(255) DEFAULT NULL,
  `TimeOut` varchar(255) DEFAULT NULL,
  `Status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `2022-12-10`
--

INSERT INTO `2022-12-10` (`Name`, `TimeIn`, `TimeOut`, `Status`) VALUES
('CUMPA,REYVINCENT BLAUTA', '04:48 PM', '05:11 PM', 'Time Out'),
('DIGNOS,JAMES DELA CRUZ', '05:11 PM', NULL, 'Time In');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `ID` int(11) NOT NULL,
  `username` varchar(500) NOT NULL,
  `password` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`ID`, `username`, `password`) VALUES
(1, 'admin', 'admin123');

-- --------------------------------------------------------

--
-- Table structure for table `masterlist`
--

CREATE TABLE `masterlist` (
  `ID` varchar(200) NOT NULL,
  `Name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `masterlist`
--

INSERT INTO `masterlist` (`ID`, `Name`) VALUES
('1831209348', 'LISBOA,ARTMILLEN COYUCA'),
('4825210726', 'cumpa,reyvincent blauta');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `2022-11-13`
--
ALTER TABLE `2022-11-13`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `2022-11-15`
--
ALTER TABLE `2022-11-15`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `2022-11-16`
--
ALTER TABLE `2022-11-16`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `2022-11-17`
--
ALTER TABLE `2022-11-17`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `2022-11-18`
--
ALTER TABLE `2022-11-18`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `2022-11-28`
--
ALTER TABLE `2022-11-28`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `2022-12-10`
--
ALTER TABLE `2022-12-10`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `masterlist`
--
ALTER TABLE `masterlist`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
