"functions---if we want particular data repetative times we use function"
# we have to define function first then we can call it anywhere

# syntax of function
# def function(parameter):
	# """docstring""" to add comments
# 	statements

# def Greet():    #paranthesis imp  #function doesn't return anything by default return is None
# 	print('hello')
# 	print('Good morning')
# 	print('Good evening')
# 	print('Good night')
# 	print("-"*30)   #we can multiply

# Greet()  #we have to call defined function to get results
# Greet()
# Greet()
# Greet()
# print(Greet)   #gives memory location of function <function Greet at 0x000001F5A5588EE0>hexadecimal
# print(Greet())  # hello
				# Good morning
				# Good evening
				# Good night
				# ------------------------------
				# None


"to search any funcion click ctrl and hover over function name and press F for search and H for replace"

# l = {Greet(), Greet(), Greet()}  #will  call function then will give value None ----{None}
# print(l)
# A = [Greet(), Greet(), Greet()]  #will  call function then will give value None ----[None, None, None]
# print(A)
# T = (Greet(), Greet(), Greet())  #will  call function then will give value None ----(None, None, None)
# print(T)
# D = {1:Greet(), 2:Greet(), 3:Greet()}  #{1: None, 2: None, 3: None} duplicate values are allowed in dict
# print(D)
# D = {Greet():1, Greet():2, Greet():3}  # {None: 3} duplicate keys are not allowed in dict
# print(D)

# for i in range(1, 101):
# 	print(f"--------{i}---------")
# 	Greet()

'dynamic function'
# def Greet(value):    # we can 
# 	"""for greeting student"""
# 	from sys import argv
# 	print('hello')
# 	for i in argv[1:2]:
# 		print('Good morning')
# 		print(argv[1:])
# 	print(f'Good {value}')  #define value for dynamic fucntion
# 	print('Good night')
# 	print("-"*30)

# Greet("message")	
# Greet("Night")	

'square root example'
# def square_root(number):
# 	"""for finding square root"""
# 	print(f"the square of,{number} is, {number*number}" )

# square_root(4)
# square_root(10)

# def even_odd(num):
# 	"""find even or odd number"""
# 	if num %2 == 0:
# 		print("Number is even", num)
# 	else:
# 		print("number is odd", num)	

# 	print(num,"is a integer")	

# even_odd(40)
# even_odd(27)

'factorial example'
# def fact(num):
# 	"""factorial"""
# 	result = 1
# 	while num >= 1:
# 		result = result * num
# 		num = num - 1
# 	return result	
# for i in range(5,10):
# 	print("the factorial of is:", fact(i))

# fact(50)	

print("before defining function")
def func():
    print("hello world")
    # return [1,2,3]
    return "abc"
    return 10.25
    return 2+3j
    return {10}
    return {"a": 10, "b":20}
    return (10,)
    return 10, 20, 10.5, [1,2,3], {10:55, 20:66}



print("after defining function")
print("before calling function")
res = func()
# res.append(20)   #[1, 2, 3, 20] <class 'list'>
# res.extend("abc")   #[1, 2, 3, 'a', 'b', 'c'] <class 'list'>
# res.popitem()   #{'a': 10} <class 'dict'>
# res.pop()
print(res, type(res))  #heterogenous return is tuple always
print("after calling function")

# def calculation(v1, v2):   #argument values is important if it is available in statments
#     a = v1 + v2
#     s = v1- v2
#     d = v1 / v2
#     m = v1 * v2
#     print(a, s, d, m)

#     return v1 + v2

# calculation(2, 5)   #only statement no return we just called the function
# res = calculation(10, 20)    
# print(res)

# def calculation(v1, v2):   #for making a func dynamic do not use print as it always print whenever we call func
#     a = v1 + v2
#     s = v1- v2
#     d = v1 / v2
#     m = v1 * v2

#     return f"""values passsed: {v1} {v2}
# adiition: {a}
# substraction: {s}        as its multiline string indentation is not required
# Division: {d}
# Multiplication: {m}"""

# res = calculation(27, 45)
# print(res)

# flag = 1
# def prime(v1):
#     for i in range(2, v1):  #value is excluded
#         if v1 % i == 0:
#             # print("non prime number")
#             flag = 0
#             break
#         else:
#             flag = 1
#     return flag        

