"""
Created on Thu Dec 29

@author: Santosh Parse
@program name: Fixers Utilites
"""
import string
import datetime as dt

print('='*65)
print('Removing leading or lagging spaces from a data entry')
baddata = "    Data Science with too many spaces is bad!!!       "
print('>',baddata,'<')
cleandata=baddata.strip()
print('>',cleandata,'<')
print('='*65)

print('Removing nonprintable characters from a data entry')
printable = set(string.printable)
baddata = "Data\x00Science with\x02 funny characters is \x10bad!!!"
cleandata=''.join(filter(lambda x: x in string.printable, baddata))
print(baddata)
print(cleandata)
print('='*65)

print('Reformatting data entry to match specific formatting criteria.')
print('Convert 2017/01/31 to 31 January 2017')
baddate = dt.date(2017, 1, 31)
baddata=format(baddate,'%Y-%m-%d')
print(baddata)
gooddate = dt.datetime.strptime(baddata,'%Y-%m-%d')
gooddata=format(gooddate,'%d %B %Y')
print(gooddata)
print('='*65)