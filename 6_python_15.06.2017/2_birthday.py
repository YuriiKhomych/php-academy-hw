from datetime import datetime, timedelta

now = datetime.now()
future_week = now + timedelta(weeks=1)

friend_birthday = input("Enter your friend birthday (format: YYYY-MM-DD): ")
birthday_format = "%Y-%m-%d"
date_birthday = datetime.strptime(friend_birthday, birthday_format)

print('Date: {0}'.format(date_birthday.date()))
if now < date_birthday < future_week:
    print("birthday of your friend at the current week")
else:
    print("You can`t visit event at this week")
