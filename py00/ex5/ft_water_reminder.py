def ft_water_reminder():
    water_age = int(input("Days since last watering: "))
    if water_age > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")