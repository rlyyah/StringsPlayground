import random

s = '深入 Python'
print(len(s))
print(s[0])
print(s + ' 3')

username = 'tomas'
password = 'S3xInTh3C1TY.!@'

hellomsg = "hello {0}, your password is: ({1}). Have a nice day :3".format(username,password)
print(hellomsg)

    
SUFFIXES = ['KB', 'MB', 'GB', 'TB']

msg = "1024{0[1]} = 1{0[2]}, am I right?".format(SUFFIXES)

print(msg)