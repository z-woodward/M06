#ZacharyW - 13.3 Parse the date from today_string.

today = open("today.txt",'r')
today_str = today.readlines()
print(today_str)

date = (today_str[0])
today = date.split('-')

def printdate():
    print("Month: ", today[1])
    print("Day: ", today[2])
    print("Year: ", today[0])

printdate()