#     # print("prime number")  

# res = prime(17)
# print(res)
# if res == 0:
#     print("non prime number")
# else:
#     print("prime number")

'2: nested function----define a function inside another function'

# print("before")     #line by line execute kara
# def outer():
#     print("inside outer function  1")   
#     def inner():
#         pass
#         print("inside inner function  1") 
#     print("inside outer function  2") 
#     inner  
#     print("inside outer function  3")   
#     inner()      # () if inner is not called it won't show anything inside inner funct

# # res = outer  #  if called without paranthesis <function outer at 0x0000016E28998E50>
# print("calling outer")
# print(outer)
# print(outer()) 
# print("after") 

'concatenation'
# def outer():
#     def inner():
#         return "inside inner "
#     print("inside outer")

#     return inner() + "1"    #Nonetype + str typeError

# outer() 
# res = outer()
# print(res)  


"3: pass a function as a parameter to another function"
# def func1(fun):   #
#     print(fun + "world")  #memory add + world ---typeerror
# def func2():
#     # print("hello")    #typeError'NoneType' and 'str'
#     return "hello "
#     # pass

# func1(func2())     # it will be func2 address

"4: return a function from another function"
# def outer():
#     print("inside outer function")
#     def inner():    #inner is local to outer
#         print("inside inner function")
#         # return 10
#     # print(inner)    #<function outer.<locals>.inner at 0x0000025776A88EE0>
#     return inner

# # def inner()          #its different coz than inner in outer function its independent
# # print(outer())       #<function outer.<locals>.inner at 0x00000235749F8EE0>
# res = outer()   # returns memory location of inner function 
# res()               # as outer() is now assigned to res, res has memory location of inner,so calling res will give inner function  
# print(res())

"arguments"
# Formal arguments
# Actual arguments: 
#     1. positional
#     2. default

'''forthe function which accepts/takes argument is formal arguments 
   the value we actually pass during function call is actual arguments'''
# def func(value):      #value is formal
#     print(value)

# func("hello")         # hello is actual

# 1.positional-- arguments in sequence--any 1 args missed generates type error---order must be maintained

# def func(a, b, c, d):     #func() takes 3 positional arguments but 4 were given 
#     print("inside", a, b, c, d)

# func(1, 2, 3, 4)    #TypeError: func() missing 1 required positional argument: 'd'

"""
1.order maintain theva lagto postional arguments cha.
2.jr ekhi argument missing rahla tr error raise karto
3.jr 3 formal argument asel ani 4 actual define kele tr typreerror yeto
4.jr define krtani sequence chukla tr value tr bhetel but variable diff rahil for eg in place of name we provide
  age tr to name = age dakhvel in result"""

#2. default --
# def func(name, surname, address="wardha"):   #default value is provided
#     """to check output by defining default argument"""    #docstring optional but recommended for func overview
#     print("details are ",name, surname, address)

# func("john", "watson", "london")   #if actual argument is not provided func will take default argument
# func("john","watson")    #john watson wardha----default args of address provided
"""
1.func define krtana apan jr default value formal argu la assign keli tr to output generate karel jari apan actual value
  nahi dili tri 
2.default arguments should always be defined at last not on 1st position otherwise 
  syntax--non-default argument follows default argument
3.order of sequence maintain thevaychi  
"""

# 3. keyword argument
# def func(name, surname, address):
#   print(f"""personal details are:
# {name} 
# {surname} 
# {address}""")

# func("shubham", "bakade", "wardha")
# func(name="shubham", address ="london", surname="bakade")  #if keywords are defined,the func will mapp the argument and give true output
'''
1.inside 10 20 30 40 --jr apan prtek key/variable la value define keli function madhe tr 
no mater what postion la define keli(a,c,b,d or a,b,c,d), value barober bhetel to func mapping karel tya key chi
2.'''

# 4. Variable length arguments---*args---shows in ()tuple

# def func(*args):  #min 0 max= infinite
# 	print("Given data", *args, type(*args))

# func([1,2,3],10)  
"""
1.number of formal arguments 
"""

