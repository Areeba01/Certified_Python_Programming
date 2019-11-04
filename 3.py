from datetime import datetime
now=datetime.now()
dt_str=now.strftime("Date: %m/ %d/%Y \nTime: %H : %M : %S")
print(dt_str)