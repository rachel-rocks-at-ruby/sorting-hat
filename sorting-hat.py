print "Please enter some information \n
so that you can be sorted into your Hogwarts House."

name = (raw_input("Please enter your first name.  "))
birthday = (raw_input("Please enter your birth month (ex. January).  "))
birth_place = (raw_input("Please enter the city where you were born.  "))
lhp = int(raw_input("Please enter how much you enjoyed the Harry Potter series \non a scale between 1 and 10 (10 being LOVED it!).  "))

import random

house = random.randrange(0, 4)

if house == 1:
	print "You belong to the house of of Helga Hufflepuff."
elif house == 2:
	print "You belong to the house of Rowena Ravenclaw."
elif house == 3:
	print "You belong to the house of Godric Gryffindor."
else:
	print "You belong to the hous eof Salazar Slytherin."
