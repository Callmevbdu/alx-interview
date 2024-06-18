#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Define the signal handler
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Function to print statistics
def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))

# Bind the CTRL+C signal to the handler
signal.signal(signal.SIGINT, signal_handler)

# Regex pattern for valid lines
pattern = re.compile(r'\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')

# Read from stdin line by line
try:
    for line in sys.stdin:
        # Check if line matches the pattern
        match = pattern.search(line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            # Update total size and status code count
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

        # Increment line count and check if it's time to print stats
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle any keyboard interruption
    print_stats()
    sys.exit(0)

# Print final stats when EOF is reached
print_stats()
