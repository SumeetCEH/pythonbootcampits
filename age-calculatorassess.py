from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

# Example usage
birth_year = 2003  # Replace this with the desired birth year
age = calculate_age(birth_year)
print(f"The age is: {age} years")
