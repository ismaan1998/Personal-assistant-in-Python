
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H hours %M minutes")
print("Current Time =", current_time)