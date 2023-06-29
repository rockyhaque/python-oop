import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

hour = int(input('Enter Hour: '))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning!")
elif(hour>=12 and hour<17):
    print("Good Afternoon!")
elif(hour>=17 and hour<24):
    print("Good Night!")