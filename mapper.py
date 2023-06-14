def parse_log_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    parsed_lines = []
    for line in lines:
        parts = line.strip().split(' ')
        if len(parts) < 3:  # Skip lines without the expected format
            continue
        date, time = parts[0], parts[1]
        log_level = parts[2].split(':')[0]
        message = ' '.join(parts[2].split(':')[1:])
        ip_address = ''
        for part in parts[3:]:
            if part.startswith('IP:'):
                ip_address = part.split(':')[1]
                break
        parsed_lines.append([date, time, log_level, ip_address, message])

    with open(output_file, 'w') as f:
        for line in parsed_lines:
            f.write('\t'.join(line) + '\n')

    print(f"Successfully parsed log file '{input_file}' into columns and saved as '{output_file}'.")


# Example usage
input_file = 'input.txt'  # Replace with the actual path to your input file
output_file = 'output.txt'  # Replace with the desired output file path

parse_log_file(input_file, output_file)
