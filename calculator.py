import ADDIEREN
import dividieren
import subtrahieren

print("***** ***  Ivo")

a = float(input("Write your number here :) :"))
b = float(input("Write your second number now :) : "))
c = str(input("Write the symbol of the desired operation :D : "))

print("Your result is:")
match c:
    case "+":
        print(ADDIEREN.addieren(a, b))
    case "-":
        print(subtrahieren.subtrahieren(a, b))
    case "/":
        print(dividieren.dividieren(a, b))
    case other:
        print("Not a valid thing fucko")

