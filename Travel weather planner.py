distance_mi = float(input("Enter the distance in miles: "))
is_raining = bool(input("Is it raining? (True/False): "))
has_bike = bool(input("Do you have a bike? (True/False): "))
has_car = bool(input("Do you have a car? (True/False): "))
has_ride_share_app = bool(input("Do you have a ride-share app? (True/False): "))
if distance_mi == 0 :
    print("You are already at your destination silly :).")
elif distance_mi <= 1:
    if is_raining == True :
        print("Seems like it's raining, you should probably delay your trip until it stops pouring.")
    else :
        print("You can walk :).")
elif distance_mi <= 6:
    if has_bike == True and is_raining == False :
        print("You can ride your bike :)")
    else :
        print("You should book a ride-share or stay until it's not raining.")
elif distance_mi > 6 :
    if has_car == True or has_ride_share_app == True :
        print("You can drive your car or take a ride-share. :)")
    else :
        print("You should probably stay home or find another way to get there.")