def add_time(start, duration, day_mention = None):

  day = ""
  end = ""
  day_count = 0
  end_min = ""
  end_h = ""
  x = 0
  sun = ""
  when = ""

  days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
  days_return = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

  if day_mention :
    x = days.index(day_mention.lower())
  
  start_hour = start.split(":")[0]
  start_minute = (start.split(":")[1]).split(" ")[0]
  start_sun = (start.split(":")[1]).split(" ")[1]


  duration_hour = duration.split(":")[0]
  duration_minute = duration.split(":")[1]

  end_hour = int(start_hour)+int(duration_hour)
  end_minute = int(start_minute)+int(duration_minute)
  
  if start_sun == "PM" :
    end_hour += 12
  
  while end_minute > 60:
    end_minute -= 60
    end_hour += 1


  while end_hour >= 24 :
    end_hour -= 24
    day_count += 1

  if end_hour >= 12 :
    end_hour -= 12
    sun = "PM"
  else:
    sun = "AM"

  if end_hour==0 and sun =="AM":
    end_hour = 12
  elif end_hour==0 and sun =="PM":
    end_hour = 12

  # change to str for output
  if end_minute < 10 : 
    end_min = "0" + str(end_minute)
  else :
    end_min = str(end_minute)
  end_h = str(end_hour)

  # showing the day
  if (day_mention != None):
    day_index = x + day_count 
    while (day_index > 6):
      day_index -= 7
    day = ", " + days_return[day_index]
  
  if day_count == 0:
    when = ""
  elif day_count == 1:
    when = " (next day)"
  else :
    when = " (" + str(day_count) + " days later)"

  
  end = end_h + ":" + end_min + " " + sun 
  return end + day + when

print(add_time("11:40 PM", "0:25","monday"))
