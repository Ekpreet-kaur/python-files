# conditional constructs

total = 500
discount = 40

#regular if else
"""
#if total >= 500:
if total > 500:
    print("flat 40% off")
else:
    print("sorry no discounts")
"""

# ladder if else
if total >= 100 and total < 200:
    print("flat 20% off")
elif total >= 200 and total < 500:
    print("flat 30% off")
elif total >= 500:
    print("flat 50% off")
else:
    print("please add valuaables of upto 100 for discount")

# nested if else
isInternetConnected = true
isGPSConnected = false

if isInternetConnected:
    print("u can browse google maps")
    if isGPSConnected:
        print("u can navigate using google maps")
    else:
        print("to use navigation using google maps enable GPS")
    else:
        print("please connect to internet and try again")