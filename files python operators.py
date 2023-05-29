x=4
print(id(x))
y=3+x
print(y)
t=2*y
print(t)

p=5
t="hallo"
b=1,2,3
c=[1,2,3]
d=700
f= 6.9999
print(type(f))

#arethmatic_operation
#add +
# subtract -
# mul *
         #div /
#modulas %
#exponent **
# floor div //

a=2
b=4
c=5
w=1
print(id(c))
# == equl.
# != not equl.
# < less than
# > greater than
# >= grt. than or equal
# <= less thn. or equal

a=1
b=2

# logical gates
# f and t -----(and gate opp.) output -- f
# t and t ----- output --- t
# f or t ----( OR gate) ---output --t
# not f ---( not gate) ---output-- t

# bitwise logical OPP.
# & --- and
# | --- or

# ^ --- xor
# >> binary bit shift right 
# << binary bit shiftleft

# identity opprator
# is --------- same as == 
# is not ----- same as !=

# (difference in 'is' and '==' ) ---- "it checks ,if both are as same as datatype/id"
# no. above 256 will not be considered as same /ID

#
# in ---used to check if it's in that or not---O/P -- T or F
# not in --- used to check if that is not in that --- O/P--- T or F

# conditional operator

input = input('enter the phone no.')
input=str(input)
if len(input) <10:
	print('invalid oNe')


a='mday'
b=str(a)
if len(b) >2:
    print('done')


d=899
if d<700:
        print('do again')
else:
                print('ok')


a=23

if a==20:
        print('ok')
elif a>20:
        print('no try again')
elif a<20:
        print('not less')

b=7
if b>=5:
        print(' sucess')
else:
        print('scratch card' , 'NO. :')
#input function



#Ex:  a= input(' No. ')

#loop                          {the no. [listNo.  (list' no. 
#                                of list   range/  increaent
#                                starts   upto      rate)
#                                 from}  thatNo.]

#                                    |          |         |
print(range(3, 7, 2 ))      # ( 3   ,     7 ,       2 )
        
print(range(0 ,9 , 3))      # [ 0    ,     9,        3]

sum=0
for i in range(1,11):
        sum=sum+i
        print(sum)
print(sum)


i=1
while i<8:
        print(i)
        i=i+0.5

#break--- breaks the loop process
#continue---continues the loop process

for i in 'crazzy oXyuz':
        if i in 'aeiou':
                break
        else:
                print(i)
                
for i in 'crazzy oXyuz':
        if i in 'aeiou':
                continue
        else:
                print(i)
                

        
for i in 'crazzy oXyuz':
        if i in 'aeiou':
                print(i)
                break
                
        else:
                print(i)
                
#pass:   passes    
for i in 'crazzy oXyuz':
        if i in 'aeiou':
                print('vouel')
                pass
                
        else:
                print(i)
                

#LIBRERY_module_functions
                                               #[ module< name > . function< name> ]
                                              
#  MATH_MODULE:

#print(dir(math))         --- gives the list of all the available functions in this module
a=-5
#print(math.log(a))      ----modele_name.function_name(variable a)
#print(math.log10(a))   ---log_base 10
#print(math.exp(a))     ---exponetial 'e'
#print(math.sqrt(a))    ---squar_root of a
#print(math.power(a,2)) -- a^2
#print(math.factorial(a)) -- a! 
#print(math.fabs(a))      --- gives absolute value in float

 
#print(math.sin(a))   -- sin of a , cosine of a 
#print(math.cos(a)   --- Etc. any trigonametric operation of 'a' 

#help(math)           ---helps to find out which function does what



#RANDOM_MODULE :

#import random        ---- picks up a random number

#a=[2,3,5,6,7,10,18,25]   --from a given list of numbers, which is defined to veriable 'a'
#print (random.choice(a)) -- choice function's opp.> 'randomly chooses a no from a given list


#random.shuffle(a)   ---randomlly changes the order of list number assigned to verriable 'a'
#print(a)

#print(random.randrange(1,20))  ---randomly picks a no. from given range { INT NO.}

