def get_daily_temps():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    temps = {}
    for day in days_of_week:
        temp = float(input(f"Enter the average temperature for {day}: "))
        temps[day] = temp
    return temps

weekly_temps = get_daily_temps()
print(weekly_temps)