# def addition(*args):
# 	total = 0
# 	c = 0     #for average as len(args) is different as diff data types available
# 	for i in args:
# 		if type(i) == int:
# 			total += int(i)   #typecasting for any string args present in actual argument
# 			c += 1			
# 	average = total // c  # (13, 2.6) return in tuple
# 	return total, average

# res = addition(1,2,3,4,3) 
# res = addition(10,20,30,40,"50",60+2j)      #(100, 25)  num of int are 4 as "50"string and other is complex
# print(res)

# 5. Variable length keyword arguments---**kwargs---shows in {} dict

# def func(**args):   #**kwargs means v.l.keyword argument takes min.0  max=infinite 
# 	print(args)
# func(a=10,b=30,c=40)    #{'a': 10, 'b': 30, 'c': 40}  gives in dict form as it consider key value pair

# def func(a, b, c, *args, **kwargs):   #postional args are always 1st
# 	print(a, b, c, end=" ")
# 	print(args, end=" ")
# 	print(kwargs)

# func(10, 20, 50, 505, 666)  #10 20 50 (505, 666) {}-- as keyword is required for vlka
# # func(10, 20, 50, x=22, 505, 666)   positional argument follows keyword argument --xxxxxxxxxnot allowed
# func(10, 20, 50, 505, 666, x="val1", y="val2")   #10 20 50 (505, 666) {'x': 'val1', 'y': 'val2'}

# def func(a, b, c, *args, **kwargs):   #postional args are always 1st
#     """addition of all types of arguments"""

#     print("positional argument:", a, b, c,)
#     print("variable length:", args)
#     print("variable length keyword", kwargs)

#     t1 = a +b +c
#     for i in args + tuple(kwargs.values()):    # single for loop madhe dict la tuple madhe convert kela ani loop run kela
#         if type(i)== int:
#             t1 += i
#     # for j in kwargs.values():
#     #     t1 += int(j)        
#     return t1    

# print(func(10,20,30,555,666,d=10,f=20))   # t1 = 1311

# def func(name, surname, marks = 78, *args, **kwargs):
#     """all types of arguments in single function"""
#     print(f"""
# types of arguments:
#     positional: {name, surname}
#     default : {marks}
#     variable len : {args}
#     variable len keyword : {kwargs}""")

# func("sam", "ross", 98, "python","durga", A ="english",B = "Maths")

"scope of variables"
# --access same line, inside function, another module

# types of variables
# 1. Global--defined outside function
# 2. local--defined inside function
# 3. Nonlocal --it is 

'Global variable'
# var = 100    #defined outside it is called global variable
# def func():
	# """global variable--can be called/import in another file also"""
# 	print("inside function:", var)    #accessed globle variable

# func()   #inside function: 100
# print(var)   #  100---doesn't change until redifined

# var = 555    #we modified 
# print(var)  #555

'local variable'
# var = 100
# def func():
# 	"""local variable"""
# 	# print(var)   #UnboundLocalError: local variable 'var' referenced before assignment---variable che nav same aslya mule 
# 				   # conflict hoto and python error deto karan local var apan khali define kela and tychya adhi apan reference dila 
# 	var = 333    #this is local variable of function--means local to function
# 	abc = "local to function"
# 	print("inside fucntion:", var)

# func()    #inside fucntion: 333
# # print(abc)    #NameError: name 'abc' is not defined---as its local to func()
""""we cannot call or access local variable outside any function.it is bound to that function only
also we cannot modify global variable inside function we can only access it or call it to modify it we have
to declare it"""

"""methode to modify global inside fucntion"""
var = 100
# def func():
# 	"""modify global inside function"""
# 	# print(var)
# 	def inner():
# 		print("inside inner:", var)   #global var
# 	global var    
# 	var = 250
# 	inner()

# print(var)
# func()
# print(var)
"""cannot access and modify global variable with same name inside function it will raise syntax error
var = 100
def func():
	print(var)----will raise syntaxError as var used prior to global declaration
	global var  ----declare for modification
	var = 250 -----new global value
	print(var) 
	then"""

# def func():
# 	"""global declaration"""
# 	def inner():
# 		print("inside inner: ",var) #100 as after inner() global is modified
# 		# print(new_var)   #free variable 'new_var' referenced before assignment in enclosing scope
# 	inner()    # as python goes line by line inner will be called 1st and var value will be accessed global
# 	new_var = 11
# 	global var
# 	var = 600
# 	print(var, new_var)
	