#print(random.uniform(1,20))    ---randomly picks a no. from given range { FLOAT NO.}


### print(random.randrange(1.99,20.99))  --- always gives float no.



#print(random.random())    ------ picks randomlly a no. in the range '0 to 1': { <= but never >1}



#random.seed(2)     ---- provides an id to the randomlly gnerated no. , hence it's no longer random; '2'--> ID

#print(random.random())
#print(random.random())
#random.seed(2))          ---  everytime 'random.seed(2)' typed before random func. > it generates the same(id) random_no. again
#print(random.random())

#>>> random.seed(3)
#>>> print(random.random())
#0.23796462709189137
#>>> random.seed(2)
#>>> print(random.random())
#0.9560342718892494
#>>> random.seed(3)
#>>> print(random.random())
#0.23796462709189137
#>>> random.seed(2)
#>>> print(random.random())
#0.9560342718892494


#   STRING_OPP :

                                # 0123.56.8.1011...........
                               #   |||||  ||  | ||||||| |
a= 'this is a string'        # 'this is a string'

print(a[11])                     #index value is always represented in [ ]

print(a[-1])
print(a[-2])                     #[-2 or -1] ; ' -* ' --> last ones index value

print(a[0:3])                   #slicing -> from index '0' upto '3'

print(a[:: -1])                 #'string' in reverse config. & print each charec.
print(a[::-2])                  #'string' in reverse cofig. & print each charec. but skip1charec. in between
print(a[:: -3])                 #print each charec. in reverse but skip 2 charec. in between

help(str)

print(a.upper())              #same string in upper/capital form
print(a.lower())

b=' hello I AM karl'
print(b.swapcase())        #swaps the form of string ( small -> capital )or ( capital -> small)
print(a.title())               # first charec. of each word in capital
print(a.capitalize())        # only first charec. of string will be capital
print(b.istitle())             # checks if the first charec. of each word in capital or not <o/p> TorF
print(b.isupper())           # checks if that string is in upper OR not



d='  ' 
c='@@@ap@ple@@@'
print(a.istitle())
print(a.islower())
print(a.isalpha())         # checks if each letter is alphabet OR not
print(c.isalpha())         # scape( _ ) in between letters is aslo counted ; hence it gives F ...as space( _ ) is not an alphabet
print(c.isdigit())          # if digit or Not ; digits = '123456789'
print(c.isalnum())        # TRUE only when-> no spaces, no special charec.
print(d.isspace())        # TRUE only when; string contains ONLY spaces.

print(a.find('i'))           # finds the index no. from that string
print(a.find('i',4,10))     # finds in the range
print(a.rfind('i'))          # finds from the reverse.
print(a.index('i'))          # finds the index of that letter
print(a.index('i', 4,8))    # finds index in the range
print(a.rindex('i'))         # finds index from the reverse.
print(a.count('s'))        # counts the letter present in string
print(a.find('v'))           # if not present gives -1
print(a.replace('s','@',1)) # replaces in string. '1'--> index no.
print(len(a))                # gives length of the string

print(a.ljust(25, '-'))      # fills with extra till index no. 25
print(a.ljust(25, '1'))      # fills with one charecter_space.
print(a.ljust(25, '$'))     # fills from left direction
print(a.rjust(25, '$'))     # fills from right direction
print(a.center(25,'$'))   # fills from both direc ; original string in the centre, total index no. 25
print(a.zfill(25))           # fills with 0 from the begining with the string, and makes index no.25
print(c.strip('@'))         #strips from both the begining and ending ; but not in the middle
print(c.lstrip('@'))        # strips from the left side
print(c.rstrip('@'))       # strips from the right side

print(c.split())            # represents all the letters present in the string as A list [' ']
print(a.split())            # whenever it finds a space it considers upto that perticular point as a word
print(a.split('i'))          # whenever it finds 'i' splits upto that point and represents that as a separate word; space is also counted ; till it discovers 'i' again combines everything as a single 'word'

