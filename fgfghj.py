hour = int (       input ('введите время')         )
print (hour)
minute = int (input('введите минуты'))
print (minute)
print (f"вы проснулись в {hour}:{minute}")
new_time = hour *60+minute
if 420<new_time<540:
    print ('вы успиваете')