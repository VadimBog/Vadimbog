# Get the user's weight as a float
weight = float(input("Enter your weight: "))

# Get the user's weight option (case-insensitive) and convert to lowercase
weight_option = input("(K)g or (L)bs: ").lower()

# Check the weight option and perform the appropriate conversion
if weight_option == "k":
    # Convert kilograms to pounds
    converted_weight_lbs = round(weight * 2.20462, 2)
    # Display the result
    print(f"Your weight is {weight} Kg or {converted_weight_lbs} Lbs")
elif weight_option == "l":
    # Convert pounds to kilograms
    converted_weight_kg = round(weight * 0.453592, 2)
    # Display the result
    print(f"Your weight is {converted_weight_kg} Kg or {weight} Lbs")
else:
    # Display an error message for an invalid weight option
    print("Invalid weight option")