print(a.partition('s'))    # gives a list of 3 'word's ; everrything occours before 's' as 1st 'word' ; 's' as a word; everything comes after 's' as 3rd 'word'
print(a.rpartition('s'))   #

print(a.endswith('ing'))    # checks wheater it starts with 'ing' ; o/p --> TorF
print(a.startswith('ing'))   # if start's with 'ing' ; O/P --> TorF

f=['electro' , 'old' , 'days' ,'are' , 'best' ]
print(''.join(f))          # joins everything together as a single 'word'
print('_'.join(f))         # 'x' ; puts x in between while joining

help(str)


# LIST OPP :

a= [12, 56 , 6.5 , 'abc']
print(a)
print(a[0])                  # prints<INDEX No.>str a[]
print(a[1])                  # prints that whose index no. is [1]
print(a[-1])                 #prints the last one<index no. '-1'

print(a[0:3])               #print from index'0' upto '3'
print(a[:3])                #print from the begining upto index'3'
print(a[1:])                 #print from index'1' till the end.
print(a[::2])               # print from begining and skip 1 charec. in between.
print(a[::-1])              #print


help(list)

a=[23,45,6,7,8,9]
a.append(466)             #incert new stuffs at the end of the list.

m=[99,79]
a.append(m)              # Add new list to existing list ; but as a list not as a list element.
a.extend(m)               # add new list to existing list, as an indivisual elemet.

a.insert(1,'new')         # incert new stuffs at the begining of list at specified index No.
a[3]= 'update'           # updating list at a specified INDEX No.
b=[3,2,1]
del(b)                     # 
del(a[3])                #
del(a[0:1])               # 
print(a.pop())          # last element
print(a.pop(1))         # elemenates according to INDEX No.
a.remove(466)         # removes the element ; in case there are two of them are present....then removes the first one.
a.reverse()             #reverses the order of list.
n=[1,2,3,4,5,6]
n.sort()                 # list in ascending order.

n.sort(reverse=True)  # list in descnding order.

print(a.index(9))       # index no.
print(a.index(9,1,4))  # gives index no. of multiple elements.
print(a.count(9))      # counts.


#  TUPPLE :

a=(1,2,45,6.7,'abc')            #
print(a[0])                     #
print(a[1:3])                   #
print(a[::-1])                  #
print(a.index(6.7, 2,4))        #
print(a.count(6.7))             #

a=list(a)                       #
print(a)                        #

a=tuple(a)                      #
print(a)                        #

b=(2,3,5,(3,2),6,9)             # tuple inside tuple.
print(b[3][1])                  #
c=(22,34,(3,6,(10,90),77),89)  #
print(c[2][2][1])               #

          #same for list:
d=[1,2,3,[2,3],5,6]             # list inside list.
print(d[3][0])                  #


                #DICTIONARY :
g=['abc' ,23, 45]                              # data stored inside a list.
g={'name' : 'abc' , 'id' :23 , 'age':45}     # data stored with clarity; stores data at a specific key element , each key has a value assigned to it.

print(g['name'])                        # print the value assigned to it.
g['new key']=99                         #adding a new stuffs to the dict.
g['name']='RAM'                      # updating a Dict.
del g['new key']                        # dels the value assigned to the key.
g.pop('age')                        # pops the specified item only.
g.popitem()                           #No need to specify to pop item.

g.clear()                            # clears everything and shows an empty Dict.

g={'name' : 'abc' , 'id' :23 , 'age':45}
h=g.copy()                                   # makes a copy of it and assigns it to another veriable as Dict.

g.get('name')                      # presents the item assigned to it.
print(g.get('name1'))                     #if not present in dict. ; returns NONE
print(g.get('name1' , 'not present'))    #we can change ,what it returns.

print(g.setdefault('name'))              #works same as the .get if only the item is in the Dict.
print(g.setdefault('name1' , 'new name'))            # if not in Dict. ; adds to Dict.

k={'name' : 'r@125' ,'id' : 23 , 'age' : 45}
g.update(k)                                             #Updates Dict. with the key that isn't present in the existing one.

a=['a','b','c']
print(dict.fromkeys(a,10))             #Takes the elements of list and assigns a same value to them.

