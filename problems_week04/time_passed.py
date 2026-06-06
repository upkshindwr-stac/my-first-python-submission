from datetime import datetime
import time

number_of_repeats = int(input("Enter how many times you want the message to repeat: "))
time_interval = int(input("Enter the number of seconds for the interval: "))

for repeat in range(number_of_repeats):
    time.sleep(time_interval)
    current_second = int(datetime.now().strftime("%S"))
    print(f"{time_interval} seconds has passed")