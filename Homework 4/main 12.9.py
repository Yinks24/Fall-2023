# Solomon Falode 2154980
# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '−1':
    try:
        # Attempt to convert the age to an integer
        age = int(parts[1]) + 1
    except ValueError:
        # If the conversion fails (input is not an integer), set age to 0
        age = 0
    print(f'{name} {age}')
    
    # Get next line
    parts = input().split()
    name = parts[0]