month = input("Enter the month number: ")
month = int(month)
months_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# Check if the input month name exists in the dictionary
if month in months_dict:
    # Print the corresponding numerical value
    print(f"The month is {months_dict[month]}")
else:
    print("Invalid month name entered.")