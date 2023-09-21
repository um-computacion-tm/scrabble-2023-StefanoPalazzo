# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.2.4] - 2023-09-21

### Changed

- Now 'validate_word_overlapping_is_possible' receives words as a string instead of tiles
- Now 'validate_tiles_for_word' receives words as a string instread of tiles
- Tests were updated to send words as a String

## [0.2.3] - 2023-09-18

### Added

- Function to verify if word overlapping is possible (they share the intersection letter)


## [0.2.2] - 2023-09-17

### Added

- Function to verify if the first word passes through the center
- FUnction to verify if the word is connected by at least one letter to another word



## [0.2.1] - 2023-09-13

### Added

- Function to verify if the user has the tiles and can create the word
- Surrender option added

### Fixed

- Now main shows tiles 'LL','CH','RR' as 1 tile

## [0.2.0] - 2023-09-12

### Added

- Main interface
- Function to shuffle player's tiles


## [0.1.2] - 2023-09-11

### Added

- RAE API to verify if a word exists in the 'Real Academia Española' dictionary


## [0.1.1] - 2023-09-07

### Added

- Now the board has colors
- Function to verify if a word fits in the board

## [0.1.0] - 2023-09-06

### Added

- Function to put words in the board
- Tools class with useful functions

### Changed

- Calculate_word_value function moved to Tools
- Rotate matrix function moved to Tools

## [0.0.9] - 2023-09-02

### Added

- Function to rotate a matrix
- Board structure and multipliers

## [0.0.8] - 2023-08-31

### Added

- Function to calculate word value

## [0.0.7] - 2023-08-30

### Added

- Turns system and function to change turns

### Changed

- Now you can exchange more than one tile at once


## [0.0.6] - 2023-08-28

### Added

- Function to exchange tiles with the bag


## [0.0.5] - 2023-08-27

### Added

- Class for Scrabble's main functions

## [0.0.4] - 2023-08-24

### Added

- Class for player
- Class for Board

## [0.0.3] - 2023-08-23

### Fixed

- Tests import functions properly
- Tests values were corrected

### Added

- Wildcards were added
- Class for board cells and its multipliers
- function to add letters to cells
- function to calculate the value of each cell

## [0.0.2] - 2023-08-17

### Fixed

- Now BagTiles contains all the tiles and their correct values

## [0.0.1] - 2023-08-16

### Added

- Class for tiles
- Class for Bag of tiles and its values
- Function to take tiles from the bag
- Function to put tiles in the bag
- This Changelog file to report changes in the project
- Tests file
- .gitignore file to especify which files should not be pushed to GitHUB
- README file 
