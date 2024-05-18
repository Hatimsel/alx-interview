#!/usr/bin/python3
"""Log parsing"""
import re
import signal
import signal
import sys


pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "GET /projects/260 HTTP/1\.1" \d{3} \d+$')

status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}

total_size = 0
line_count = 0


def print_statistics():
    """Prints the file size and status code counts"""
    print("File size: {}".format(total_size))
    # sorted_dict = dict(sorted(status_code.items(),
                              # key=lambda item: item[1],
                              # reverse=True))

    # for st_code, count in sorted_dict.items():
    #     if count > 0:
    #         print("{}: {}".format(st_code, count))

    for st_code in sorted(status_code.keys()):
        if status_code[st_code] > 0:
            print("{}: {}".format(st_code, status_code[st_code]))

def sigint_handler(signum, frame):
    """Handles the SIGINT signal (CTRL + C)"""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)


try:
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break

        if pattern.fullmatch(line):
            parts = line.split()
            file_size = int(parts[-1])
            code = parts[-2]

            total_size += file_size
            if code in status_code:
                status_code[code] += 1
            line_count += 1

        if line_count == 10:
            print_statistics()
            line_count = 0

except Exception as e:
    print(e)
finally:
    print_statistics()
