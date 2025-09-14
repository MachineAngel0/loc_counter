# Lines of Code Counter
- - - 
 A simple lines of code command line script

I made this because I couldn't find a jetbrains plugin that would tell me the loc of my project, so I made one myself

### How To Use:
- The structure of the command line looks like such: py loc.py -p - e
- -p is the file path or directory; -e is a list of extensions you wish to count, can be left empty to scan all files
- If you are passing in a file, you do not need to specify any params for e
- All info above can be using the help command: py LOC.py -h

### Notes: 
- if you pass in a directory, it will scan the entire directory
- Comments and empty lines will contribute to the final count


### Examples:
- py loc_reader.py -p loc_reader.py
  -  Will count the file. Again, not that you do not need to pass any values in for -e
- py loc.py -p test_directory -e .c 
  -  Will scan the entire directory for all .c files 
- py loc.py -p test_directory -e .c .py
  -  Will scan the entire directory for all .c and .py files 
- py loc.py -p test_directory
  -  Will scan the entire directory for all openable files. Notice that no values were used for -e 



