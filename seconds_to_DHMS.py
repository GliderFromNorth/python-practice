"""
Created on Sun Jun 14 23:54:23 2020

@author: saurav jha #linkedin.com/in/gliderfromnorth

"""
#input seconds 
seconds = int(input("Enter the time in seconds: "))

day = seconds // 86400
hours= (seconds - day*86400)//3600

minutes = (seconds - hours*3600 -day*86400)//60

remaining_seconds = seconds - hours*3600 -day*86400 - minutes*60
#output in DHMS format.
print("{} Days {} Hours {} minutes {} seconds" .format(day,hours,minutes,remaining_seconds))