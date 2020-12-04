hours = int(input("Enter the number of hours: "))

# compute days and hours
days = hours//24
remaining_hours = hours%24

# output results
print(str(hours) + " hours = " + str(days) + " days and " + str(remaining_hours)+" hours.")