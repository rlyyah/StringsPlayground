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

# Slicing a string

a_string = 'My alphabet starts where your alphabet ends'

print(a_string[3:11])
print(a_string[3:-3])
print(a_string[0:19])
print(a_string[:])
print(a_string[3:11])


# Strings vs. Bytes

'''Bytes are bytes; characters are an abstraction.
 An immutable sequence of Unicode characters is called a string.
 An immutable sequence of numbers-between-0-and-255 is called
  a bytes object.'''

by = b'abcd\x65'
print(by)
print(type(by))
print(len(by))
by += b'\xff'
print(by)
print(len(by))
for b in by:
    print(b)

'''To define a bytes object, use the b'' “byte literal” syntax. 
Each byte within the byte literal can be an ascii character or 
an encoded hexadecimal number from \x00 to \xff (0–255).'''

another_by = b'abcd\x65'
barr = bytearray(another_by)
print()
print('Byte rep: ')
print(another_by)
print('ByteArray rep: ')
print(barr)

'''with the bytearray object, you can assign individual bytes 
using index notation. The assigned value must be an integer 
between 0–255. - The one thing you can never do is mix bytes and strings.'''

barr[0]=102
print(barr)

b_byte = b'd'
s = 'abcde'

amt = s.count(b_byte.decode('ascii'))

print(b_byte)
print(b_byte.decode('ascii'))
print(amt)

'''Link between strings and bytes
For bytes its: decode(),
For strings its: encode()'''

a_string = '深入 Python' 
len(a_string)

by = a_string.encode('utf-8')
print(by)
print(len(by))
by = a_string.encode('gb18030')
print(by)
print(len(by))
by = a_string.encode('big5')
print(by)
print(len(by))

roundtrip = by.decode('big5')
print('a_string =?= roundtrip')
print(roundtrip == a_string)

