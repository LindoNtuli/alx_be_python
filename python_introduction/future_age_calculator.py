# A Python script that asks the user for their current age and then calculates how old they will be in a specific future year.
age_request = int(input("How old are you?"))
current_year = 2023
future_year = 2050                  
user_age = future_year - current_year + age_request
print("In 2050, you will be", user_age, "years old.")
                  
