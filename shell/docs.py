MERGE_LEFT = '''
Operation: Pulls column data from the right table into the left table against a single ID column.
Command: merge
Arguments:
    File 1: The left file that will be merged upon.
    File 2: The right file that data will be pulled from.
    Left ID: The ID from File 1.
    Right ID: The ID from File 2.
    Output File: The resulting output file. This file will be accessible to the CLI using this alias.
    Columns (Optional): The columns from File 2 that will be pulled into File 1. 
        If left blank, all columns from File 2 will be pulled into File 1'''