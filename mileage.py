# Get input from user
# Convert the input to a number
# Calculate convertion of km to mi
#Print the results
#
#
#
#


user_km = input("How many kilometers did you run today? \n")
user_km_to_mi = round(float(user_km) * 0.62137, 2);

print(f"Your {user_km}km run was {user_km_to_mi}mi \n")
