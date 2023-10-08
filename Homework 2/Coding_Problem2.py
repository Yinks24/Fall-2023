# Solomon falode PSID:2154980
import re

def parse_date(input_date):
    match = re.match(r'(\w+)\s+(\d+),\s+(\d{4})', input_date)
    if match:
        month, day, year = match.groups()
        return '{month_dict[month.lower()]}/{day}/{year}'
    else:
        return None

month_dict = {
    'january': '1',
    'february': '2',
    'march': '3',
    'april': '4',
    'may': '5',
    'june': '6',
    'july': '7',
    'august': '8',
    'september': '9',
    'october': '10',
    'november': '11',
    'december': '12'
}

input_file_name = 'input1.csv'
dates = []

with open(input_file_name, 'r') as input_file:
    for line in input_file:
        date_input = line.strip()
        if date_input == '-1':
            break
        parsed_date = parse_date(date_input)
        if parsed_date:
            dates.append(parsed_date)

output_file_name = 'parsedDates.txt'
with open(output_file_name, 'w') as output_file:
    for date in dates:
        output_file.write(date + '\n')

print("Dates have been parsed and saved to 'parsedDates.txt'.")

