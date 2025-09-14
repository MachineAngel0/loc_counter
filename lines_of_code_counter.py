import os


#Note this does not parse out comments
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


