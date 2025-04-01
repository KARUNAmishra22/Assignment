def add_daily_temp(temp_dict, temp, day):
    if day not in temp_dict:
        temp_dict[day] = temp
    return temp_dict

# Example usage:
temperatures = {}
updated_temperatures = add_daily_temp(temperatures, 25, 'Monday')
updated_temperatures = add_daily_temp(updated_temperatures, 30, 'Monday')  # Will not update
updated_temperatures = add_daily_temp(updated_temperatures, 28, 'Tuesday')
print(updated_temperatures)