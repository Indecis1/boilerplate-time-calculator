import re

def add_time(start, duration, *args):
  day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  period_of_the_day = ["AM", "PM"]
  #    here we have for example ("3","00","PM") for start_time
  start_time = re.split(r':([0-9]{2})', start)
  start_time[2] = start_time[2].strip()
  duration_time = tuple(re.split(r':([0-9]{2})', duration))
  total_minute = int(start_time[1]) + int(duration_time[1])
  minute = total_minute % 60
  total_hour = int(start_time[0]) + int(duration_time[0]) + (total_minute // 60)
  hour = total_hour % 12
  #    We determine the new period of the day (in number)
  number_of_period = total_hour // 12
  period = (period_of_the_day.index(start_time[2]) + number_of_period) % 2
  #    if hour == 0 it means we are on limits 12:00 AM or 12:00 PM
  if hour == 0:
    hour = 12
  if minute < 10:
      new_time = "" + str(hour) + ":" + "0" + str(minute) + " " + period_of_the_day[period]
  else:
      new_time = "" + str(hour) + ":" + str(minute) + " " + period_of_the_day[period]
  #    if we get the day
  if args:
    if (start_time[2] == "AM" and number_of_period < 2) or (start_time[2] == "PM" and number_of_period < 1):
      new_time += ", " + args[0].lower().capitalize()
    elif (start_time[2] == "AM" and 2 <= number_of_period <= 3) or (start_time[2] == "PM" and 1 <= number_of_period <= 2):
      new_time += ", "+ day[(day.index(args[0].lower().capitalize()) + 1) % 7] + " (next day)"
    elif (start_time[2] == "AM" and number_of_period >= 4) or (start_time[2] == "PM" and number_of_period >= 3): 
      new_time += ", " + day[(day.index(args[0].lower().capitalize()) + number_of_period // 2 + 1) % 7] + " ({} days later)".format((number_of_period + period_of_the_day.index(start_time[2])) // 2) # We use this expression to get the number of days later
  else:
    if (start_time[2] == "AM" and number_of_period == 2) or(start_time[2] == "PM" and 1 <= number_of_period <= 2):
      new_time += " (next day)"
    elif (start_time[2] == "AM" and number_of_period >= 4) or (start_time[2] == "PM" and number_of_period >= 3):
      new_time += " ({} days later)".format((number_of_period + period_of_the_day.index(start_time[2])) // 2)

  return new_time
