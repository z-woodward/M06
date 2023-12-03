import time

with open('today.txt', 'w') as date:
    date.write(time.strftime("%B %d %Y", time.localtime()))

date = open('today.txt', 'r')
today = date.read()

print(today.split())