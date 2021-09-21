-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Login_Reg
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Login_Reg
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Login_Reg` DEFAULT CHARACTER SET utf8 ;
USE `Login_Reg` ;

-- -----------------------------------------------------
-- Table `Login_Reg`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Login_Reg`.`Users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` CHAR(8) NULL,
  `pw conf` CHAR(8) NULL,
  `created_at` DATETIME NULL DEFAULT NOW (),
  `updated_at` DATETIME NULL DEFAULT 'NOW () on update NOW()',
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
