import time
timestamp = (time.strftime('%H'))
current_time =int(timestamp)
if current_time < 12:
    print("Good morning")
elif current_time>12 and current_time<17:
    print("Good Afternoon")
elif current_time>17:
    print("Good Night")