# func()

# var = 100    #global to all function
# def outer():
# 	"""defining nonlocal"""
# 	var = 200    #local to outer function and non local to inner function
# 	def inner():
# 		# print(var)   # error as used before declaration
# 		global var # calling/declaring global if we want to use global var value in inner function
# 		var = 654  # redfining global var value after declaration
# 		print("inside inner function", var)  #takes var from outer function local
# 		return "hello"
# 	print(var)
# 	inner()
# 	return inner

# res = outer()
# print(var)
# print(res)      # prints memory location of inner funct as outer returns inner
# res()       #calls inner function as it has memory location of inner

# print(globals())
# print(locals())

"main method"

"""kuch bhi function call krne hai to main method ke ander call karo"""














"Lambda------------one liner function------anonymous function---------funcion without name"

# var_name = lambda args : operation 
# var_name(args)

s = "lambda is one liner function"
# print(lambda s : s)     #<function <lambda> at 0x00000194FB958E50> gives memory location
# (lambda s : print(s))(s)   #geeksforgeeks
# lf = lambda val1 : val1
# print(lf)    # we didn't call lambda func here
# print(lf("lambda"))   #we call here

# def func(val1, val2, *args, **kwargs):      #normal function takes more line coding
	# return val1 * val2 , args, kwargs

# print(func(10, 20, 60, 70, 80, a=10, b=20))	   #(200, (60, 70, 80), {'a': 10, 'b': 20})

##############################################################

# lf1 = lambda val1 : val1     # one line coding
# print(lf1)            #<function <lambda> at 0x000001EF055C80D0> gives memory location as we didn't call lf1 function
# print(lf1(10))     #we called lf1 here so it gives value


# lf1 = lambda val1, val2, *args, **kwargs : [val1 * val2, args, kwargs]             #packed in tuple or list or set
"""gives same output as function
in def fucntion as it returns packed tuple,
but in lambda function we have to pack the expression or operation in tuple or list or dict"""
# print(lf1(10, 20, 60, 70, 80, a=10, b=20))    #(200, (60, 70, 80), {'a': 10, 'b': 20})

# filter, map, reduce

"""filter"""
#filter object---filter is class-----filter gives true and false 
#filter requires (function, iterable)
#filter gives output if the condition is satisfied and it is True
#filter hit condition satisfied object
# function: function that tests if each element of a sequence true or not.
# sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators

# def check_even(val):
# 	if val % 2 == 0:
# 		return True
# 	else:
# 		return False	

# print(check_even(10))

# l = list(range(2, 21))

# res = filter(check_even, l)
# print(res)          #gives filter object memory location
# print(list(res))       #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# res_lambda = filter(lambda val:val % 2 ==0, l)   
# print(list(res_lambda))        #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

map # map is a class we can call it map object
"""
1.hits every object
2.requires function and we can pass multiple iterables
3."""

# l1 = [1,2,3,4,5]
# l2 = [10,20,30,40]
# l3 = [100,200,300,400,500]
# l4 = [22,55,99,66,77,88,33]

# res = map(lambda a, b, c: a*b, l1, l2, l3)              #[10, 40, 90, 160]
# res = map(lambda a, b, c: a+b*c, l1, l2, l3)            
# res = map(lambda a, b, c: a*b/c, l1, l2, l3)            #[0.1, 0.2, 0.3, 0.4]
# res = map(lambda a, b, c, d: a*b+c/c, l1, l2, l3,l4)    #[11.0, 41.0, 91.0, 161.0]
# res = map(lambda a, b, c, d,: a*b*d, l1, l2, l3, l4)    #[220, 2200, 8910, 10560]
# print(list(res))


"""reduce---
it is function, we have to import this
it gives output in a single object like sum,multiplication etc
syntax: reduce(function, iterable) """
from functools import reduce

# l = [1,2,3,4,5]
# l2 = [55,66,55,44,33]
# def sum():
# 	sum = 0
# 	for i in l:
# 		sum += i
# 	return sum
# print(sum())		

# res=reduce(lambda x,y : x+y ,l, l2)
# print(res)

