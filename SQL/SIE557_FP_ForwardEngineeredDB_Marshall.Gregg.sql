-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema SIE557_Project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema SIE557_Project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SIE557_Project` DEFAULT CHARACTER SET utf8 ;
USE `SIE557_Project` ;

-- -----------------------------------------------------
-- Table `SIE557_Project`.`County`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIE557_Project`.`County` (
  `County_ID` INT NOT NULL AUTO_INCREMENT,
  `County_Name` VARCHAR(45) NULL,
  PRIMARY KEY (`County_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SIE557_Project`.`Developer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIE557_Project`.`Developer` (
  `Developer_ID` INT NOT NULL AUTO_INCREMENT,
  `Developer_Name` VARCHAR(45) NULL,
  PRIMARY KEY (`Developer_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SIE557_Project`.`Generation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIE557_Project`.`Generation` (
  `Generation_ID` INT NOT NULL AUTO_INCREMENT,
  `Generation_Type` VARCHAR(45) NULL,
  PRIMARY KEY (`Generation_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SIE557_Project`.`Project`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIE557_Project`.`Project` (
  `Project_ID` INT NOT NULL AUTO_INCREMENT,
  `Project_Name` VARCHAR(45) NULL,
  `Operational_Status` VARCHAR(45) NULL,
  `Capacity_MW` DECIMAL NULL,
  `County_ID` INT NOT NULL,
  `Developer_ID` INT NOT NULL,
  `Generation_ID` INT NOT NULL,
  PRIMARY KEY (`Project_ID`),
  INDEX `fk_Project_County_idx` (`County_ID` ASC),
  INDEX `fk_Project_Developer1_idx` (`Developer_ID` ASC),
  INDEX `fk_Project_Generation1_idx` (`Generation_ID` ASC),
  CONSTRAINT `fk_Project_County`
    FOREIGN KEY (`County_ID`)
    REFERENCES `SIE557_Project`.`County` (`County_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Project_Developer1`
    FOREIGN KEY (`Developer_ID`)
    REFERENCES `SIE557_Project`.`Developer` (`Developer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Project_Generation1`
    FOREIGN KEY (`Generation_ID`)
    REFERENCES `SIE557_Project`.`Generation` (`Generation_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
