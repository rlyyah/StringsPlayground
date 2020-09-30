import random

s = '深入 Python'
print(len(s))
print(s[0])
print(s + ' 3')

username = 'tomas'
password = 'S3xInTh3C1TY.!@'

# BELOW: THESE are FORMAT SPECIFIERS

'''
Passing a list, and accessing an item of the list by index (as in the previous example)
Passing a dictionary, and accessing a value of the dictionary by key
Passing a module, and accessing its variables and functions by name
Passing a class instance, and accessing its properties and methods by name
Any combination of the above
'''

hellomsg = "hello {0}, your password is: ({1}). Have a nice day :3".format(username,password)
print(hellomsg)

    
SUFFIXES = ['KB', 'MB', 'GB', 'TB']

msg = "1024{0[1]} = 1{0[2]}, am I right?".format(SUFFIXES)

print(msg)

# FORMAT SPECIFIERS

some_float_number = 13.37
print(some_float_number)

new_msg = "my super number migh have been: {0:.1f}, but I've rounded it a lil bit".format(some_float_number)
print(new_msg)

s = '''Finished files are the re-
sult of years of scentif-
ic study combined with the
experience of years.'''
# print(s.splitlines())
print(s.lower())
print(s.lower().count('f'))

# Dealing with queries
query = "user=pilgtim&database=master&password=KappaK3ppo"

a_list = query.split('&')
print(a_list)

a_list_of_lists = [v.split('=') for v in a_list if '=' in v]
print(a_list_of_lists)

a_dict = dict(a_list_of_lists)
print(a_dict.items())
