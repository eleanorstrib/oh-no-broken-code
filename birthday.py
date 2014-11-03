from datetime import datetime

number_endings = {
    1: 'st',
    2: 'nd',
    3: 'rd'
}

today = datetime.now()
todays_day = today.day

# get the right ending, e.g. 1 => 1st, 2 => 2nd
# but beware! 11 => 11th, 21 => 21st, 31 => 31st

# test your code by forcing todays_day to be something different
# todays_day = 22
if todays_day < 10 or todays_day > 20:
	if todays_day%10 <= abs(3):
		ending = number_endings.get(todays_day%10)
else:
	ending = 'th'


#     # x % y (mod) will give the remainder when x is divided by y
#     # -- but x needs to be an integer!
#     number = todays_day % 10
#     # look up number in number_endings
#     # and if you find it as a key, put the value in ending
#     if number in number_endings:
# # make this print ending, not 'th'
print "Today is the {}{}".format(todays_day,ending)

birthday = int(raw_input("What day of the month is your birthday?"))
if birthday < 10 or birthday > 20:
	if birthday%10 <= abs(3):
		ending = number_endings.get(birthday%10)
else:
	ending = 'th'

# make this print the birthday, and the right ending
print "Your birthday is on the {}{}!".format(birthday,ending)