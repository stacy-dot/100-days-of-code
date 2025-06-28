history = []

# Length conversions
def km_to_miles(km):
    result = km * 0.621371
    history.append(f"{km} km = {result:.2f} miles")
    return result

def miles_to_km(miles):
    result = miles / 0.621371
    history.append(f"{miles} miles = {result:.2f} km")
    return result

# Temperature conversions
def c_to_f(c):
    result = (c * 9/5) + 32
    history.append(f"{c}°C = {result:.2f}°F")
    return result

def f_to_c(f):
    result = (f - 32) * 5/9
    history.append(f"{f}°F = {result:.2f}°C")
    return result

# Weight conversions
def kg_to_lbs(kg):
    result = kg * 2.20462
    history.append(f"{kg} kg = {result:.2f} lbs")
    return result

def lbs_to_kg(lbs):
    result = lbs / 2.20462
    history.append(f"{lbs} lbs = {result:.2f} kg")
    return result

# Show conversion history
def show_history():
    print("\n--- Conversion History ---")
    if history:
        for entry in history:
            print(entry)
    else:
        print("No history yet.")

# Main app loop
while True:
    print("\n Unit Converter")
    print("1. km to miles")
    print("2. miles to km")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. kg to lbs")
    print("6. lbs to kg")
    print("7. View History")
    print("8. Exit")

    choice = input("Choose an option (1–8): ")

    if choice == "1":
        value = float(input("Enter kilometers: "))
        print("Result:", km_to_miles(value))

    elif choice == "2":
        value = float(input("Enter miles: "))
        print("Result:", miles_to_km(value))

    elif choice == "3":
        value = float(input("Enter Celsius: "))
        print("Result:", c_to_f(value))

    elif choice == "4":
        value = float(input("Enter Fahrenheit: "))
        print("Result:", f_to_c(value))

    elif choice == "5":
        value = float(input("Enter kilograms: "))
        print("Result:", kg_to_lbs(value))

    elif choice == "6":
        value = float(input("Enter pounds: "))
        print("Result:", lbs_to_kg(value))

    elif choice == "7":
        show_history()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
