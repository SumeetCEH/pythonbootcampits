from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Example usage
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

birthdate = date(birth_year, birth_month, birth_day)
age = calculate_age(birthdate)

print(f"You are {age} years old.")
