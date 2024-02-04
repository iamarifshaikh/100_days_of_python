unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temperature = float(input("Enter the temperature: "))

if unit == "C":
    temperature = round((9 * temperature) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temperature}°F")
elif unit == "F":
    temperature = round((temperature - 32) * 5 / 9,1)
    print(f"The temperature in Celsius is: {temperature}°C")
else:
    print(f"{temperature} is an invalid unit of measurement")