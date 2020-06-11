#Author @GliderFromNorth Alias : Saurav jha
#LinkedIn.com/in/gliderfromnorth
import math

n=1
total =0
tax=0
hola = True
while hola:
    value = input("Enter the product value {}: ".format(n))
    n+=1
    if value != "done":
        total += float(value)
        continue
    else:
        tax += float(input("Enter the % of TAX:"))
        hola = False

final= total+(total*tax/100)
print("Final Amount:{}".format(final))
