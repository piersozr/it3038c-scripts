import datetime
bday = input("Please enter your birthday")
birthday = datetime.datetime.strptime (bday, '%m %d %Y')
tday = datetime.datetime.today()
timedelta = (tday - birthday) .total_seconds()
print("You have been alive for", timedelta, "seconds")


