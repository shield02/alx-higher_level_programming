#!/usr/bin/python3
"""Log parsing module"""


def generate_stats(file_size, status_codes):
    """Print statistics
    Args:
        file_size (int): sum of all previous file sizes
        status_codes (dict): status codes from input
    """
    print(f"File size: {file_size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")

if __name__ == "__main__":
    import sys

    file_size = 0
    status_codes = {}
    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                generate_stats(file_size, status_codes)
                count = 1
            else:
                count += 1

            try:
                file_size += int(line.split()[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in possible_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        generate_stats(file_size, status_codes)

    except KeyboardInterrupt:
        generate_stats(file_size, status_codes)
        raise
