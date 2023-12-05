# Solomon Falode 2154980
while True:
    try:
        # Read input
        parts = input().split()
        name = parts[0]

        # Check for the exit condition
        if name == '-1':
            break

        # Process age and print output
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))

    except ValueError:
        # Handle the case where the age is not an integer
        print("Invalid input format. Please provide a name followed by an integer age.")
