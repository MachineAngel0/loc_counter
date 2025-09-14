import argparse
import os

from DirectoryIterator import return_files_list_in_directory


def read_lines_of_code_in_file(filepath: str) -> int:
    line_count = 0

    if not os.path.isfile(filepath):
        print('INVALID FILE')
        return 0


    opened_file = open(filepath, 'r', errors='ignore')

    if not opened_file:
        print('File not found')
        opened_file.close()
        return 0

    for line in opened_file.read():
        if line == '\n':
            line_count += 1

    opened_file.close()

    # debug
    #print(f"LINE COUNT: {line_count}")

    # we add a plus one since it doesn't read the last line
    return line_count + 1

# testing on itself
# read_lines_of_code_in_file("LOC.py")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prints lines of code for a file or directory, for a specific file type"
    )

    parser.add_argument(
        "-p", "--path", metavar="file path/directory",
        required=True, help="Specify the file or directory you wish to find the lines of code from"
    )

    # TODO: add in the ability to parse by file extension
    ''' 
    parser.add_argument(
        "-e", "--ext", metavar="extension type",
        required=False, help="specific file extension we are looking for, defaults to all openable files if not specified",
        default= ""
    )
    '''

    args = parser.parse_args()

    #check if its a file or directory
    if os.path.isfile(args.path):
        print(f"TOTAL COUNT {read_lines_of_code_in_file(args.path)}")
    elif os.path.isdir(args.path):
        files_list = return_files_list_in_directory(args.path, )
        total_count = 0
        for file in files_list:
            total_count += read_lines_of_code_in_file(file)
        print(f"TOTAL COUNT: {total_count}")

    else:
        print("passed in path is neither file nor directory")

    #msg = f"hello, {args.path}, {args.ext}"

    # read_lines_of_code_in_file()


