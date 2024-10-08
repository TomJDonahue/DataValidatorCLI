# Data Validator
Despite the best attempts of data analysts, most data analysis still takes place in Excel (or Excel-like tools). For small datasets, Excel is likely sufficient, but once your dataset reaches the multiple thousands (or multiple hundreds of thousands) Excel quickly staggers under the weight of the data. Simple VLOOKUP and COUNTIF functions can take several seconds to execute--and heaven forbid you filter your data with one of those formulas still live.

This tool is an attempt to take the common analysis formulas and actions performed in Excel and allow you to perform them without needing to open the document. I'm starting with a CLI but intend to provide a GUI once the core functionality is finalized.

## Commands
The tool currently supports the following commands:

   - cols
   - data
   - drop
   - exit
   - files
   - import
   - merge

| Command | Arguments | Description |
| --- | --- | --- |
| cols | 1. alias: str  | Shows all of the columns in a particular dataframe | 
| data | 1. alias: str <br> 2. num: int (optional) | Shows the data in a particular dataframe. By default, the entire dataframe is displayed. If 'num' is passed, only that number of rows is displayed. | 
| drop | 1. alias: str | Removes the table from the data model of the application |
| exit | None | Closes the application |
| files | None | Shows all of the files stored in the data model of the application |
| import | 1. alias: str <br> 2. path: str | Imports a file at the 'path' and stores it as 'alias' in the data model of the application |
| merge | 1. file1: str <br> 2. file2: str <br> 3. left_on: str <br> 4. right_on: str <br> 5. alias: str <br> 6. columns: str | Similar to an excel VLOOKUP or pandas merge. The merge is always a left join, pulling columns from the right file (file2) into the left file (file1) based on an ID column that exists in both tables. It saves the resulting data in a new table under 'alias' in the data model. If no additional 'columns' are passed into the arguments, the operation will merge all columns from 'file2'. 'columns' should be passed with commas) separating each new entry. |