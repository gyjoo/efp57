is_key_returned = input("Is the key returned? (y/n) ")

if is_key_returned == "y":
	is_battery_corroded = input("Are the battery terminals corroded? (y/n) ")
	if is_battery_corroded == "y": print("Clean terminals and try starting again.")
	elif is_battery_corroded == "n": print("Replace cables and try again.")
elif is_key_returned == "n":
	car_make_clicking_noise = input("Does the car make a clicking noise? (y/n) ")
	if car_make_clicking_noise =="y": print("Replace the battery.")
	elif car_make_clicking_noise == "n":
		car_crank_up_fail_to_start = input("Does the car crank up but fail to start? (y/n) ")
		if car_crank_up_fail_to_start == "y": print("Check spark plug connections.")
		elif car_crank_up_fail_to_start == "n":
			engine_start_then_die = input("Does the engine start and then die? (y/n) ")
			if engine_start_then_die == "y" : 
				car_have_fuel_injection = input("Does your car have fuel injection? (y/n) ")
				if car_have_fuel_injection == "y": print("Get it in for service.")
				elif car_have_fuel_injection == "n": print("Check to ensure the choke is opening and closing.")

