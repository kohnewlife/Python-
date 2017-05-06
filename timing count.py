hours = int(input("Please enter the hours:"))
minutes = int(input("Please enter the minutes:"))
seconds = int(input("Please enter the seconds:"))

print("You entered", hours, "hours", minutes, "minutes and", seconds, "seconds")
12

total_seconds = 3600*hours + 60*minutes + seconds
print("The total number of seconds:", total_seconds)
