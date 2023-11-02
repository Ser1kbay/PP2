from datetime import datetime
date_str1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")

date_str2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

time_difference = (date2 - date1).total_seconds()
if time_difference < 0:
    time_difference *= -1
  

print("Time difference in seconds:", time_difference)