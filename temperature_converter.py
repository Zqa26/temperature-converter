# temperarure_converter.py 
# a program to convert temperatures between celsius and fahrenheit

def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        celsius = float(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit")
    elif choice == "2":
        fahrenheit = float(input("What is the Fahrenheit temperature? "))
        celsius = (fahrenheit - 32) * 5/9
        print("The temperature is", celsius, "degrees Celsius")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return


# Print warnings for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("It's really cold out there. Dress warmly!")

main()
