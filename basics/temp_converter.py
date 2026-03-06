def convert_temperature():
    print("--- Temperature Converter ---")
    scale = input("Convert from (C)elcius or (F)ahrenheit? ").upper()
    
    try:
        temp = float(input("Enter the temperature: "))
        
        if scale == 'C':
            result = (temp * 9/5) + 32
            print(f"{temp}°C is {result:.2f}°F")
        elif scale == 'F':
            result = (temp - 32) * 5/9
            print(f"{temp}°F is {result:.2f}°C")
        else:
            print("Invalid scale selected.")
    except ValueError:
        print("Please enter a valid number.")


if __name__=="__main__":
    convert_temperature()