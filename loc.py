import argparse
import os

from DirectoryIterator import return_files_list_in_directory
from lines_of_code_counter import read_lines_of_code_in_file

# test_directory
#py locloc.py -p test_directory
# test file
#py locloc.py -p loc.py


#NOTE: A LINES OF CODE READER,
#py locloc.py - for help
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prints lines of code for a file or directory, for a specific file type"
    )

    parser.add_argument(
        "-p", "--path", metavar="file path/directory",
        required=True, help="Specify the file or directory you wish to find the lines of code from"
    )

    # TODO: add in the ability to parse by file extension
    parser.add_argument(
        "-e", "--ext", nargs='*', metavar="extension type",
        help="specific file extension we are looking for, defaults to all openable files if not specified",
        default= ""
    )

    args = parser.parse_args()

    #check if its a file or directory
    if os.path.isfile(args.path):
        print(f"TOTAL COUNT {read_lines_of_code_in_file(args.path)}")
    elif os.path.isdir(args.path):
        files_list = return_files_list_in_directory(args.path, args.ext)
        total_count = 0
        for file in files_list:
            total_count += read_lines_of_code_in_file(file)
        print(f"TOTAL COUNT: {total_count}")

    else:
        print("passed in path is neither file nor directory")

    #msg = f"hello, {args.path}, {args.ext}"

    # read_lines_of_code_in_file()


