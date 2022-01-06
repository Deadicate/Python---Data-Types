'''
Text Type (String)
'''

# when writing strings, you can use either single or double quotation marks, it doesn't seem to matter 'hello' or "hello"

# s = 'This is a single line string'
# print(s)
# print(type(s))

# s = '''this is a multiline
# string example'''
# print(s)
# print(type(s))

# multi line strings need triple quotation marks. Again they can be double or single, it doesn't matter as long as there is 3 of them.

# note that when i left both above lines of code in, the console printed them both. maybe if you have a variable given a name, follwed by a print command, it complets that command, then starts anew, so you could theoretically assign one variable multiple references and still have them function. interesting.

# ===========================================================

# find a character by index

# s = 'string sample'
# print(s[5])

# every object is given an index which starts with 0. so s in string is equal to 0 and goes up incrementally from there. Above will only print letter 5 of the indexed object, in this compile

# s = 'string sample'
# print(s[7:])

#above will print everything from the index of 7, which is s in sample to the end. When putting in numbers like this, you have to use the square brackets, it doesn't work with rounded brackets [] and not ()

# slicing
# s = "string example"
# print(s[0:6])

#above example prints from position 0, which is s in string, to the gap, so prints string and nothing after. : means until, or the end if nothing is put afterwards. if i change this to 5, it removes the g, so it needs one space after for some reason.

# the first integer goes from the index, the 2nd is the position after.

# ===========================================================

# immutable - this means something can't be changed. the string values below cannot be changed. strings are immutable, cannot be changed later on.
# s = "string sample"
# s[2] = '0'
# print(s[1:6])

# the above example will lead to an error, as strings are immutable.

'''
Numeric Type (Integer, Float, Complex)
'''

# x = 123456789
# print(x)
# print(type(x))

 # above is an integer object type

# x = 0.123456789
# print(x)
# print(type(x))

# above is a float example. This happens when you have a decimal point. it can only go up to 15-16 decimal places. look at below example

# x = 0.1234567891011121314151617181920
# print(x)
# print(type(x))

# in the above example, it only prints up to 13, as this is 15-16 decimal places after the . and is the limit of python.

# x = 1 + 2j
# print(x)
# print(type(x))

# above is an example of a complex data type. This occurs when you have complex equations and in this case, and imaginary number shown by the j. 


'''
Sequence Type (List, Tuple, Range)
'''

# list

# x = [10, 2.5, 'hello']
# print(x[0])
# print(x[0:2])

# see how lists can also be sliced. makes sense.

# above is list data type. x contains an integer, a float and a string. the commas seperate each of the data types. when we print using an index, 0 is equal to the number before teh first comma, 1 is 2.5 and 2 is equal to hello, as in a list, the index seems to denote at which point in the list it is. remember in a string, each character is its own index, and i assume with an integer also

# y = 123456789
# print(y[3])

# when i try running above, i get the error 'int' object is not subscriptable, which suggests it can't be indexed, or that the index gives the entire number a value, and only seperates then with commas. when i try putting in an index value greater than 2 in the 2nd example above, i get an error. it seems with lists, each item in the list is an index value and can't be subscripted further. - later note, this is wrong. the reason above didn't work was it is just a script or long integer and not a list in square brackets. but it also wouldn't work as there isn't a index = 3. the whole number is index 0. i think items within lists are no subscriptable.

# lists are mutable. they can be changed, unlike strings. lists are made with square brackets []

# x = [10, 2.5, 'hello']
# # print(x)

# x[2] = 'mutable'
# print(x[1:3])
# print(type(x))

# in the above example, index 2 in the list 'hello' is changed to mutable, as lists are mutable (can be changed).

# ===========================================================

# Tuple
# heterogenous (lists are homogenous)

# tuple = ()
# print(type(tuple))

# tuple data types have rounded brackets () where lists use square brackets []. above is an example of an empty tuple. the same can be done with a list.

# tuple = ("hello", [4,3,2], [1,2,3])
# print(tuple)
# print(type(tuple))

# tuples use rounded brackets and have commas between each item

# tuple = ("hello", [4,3,2], [1,2,3])
# print(tuple[0:2])
# print(type(tuple))

# tuples can also be sliced

# both examples below are tuples. without the comma makes it a string

# tuple = ('hello',)
# tuple2 = 'hello',

# print(tuple)
# print(type(tuple))
# print(tuple2)
# print(type(tuple2))

# if you remove the commas from above, they both become str (strings).

# tuple = ("hello", [4,3,2], (1,2,3),)
# print(type((1,2,3)))
# print(type(tuple))

# you can have a tuple, within a tuple. Above does this by putting index 2 into rounded brackets

# it is good practice to always put a comma after the last index object in a tuple, so it is easy to tell it is a tuple. also without the comma after a single index, it will be a str or int.

