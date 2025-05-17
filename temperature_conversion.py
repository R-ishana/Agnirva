#Define a function that convert temprature from fahrenheit to celsius and vice-versa
def fahrenheit_celsius(F):
    return ((F-32)*5/9)
#Converts input in fahrenheit to celsius and returns the value
def celsius_fahrenheit(C):
    return ((C*9/5)+32)
#Converts input in celsiun to fahrenheit and returns the value
a=input("Please press: \n'F' if you wish to convert from Farenheit to Celsius\n'C' if you wish to convert from Celsius to Fahrenheit: ")
#To check which type of conversion user wishes to make before getting value
if a=="C" or a=='c':
    C=int(input("Enter your temprature in celsius: "))
    print("Your given temprature in Fahrenheit is: ",celsius_fahrenheit(C))
#To fahrenheit conversion
elif a=='F' or a=="f":
    F=int(input("Enter your temprature in Fahrenheit: "))
    print("Your given temprature in Celsius is: ",fahrenheit_celsius(F))
#To celsius conversion
else:
    print("Invalid input, please enter either F or C")
#If user inputs anything else
print ("Thank You")
