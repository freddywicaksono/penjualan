-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 10, 2024 at 11:10 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kamehame`
--

-- --------------------------------------------------------

--
-- Table structure for table `penjualan_detail`
--

CREATE TABLE `penjualan_detail` (
  `id` int(11) NOT NULL,
  `kode` varchar(20) NOT NULL,
  `nomor_bukti` varchar(10) NOT NULL,
  `kode_barang` varchar(10) NOT NULL,
  `qty` int(11) NOT NULL DEFAULT 1,
  `harga` int(11) NOT NULL,
  `subtotal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `penjualan_detail`
--

INSERT INTO `penjualan_detail` (`id`, `kode`, `nomor_bukti`, `kode_barang`, `qty`, `harga`, `subtotal`) VALUES
(1, '}\\;73', '1001', '2001', 1, 2000000, 2000000),
(2, 'FRM4F', '1001', '2002', 1, 2500000, 2500000),
(3, '?hl#U', '1002', '2003', 1, 1500000, 1500000),
(4, 'p7_e}', '1002', '2004', 1, 600000, 600000),
(5, 'H(3KV', '1003', '2002', 1, 2500000, 2500000),
(6, 'vV4cu', '1003', '2003', 1, 1500000, 1500000),
(7, 'Jry?a', '1004', '2002', 1, 2500000, 2500000),
(8, '[)ts2', '1005', '2001', 1, 2000000, 2000000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `penjualan_detail`
--
ALTER TABLE `penjualan_detail`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode` (`kode`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `penjualan_detail`
--
ALTER TABLE `penjualan_detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