b=[1,2,3]
print(dict(zip(a,b)))                  # takes the elements of 'a' as keys & 'b' as the values wi'be assigned to them.

print(zip(a,b))                         #

dict = { 
  'key': 'value1',
  'key_1': 'value_2'

}

print(g.values())                       # gives the value present in Dict.
print(g.items())                        #gives a list of tuples of pairs of Dict. keys&items.
print(len(g))                   #Len of Dict. ; len= no. of key-values present in Dict.
print(sorted(g))                # keys in ascending order.


#       SET :

a={23, 5.6, 'abc', (5,6)}      # set of multiple type of elements; also repeted elements are not alowed.

a={1,2,3,4}
b={3,4,5,6}

print(a.intersection(b))        #provides a set of elements that are common.
print(a.intersection_update(b))  #Same as the above ; also updates the set.

a={1,2,3,4}
print(a.union(b))                        #Combines both 'a' & 'b' and presents as a single set.

print(a.difference(b))                  # gives a set of elements of 'a ' that is not present in set 'b' .
print(a.difference_update(b))         # same as above ; also updates set 'a' .d

a={1,2,3,4}
a.update(b)                   #Combines everything ; forms a single set &  updtes.
a={1,2,3,4}
a.symmetric_difference(b)        # combines everything & forms a single set by removing the common elements.
a.symmetric_difference_update(b)    # same as above ; aslo apdates.
a={1,2,3,4}
print(a.isdisjoint(b))                  # if no common elements are in between both the sets ; then only gives true.
print(a.issubset(b))                 #TRUE only when each element of set 'a' is a part of set 'b' .
print(a.issuperset(b))              #TRUE only when each element of 'b' is a part of 'a' .
a.add(78)                       # adds to SET.
print(a)                        # set does not have index no. hence not sure where it adds that element.
a.discard(78)                   # removing that element.
print(a)

a.remove(4)                 # removes. [if item is not in set ; gives error] thats not the case in .discard
print(a)
a.pop()                 # pops the element present in set.
print(a)
a.clear()               # clears the entire set.
print(a)                #


# FUNCTION :

def function_name():
        a=2
        b=3
        print(a+b)

def function_name(a,b):           # assign parqmeter values to function name ; gives the sum of the assigned values.
        print(a+b)                    # assigned parameter values a

def function_name(a,b):          #To access the sum outside the function; we need to store the sum at a veriable
        e=a+b                         # and incert retunn() inside the function.    
        print(e)
        return(e)

ver=function_name(3,4)
print(ver)


def function_name(a,b,c=5):             #default arguments.
        print(a)
        print(b)
        print(c)

function_name(2,3)


def function_name(a,b=1,c=2):           # if parameter value is provided then it skips the default value.
        print(a)
        print(b)                                # we can not define a non default parameter after a default parameter.
        print(c)

function_name(5,6,7)


def function_name(a,b,c):               #keyword arguments.
        print(a)                                # right argument to the right parameter.
        print(b)
        print(c)

function_name(2,c=5,b='2nd')

                                                #veriable length argument :
def function_sum(*arg):                 #Not sure how many arguments will it takes? ;put *arg & all the argumrnts will be casted to parameter(arg) as a tuple. 
        print(arg)                            #more like a packing of multiple arguments as a tuple to parameter.

function_sum(23,24,25,67,'abc',90)      # can't take non veriable length argument  before a veriable length argument.

def function_sum(a, *arg):              # first argument will be assigned to non ver len argument , rest goes to ver len argument.
        print(a,*arg)           


def func(a,b,c):
        print(a)
        print(b)
        print(c)
                           # instead of providing different values to different parameters, we can provide a string from which all the parameters will take values respectively.
m='cat'      
func(*m)                # simillarly we can use tuple , list also.
m=['cat','dog','elefant']
func(*m)

                                #veriable len keyword arg.
def func_marks(**kwarg):
        print(kwarg)
        return(kwarg)

func_marks(maths=9,chem=8,eng=7)        # kwarg as adict.{ keys along with data as a Dict.}

