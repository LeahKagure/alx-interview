import sys

# Initialize variables to store metrics
total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

# Read input line by line
line_count = 0
for line in sys.stdin:
    # Check if line matches input format
    parts = line.split()
    if len(parts) != 9:
        continue

    # Extract file size and status code
    try:
        file_size = int(parts[8])
        status_code = int(parts[7])
    except ValueError:
        continue

    # Update metrics
    total_size += file_size
    if status_code in status_codes:
        status_codes[status_code] += 1

    line_count += 1
    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print("Total file size: ", total_size)
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print(f"{code}: {status_codes[code]}")

# Print final statistics on keyboard interruption
except KeyboardInterrupt:
    print("Total file size: ", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

