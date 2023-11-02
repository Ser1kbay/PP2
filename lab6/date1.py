import datetime
current_date = datetime.date.today()

new_date = current_date + datetime.timedelta(days=5)

print(current_date)
print(new_date)