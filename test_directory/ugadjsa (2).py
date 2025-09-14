import os
import sys
import string
from typing import Any


# gets the root drives on the system
def get_root_drives():
    # print(os.listdrives())
    return os.listdrives()


# returns a list of files to read, this is not at all efficient to do
def iterate_through_directory(root_directory='C:\\') -> list[Any] | list[str]:
    files = []

    for root, subdirectories, files in os.walk(root_directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            print(filepath)


    # print(found_exe)
    return files


def return_files_list_in_directory(root_directory='C:\\', file_extention=[]):
    found_file = []

    for root, subdirectories, files in os.walk(root_directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            #make sure we are parsing for a file, and then check if we have that file
            if not file_extention:
                    found_file.append(filepath)
            else:
                for ext in file_extention:
                    if filepath.lower().endswith(ext):
                        found_file.append(filepath)


    # print(found_exe)
    return found_file

# might want to be careful about this
def iterate_through_directory_ext(root_directory='C:\\', file_extention='.exe'):
    found_exe = []

    for root, subdirectories, files in os.walk(root_directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if filepath.lower().endswith(file_extention):
                found_exe.append(filepath)


    # print(found_exe)
    return found_exe


# returns a dict of the emulator name to the emulator file location
def iterate_through_all_directories():
    root_drives = get_root_drives()

    extension_to_parse = []

    for root_directory in root_drives:
        # not using append because it gives us list[list[str]], which is not what we want, we want list[str]
        # extend adds elements to the end of the array
        extension_to_parse.extend(iterate_through_directory_ext(root_directory, '.exe'))

    # print(extension_to_parse)
    # return extension_to_parse
    # parse exe for what im looking for, and then move to its own function when done

    found_emulators = {}
    # hash to store emulator to filepath
    #

    for filepath in extension_to_parse:
        head, tail = os.path.split(filepath)
        # print(head)
        # print(tail)
        # find if emulator is within the list

        # removes .exe from the file name
        tail_without_extension = os.path.splitext(tail)[0]

        # check if the emulator name is within the filename
        '''
        for emulator_name_from_list in emulators_exe_name_list:
            if emulator_name_from_list in tail_without_extension:
                print(f"Found: {tail_without_extension}")
                print(f"Found: {emulator_name_from_list}")
                found_emulators[emulator_name_from_list] = filepath
        '''



# iterate_through_all_directories()
