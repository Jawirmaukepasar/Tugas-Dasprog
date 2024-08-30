takeoff_speed = int(input("enter take off speed: "))
jarak = int(input("enter distance: "))
takeoff_speed = takeoff_speed * (1000 / 3600)

acc = (takeoff_speed ** 2) / (2 * jarak)

waktu = takeoff_speed / acc

print ("the time for the fighter to be accelerated to takeoff speed is: ", waktu)