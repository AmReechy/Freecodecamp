def add_time(start, dur, day= None):
    #add_time("3:00 PM", "3:10") - # Returns: 6:10 PM
    #add_time("11:30 AM", "2:32", "Monday") - # Returns: 2:02 PM, Monday
    #add_time("11:43 AM", "00:20") - # Returns: 12:03 PM
    #add_time("11:43 PM", "24:20", "tueSday") - # Returns: 12:03 AM, Thursday (2 days later)

    
    days = ["Sunday", "Monday", "Tuesday", "Wednessday", 
            "Thursday", "Friday", "Saturday"]
    
    am_pm = start[-2:]
    start_hr, start_min = [int(num) for num in start[:-2].split(':')]
    dur_hr, dur_min = [int(num) for num in dur.split(':')]
    hr_min, end_min = divmod(start_min + dur_min, 60) 
    end_hr = start_hr + dur_hr + hr_min + (0 if am_pm == 'AM' else 12)

    days_after, day_24hr = divmod(end_hr, 24)
    end_am_pm, end_12hr = ('AM', day_24hr%12) if day_24hr < 12 else ('PM', day_24hr%12)
    
    if end_12hr == 0:
        end_12hr = 12
    new_time = f"{end_12hr}:{str(end_min).zfill(2)} {end_am_pm}"
    if day:
        new_day = days[(days.index(day.capitalize()) + days_after) % 6]
    if days_after == 0:
        if day:
            return f"{new_time}, {new_day}"
        else:
            return f"{new_time}"
    elif days_after == 1:
        if day:
            return f"{new_time}, {new_day} (next day)"
        else:
            return f"{new_time} (next day)"
    elif days_after > 1:
        if day:
            return f"{new_time}, {new_day} ({days_after} days later)"
        else:
            return f"{new_time} ({days_after} days later)"