# ===========================================================

# tuples are immutable, not like a list

# tuple = ("hello", [4,3,2], (1,2,3),)
# tuple[2] = 'goodbye'
# print(tuple)

# above brings error message 'tuple' object does not support item assignment - in other words it is immutable.

# tuples use less memory, as you can do less with them. should always use over a list when you don't need objects to be mutable.

# ===========================================================

# Range

# x = range(10)
# for n in x:
#   print(n)

# range will start a range from 0 up to the number shown. Always be aware it will miss the last number e.g. above goes 0-9 and not 0-10. Same as earlier example with slicing and the last digit used.

# x = range(20)
# print(x)
# print(type(x))

#when printed in this mannor, it just shows range(0, 20) and not the individual integers in this sequence.

'''
Mapping Type (Dictionary)
'''

# dict = {}
# print(type(dict))

# dictionary mapping types use whatever these brackets are called {}

# dict = {'name':"Ian", 'age':35, "profession":'coder'}
# print(dict['profession'])
# print(type(dict))

# dictionary's seperate indexes using strings, so makes finding information easier than remembering it's position in an index. useful for databases. above i interchangably use both types of quotation marks with no ill effects. each object is seperated by a comma, and after the index ref e.g. 'name' it needs a colon : before inputting what it is. numbers don't seem to need square brackets, though they also work with them too.

# dict = {'name':"Ian", 'age':35, "profession":'coder'}
# print(dict["profession"])
# print(dict.get('name'))

# dictionaries can also use the .get function, in this instance to print something. you can use either above methods, the top method uses square brackets like a list, then the key, the bottom method uses rounded brackets with the .get function before it before using the key after in teh rounded brackets.

# dict = {'name':"Ian", 'age':35, "profession":'coder'}
# print(dict["profession"])
# print(dict.get('name'))

# dict['age'] =25
# print(dict)

# dictionary data is mutable and can be changed. in the above example age was changed from 35 to 25. Also it appears although strings can't be changed, items here in the dictionary can.

# dict = {'name':"Ian", 'age':35, "profession":'coder'}
# print(dict["profession"])
# print(dict.get('name'))

# dict['name']='tobias'
# print(dict)

# here i changed my name to tobias with no problems.

'''
Set Types
'''

# Set looks just like a dictionary, but it only has single values unlike a dictionary.

# set = {1,2,3}
# print (set)
# print (type (set) )

# above is a set example. You can make empty sets by doing below

# set = set()
# print(type(set))

# set2 = {}
# print(type(set2))

# empty curly brackets denote a dictionary, put one item in they become a set. to have an empty set you have to write set() 

# ===========================================================

# sets can have immutable objects. they can contain mixed data types (str, int) but they all become immutable when in a set. sets do not support indexing, so cannot be sliced. 

# set = {2.5, 'John', 12345}
# print(set)
# print(type(set))

# print(set[0])
# TypeError: 'set' object is not subscriptable

# ===========================================================

# sets cannot contain the same element twice. No duplicates. if you try a set will remove the duplicate.

# set = {3.2, "hi", (1,2,3), "hi"}
# print(set)
# print(type(set))

# when i print, it moves the order around in which i input things. Why is this? when i google it, it seems there are complex work arounds, but for some reason Kingsley's works normal, whereas mine doesn't. i am curious to know why.

# ===========================================================

# set = {3.2, "hi", (1,2,3), [1,2,3]}
# print(set)
# TypeError: unhashable type: 'list'
# above error occurs because a list is included in the set, denoted by the square brackets within the sets curved brackets. Cannot have mutable 'list' in a set.

# when doing a project, i have to think what data type do i want to use, when are each appropriate.

'''
Boolean Type (True or False)
'''

# yes and no, true and false - all done with boolean type

# print(type(True))
# class 'bool'

# using = is an asignment, which makes one thing into another
# using == is comparing two things to each other, or making them the same

# print(type(True))

# boolean as numbers

# print(True == 1)
# print(False == 0)

# interesting logic, adding/multiplying

# print(True + True)
# print(True * 3)

# not boolean operator

# print(not True)
# print(not False)

# be aware that false = 0 is regarded as being true when using 0 and 1 for true and false. true = 1 so 2 of them is 2. not true = false and not false = true.

# and boolean operator
# print(True and False)
# print(True and True)
# print(False and False)

# true and true is always true. True and false is tainted by False and becomes false. only time you can get a true, is when false is absent, it will always taint what it is with to become false

# or boolean operator

# print(True or False)
# print(True or True)
# print(False or False)

# when using the or boolean operator, it is checking to see if anything is true, if so it will return a true statement. This is different to and boolean operator, as it favours true, whereas and favours false.

