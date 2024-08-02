def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = []
    for line in lines:
        # Remove spaces after #
        line = line.replace('# ', '#')
        # Skip empty lines
        if line.strip():
            processed_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)

# Specify the input and output file paths
input_file = 'en.txt'
output_file = 'en_processed.txt'

# Process the file
process_file(input_file, output_file)
