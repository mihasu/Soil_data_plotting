import re

def convert_scientific_to_standard(value):
    """Convert scientific notation to standard float representation."""
    try:
        return float(value)
    except ValueError:
        return value

def process_terminal_output(terminal_output):
    # Regex to match the date and time from the path
    time_pattern = re.compile(r'/(\d{4})/(\d{2})/(\d{2})/(\d{2})/')
    
    # Initialize variables
    time = ""
    results = []
    
    for line in terminal_output.splitlines():
        if time_pattern.match(line):
            # Extract and format the timestamp
            match = time_pattern.match(line)
            year, month, day, hour = match.groups()
            time = f"{year}-{month}-{day} {hour}:00:00+00"
        
        elif line.startswith("X"):
            # Extract the field name and value, then convert the value
            parts = line.split()
            field = parts[0]
            value = convert_scientific_to_standard(parts[1])
            results.append((time, field, value))
    
    # Organize the results by timestamp
    organized_results = {}
    
    for time, field, value in results:
        if time not in organized_results:
            organized_results[time] = {}
        organized_results[time][field] = value
    
    # Create the output table
    fields = sorted(set(field for time in organized_results for field in organized_results[time].keys()))
    output_lines = []
    
    # Header
    output_lines.append("TIME," + "," + ",".join(fields))
    
    # Data rows
    for time in sorted(organized_results.keys()):
        row = [time] + [f"{organized_results[time].get(field, ''):.3f}" for field in fields]
        output_lines.append(",".join(row))
    
    return "\n".join(output_lines)

def process_file(input_filename, output_filename):
    # Read the content from the input file
    with open(input_filename, 'r') as file:
        terminal_output = file.read()
    
    # Process the terminal output
    reformatted_output = process_terminal_output(terminal_output)
    
    # Write the reformatted output to the output file
    with open(output_filename, 'w') as file:
        file.write(reformatted_output)

# Example usage
input_filename = 'input.txt'  # Replace with your actual input file name
output_filename = 'output.txt'  # Replace with your desired output file name

# Process the file
process_file(input_filename, output_filename)

print(f"Reformatted output written to {output_filename}")

