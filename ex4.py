car= int(input('give the no of car'))
space_in_car=int(input('capacity of car is'))
drivers=int(input('NO.of drivers'))
passengers=int(input('NO.of passengers' ))
reddy_to_move_cars=drivers
not_reddy=car - drivers
reddy_car_capacity=space_in_car * reddy_to_move_cars




print("there are", car, "cars are available")
print("in each car there are", space_in_car, "can accomadate")
print("the are only", drivers, "drivers available ")
print("reddy to move cars are",reddy_to_move_cars)
print("but the no.of people can travel is only",reddy_car_capacity)
