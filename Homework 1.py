# Solomon falode PSID:2154980
print("Birthday Calculator")
print("Current day")
current_month = int(input("Month: "))
current_day = int(input("Day: "))
current_year = int(input("Year: "))
# Prompt the user to enter their birthday
print("Birthday")
birthday_month = int(input("Month: "))
birthday_day = int(input("Day: "))
birthday_year = int(input("Year: "))
# Calculate the age
if current_month < birthday_month or (current_month == birthday_month and current_day < birthday_day):
    age = current_year - birthday_year - 1
else:
    age = current_year - birthday_year
# Output the age
print("You are "+str(age)+" years old.")
# Check if it's the user's birthday
if current_month == birthday_month and current_day == birthday_day:
    print("Happy Birthday!")
