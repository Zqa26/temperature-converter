# pseudocode - Input the temperature in degrees Celsius (call it celsius)
# Calculate the fahrenheit as (9/5) celsius + 32
# Out put fahrenheit

# tempconverter.py 
# a program to convert celsius to fahrenheit


# INTENT
# - Input the temperature in degrees Celsius (call it celsius)
# - Calculate fahrenheit as 9/5 celsius + 32
# - Output fahrenheit > 90
# - print a heat warning
# - if fahrenheit > 30
# - print a cold warning 


def main():
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit")


# Print warnings for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("It's really cold out there. Dress warmly!")

main()