e=func_marks(maths=9,chem=8,eng=7)     # storing the dict. to a veriable.


def func_marks(**kwarg):
        print(kwarg)
        for i in kwarg:
                if kwarg[i]>40:                         # kwarg[i] -> because; i is acessing items from Dict.
                        print('pass')
                else:
                        print('fail')
        return(e)

e=func_marks(math=35,eng=70,his=80,chem=29)



def func(arg):                          #call by referance. 
        arg.append('hello')            #
        print(arg)

m=[23,34,79,90]

func(m)
print(m)                          # m has changed.


         #CLASS :

                                    # logically connected functions & veriables
        

class Bank:             # To leave a class empty; we use pass
        pass            #Dont do anything


                                   #To execute a function present inside a class; create object of the class.
class Bank:
        def deposit(self , amount):            # when defining a func inside a class , it comes with a pre-build parameter
                print(amount)
                self.balance +=amount
                print(self.balance)                  # self is not a normal parameter, it's the referance to the object which is calling the function
                                                       # [self is -->customer1]
customer1= Bank()                       # to create objects; use constructor.
customer1.balance=1000
customer1.deposit(89)                   # first object is customer1
customer2=Bank()                        # default constructor present in the class -->Bank() [ class name_() ]
customer2.balance=3000              #Create an instance/ object attribute that works as a veriable for only that perticular object. { balance } 
customer2.deposit(100)                 # all the functions present inside a class called METHODES.
                                                 # use the object to add all these functions inside class     { self. } 
                                                # all the methodes can't be called directly. They can be called by using the object of class
                                                # we can have as many object as we want; each time an object acesses the deposit func. the self changes accordingly 


class Bank:
        ''' THIS IS A CLASS '''                 #adding a description to class; it will be cosidered as as comment.
        def __init__(self , balance):            #Defining a attribute for the class itself by using __init__()
                self.balance =balance          #
        def func(self, deposit):                 #
                print(deposit)
                print(self.balance)
                self.balance +=deposit
                print(self.balance)
        def interest(self):
                print('10%')

customer1=Bank(100)
#customer1.balance=100
customer1.func(20)
customer2=Bank(200)
customer2.func(50)


help( Bank )                                    #Help to understand



class Plane:
	def __init__(self, people):                     #No. of people can get in is fixed to 10.
		self.people =people                 # if No. of entry exceeds the fixed capacity of people; 'RED' indicator will glow
	def func_plane(self, entry):                     # else 'GREEN' indicator will glow up [ means; plane capacity is'nt full yet.
		print(entry)
		if entry<=self.people:
			print('G')
		else:
			print('R')


obj1=Plane(10)
obj1.func_plane(9)


class Atm:                                       # adding veriables inside a class
        location= 'bangalore'
        a=[4951,4959,4980,4988]                 #To acess the veriable outside; use object/self.
        def __init__(self, key):
                self.key =key
                print(key,'+xxxx')
                if (self.key) not in self.a:
                        print('check again')
                else:
                        print('ok')
                print(self.location)

obj1=Atm(4988)
obj1.location


class SBI(Bank): #child        #We can use methodes present in any class, in another class[ hence no need to define all the functions again ]
        def interest(self):
                print('6%')           # inheading that class { constructor_('the name of class that we want to acess the methodes of.') }
                                        # We can use multiple classes inherited at once ; provided that these classes are defined before.
cus1=SBI(50000)                   #Like : class SBI(Bank, class1, class2):
cus1.func(1000)                     # though the class we are inheriting has a__init__()methode, we have to use it sparately
cus1.interest()                                      #Must incert values -> SBI('value').....otherwise shows error.
                                        # if we dont want to use any method present inside the class and use our own; then we can overwrite them.

#hi update_311


######   DECORATORS:

name= 'Abc'                                         #To alter the functionality of the given func. 
def my_decorator(func_func1):                          #To restrict the acess of the func; or similar ctivities : To execute oth func before the main func gets executed
        def wraper_func(arg_1):                        ### func1 itself goes to {func_func1 parameter} as argument
                if name.startswith('A'):                  # internal_func -->wraper_func 
                        func_func1(arg_1)
        return wraper_func                         # returns wraper_func in such a way that it is ready to get executed

