x = int(input('Type here: '))

number_of_day_seconds = 24*60*60
number_of_hour_seconds = 3600
number_of_minute_seconds = 60

if 0 <= x <= 8640000:
    days = x // number_of_day_seconds
    after_days = x % number_of_day_seconds

    hours = after_days // number_of_hour_seconds
    after_hours = after_days % number_of_hour_seconds

    minutes = after_hours // number_of_minute_seconds
    seconds = after_hours % number_of_minute_seconds
    if days % 10 == 2 or days % 10 == 3 or days % 10 == 4 and days != 11 and days != 14:
        print(days,'дні,','',end='')
    elif days % 10 == 1 and days != 11:
        print(days,'день,','',end='')
    else:
        print(days, 'днів,','',end='')

    if hours != 0:
        print(hours,":",sep = '', end='')
    elif hours == 0:
        print(hours,'0',":",sep = '', end='')

    if minutes != 0:
        print(minutes,":",sep = '',end='')
    if minutes == 0:
        print(minutes,'0',":",sep = '',end='')
    if seconds != 0:
        print(seconds)
    if seconds == 0:
        print(seconds,'0',sep = '')
else:
    print("Error: Enter a valid number (0 to 8640000)")
#print(after_days)


#print(after_hours)

#print(days,'днів',hours,':',minutes,':',seconds)
#0 -> 0 днів, 00:00:00
#224930 -> 2 дні, 14:28:50
#466289 -> 5 днів, 09:31:29
#950400 -> 11 днів, 00:00:00
#1209600 -> 14 днів, 00:00:00
#1900800 - > 22 дні, 00:00:00
#8639999 -> 99 днів, 23:59:59
#22493 -> 0 днів, 06:14:53
#7948799 -> 91 день, 23:59:59
