#ZacharyW - 13.2 Read the text file today.txt into the string today_string.

today = open("today.txt",'r')
today_str = today.readlines()
print(today_str)