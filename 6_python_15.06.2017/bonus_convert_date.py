from datetime import datetime, timedelta

date_to_convert = input("Please enter date in next format YYYY MM DD:)")

date_converted = datetime.strptime(date_to_convert, "%Y %m %d")
print("Converted date is:", date_converted.date())

date_back_converted = date_converted.strftime("%m/%d/%y")
print("Back converted date is:", date_back_converted)
