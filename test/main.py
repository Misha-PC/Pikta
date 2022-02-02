from json_utility import *
from excel_utility import *


if __name__ == '__main__':
    file_paths = [".\\static\\test1.json",
                  ".\\static\\test2.json",          # files list
                  ".\\static\\test3.json"
                  ]

    write_ready = []
    for key in file_paths:
        parsed = parse_json(read_json_file(key))    # read & parse .json files
        write_ready.append(parsed)

    write_file(write_ready)                         # write parsed values to excle file
