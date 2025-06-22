# pythone tempacher 

unit = input("Is this temperture in celsius or faheranhait (C/F)  ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32,  1) 
    print(f"The temperture in faherenheit is : {temp}°F")
elif unit == "F":
    temp = round(( temp - 32) * 5 / 9,  1) 
    print(f"The temperture in celsius is : {temp}°C")
else:
    print(f"{unit} is an invalid unit or measurement")



    
