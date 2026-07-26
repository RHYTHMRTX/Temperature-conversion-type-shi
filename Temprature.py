# Temperature Converter
print(" The temperature has been calculated in majorly 2 units: one is celsius and the other one whatever that is..")
print("---------------Temperature(Not the pitbull one) converter-----------------")
print("")
unit = input("enter the unit u wanna convert to(C/F):  ")
if unit == "C":
    pass
elif unit == "F":
    pass
else:
    print(f"I said C or F you genius what is {unit} ? go use C/F only.")

temp = float(input("enter the temperature u wanna convert:  "))
if temp < -273.15:
    print("Where the hell are you? neptune???")
    exit()
elif temp > 1000:
    print("Either u trippin or u in the sun or something..")
    exit()

# this is the conversion part of the code
if unit == "C":
    temp = round((9 * temp)* 5 + 32, 1)
    print(f"the temperature in fahrenheit is: {temp} F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"the temperature in celsius is: {temp} C")

print("---------------Temperature(Not the pitbull one)-----------------") 
print("")
print(f"This is the temp u wanted cheeky boi/gurl: {temp} ")
# Thats it for the code now go and use it for your own good or evil purposes.