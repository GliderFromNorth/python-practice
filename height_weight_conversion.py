#Author: Saurav Jha, Alias: GliderFromNorth  https://LinkedIn.com/in/gliderfromnorth

hola = True
while hola:
    hif = int(input("Enter height in Feet:"))
    hinch = int(input("Enter height in Inch:"))
    wik = int(input("Enter Wieght in Kilo:"))

    print("Height in Cm is:{:.2f}".format(hif*12*2.54+ hinch*2.54))

    print("Weight in KiloGram is: {:.2f}".format(wik*2.2))
    now = input ("Enter yes/y to continue or no/n to Exit:")
    if now == "yes" or now == "y":
        continue
    exit()
