# This is my project for the openspace-organizer challenge from BeCode.

## Description:

This is a program made to take a list of People in a `.csv` file, and to distribute them randomly in an assortment of programmable number of `Tables` with a programmable number of `Seats` each. This is fully configurable in the `config.json` inside the `utils` folder.

## Installation

Download code by clicking [Code] - [Download Zip] or downloading the latest release.

Program requires python installed.

Open cmd in folder or navigate to it using `cd`.

Execute program with `python main.py`

Program is configurable by editting values in `/utils/config.json`: you can edit `number_of_tables`, `table_capacity` and `file_path`.

## Usage

After running program, it will simply use the information provided in `config.json`. It starts off by grabbing names from `file_path`, organizing them, and then it will output the results in the console, in a manner showing the Table numbers and the people sitting at said tables. Afterwards, it also prints the number of total seats, number of taken seats, number of either leftover seats, in case of there being more seats than people, or missing seats, if there are more people than there are seats. If so, it will also post the names of people it couldn't assign a seat to. This then saves all the table-sitting information in a `.xlsx` file.