@my_decorator                              #@<the_decorator_func_name>
def func1(arg):
        print('this is func1')
        print(arg)

func1(2)



######  Python_Files :

ver=open('python_text.txt' , 'r')         #To do amything with the txt file; first of all we need to open the txt file & create a referance of it using a veriable.
#a=ver.read(5)                             # r --> 'mode' that the file opens in ; r : read , w : write, a : append, r+ : both read&write
print(a)                                      # prints first 5 charec.
#print(ver.read())                      #Prints from the 6th charec.
a=ver.readlines()                #To read lines one by one.
print(a)
ver.seek(0,0)                    # To move the curser to the 0th charec from the befining of the file. { 2nd 0 --> begining of the file}
                                     ## 0--> the begining of the file ; 1--> current poosition ; 2--> the end of the file.

print(ver.tell())                   # To find where my curser is.


ver.close()                            #Whenever we open a txt file; make sure to close it , else there'sa chance of memory leakage.


#ver1=open('python_file_w&a.txt' , 'w')     # w -> Write_mode
ver1=open('python_file_w&a.txt' , 'a')       # a-> append_mode.
ver1.write('hi_this_is_new_one@')             #Overwrites_whatever present in that txt file & writes the new string.

ver1.close()

ver2=open('python_files_r+.txt' , 'r+')       #
print(ver2.read(4))               #
ver2.seek(0,0)
print(ver2.write('PYTHON'))   #
ver2.close()

ver3=open('python_files_w+.txt' , 'w+')      #
print(ver3.write('hya'))                      #We can`t read_first ; first write -->overwrite's -> {Then read.}

ver3.close()   

#Attrebutes_python_files:

print(ver1.name)         #prints the name that holds the txt.file.
print(ver3.name)

print(ver2.mode)        #In which mode it is open.
print(ver3.mode)

print(ver.closed)        # checks if the file is closed_OR_not.


######## Python_Generators:

def func():
        i=0                       #Instead of storing all set of the values as a list to memory; it takes_OR_yields values one by one & stores it to memory.
        while True:
                yield i              # 'yield' makes a func->generator.
                i=i+1
                                   # Provides value stepwise.
a=func()                        #Storing the values when it is required_only. 
print(type(a))                            # 
print(next(a))           #1st time we call the func->it goes inside the func ; i=0 , yields_{returns} 0 ,& executes i=i+1. <now_i=1>
                            #next time we call the object it will remember the previous state of the object_&_take the func forward from there.
print(next(a))           #2nd time we call the func->it goes inside the func ; i=1 , yields_{returns} 1 ,& executes i=i+1. <now_i=2>
                            #
print(next(a))           #3rd time we call the func->it goes inside the func ; i=2 , yields_{returns} 2 ,& executes i=i+1. <now_i=3>
print(next(a))           #4rd time we call the func->it goes inside the func ; i=3 , yields_{returns} 3 ,& executes i=i+1. <now_i=4>
                

######## WEB_CRAWLERS :

#{web_crawlers are used to get data from different websites}
#To use it; install->'2'_packages through shell comm.
#01--> pip_install_request
#02--> pip_install_beautifulsoup4


import requests
from bs4 import BeautifulSoup

url = 'https://www.googl.com'   #storing the web_URL to a ver , of which the data we want to collect. 

a=requests.get(url)                    #This gives an acess of that web_page here in python. <get_func is in requests_module>
b=a.text                                  #text_attribute gives all the html_quotes/text present inside the web_page.
result=BeautifulSoup(b)              #BeautifulSoup_module takes the text & render entire html quotes present inside the Web_page. 

for i in result.find_all('a'):            #Find all the_ancher#Tag <for all the source of images_'img'>
        print(i.get('href'))              #Only gives me text present inside href.
                                            #For_image_sources->change 'href' To 'src' {'src'_attribute of thie image #Tag}
