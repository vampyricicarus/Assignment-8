# task 1

def tempConvert():
    try:
        f = int(input("What is the temperature in Fahrenheit? "))
        convert = (f - 32) * 5 / 9
        
    except ValueError:
        print("Numeric values only please")
    else:
        print("The temperature in Celsius is " + str(convert))
    finally:
        print("Thank you for using our service!")
    return

tempConvert()