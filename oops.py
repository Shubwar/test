"OOPS -- object oriented programming system"


# class ----object/instance
# architecture ----blueprint/model-  1 2 3 4 5 6
# wood class ---- furnitures, sofa, bed-----are objects of wood class
# maida class ----- pav bread naan roti ----objects of maida 


# 1 2 3  -- objects---class int
# 2 +3j ----object ---class complex
# [1,2,3]---object ----class list etc

# characteristics of object:
# attributes/ variable 
# actions/behavior 

#creating class

from ast import Pass

def add():
    pass

class ClassName:   #---empty class--paranthesis optional---capital 
    pass
    #variables
    #method

#functions are called as methods under class

#person -----name, age, address -----attributes---variables
#           walk, talk, laugh, swim----actions ----methods    

# class
# variables
#         instance 
#         class level variable 
#         local 
#         global 
# method
#         instance method #--self reserved keyword--declare,del,access,update ----operates on instance variable---CRUD- Create Read Update Delete
#         class method 
#         static method

# wherever self is used it is used for object
"""init --- instance variable initialise--jab bhi hum constructor me variable attach karte hai hum usse intialise karte hai""" 
# class Person:
#     def __init__(self):  # __funcname__ --special/magic method or dunder method
#         print("in init method",)
#         self.name = "amit"      #attaching variables to object/instance p1
#         self.surname = "bakade"

#creating object
# p1 = Person()        # by default call init method---p1 is object of Person
# print(p1)            # gives memory location of created object at <__main__.Person object at 0x0000018C21117940>
# print(p1.__dict__)   #{'name': 'amit', 'surname': 'bakade'}
# print(p1.name)       # gives attached variable 
# p2 = Person()            #object is creating
# print(p2.__dict__)
# p3 = Person()

# class Person:
#     """"instance variable, for loop to attach variable to object,type of object,isinstance"""
#     def __init__(self, pid, nm, srnm):     # self bydefault is referrenced to person() object----nm srnm postional args for 
#                                            #dynamic code ----init is also known as constructor method 
#         # print("in init method", self)    #----self prints its memory location which is attached to object at creation
#         self.id = pid       # object variable or 
#         self.name = nm      #instance variable
#         self.surname = srnm
#         # print(self.name)                 # to print values attached to instance/object or instance variable
#         # print(self.surname)              # values inside method using self

# lst = []
# for i in range(1, 21): #we can create objects anywhere e.g in for loop
#     p = Person(pid = 100+i, nm = chr(65+i), srnm = chr(65+i) + chr(64+i))
#     print(p.__dict__)                    # to print each iterable  
#     # lst.append(p)                      #memory location of each loop in list
#     # lst.append(p.__dict__)             # dict of p in list for each loop
# print(lst)    

# p1 = Person(101,"amit","bakade")         # __init__() missing 2 required positional arguments: 'nm' and 'srnm'
# print(type(p1))                          # <class '__main__.Person'>
# if type(p1) == Person:                   # valid
#     print("valid")

# check = isinstance(p1, Person)           # it checks whether the p1 is a object/instance of person or not
# print(check)                             # isinstance gives output in true or false
# # print(p1.name)                         # values outside method using object 
# # print(p1.surname)
# print(p1.__dict__)                       #{'name': 'amit', 'surname': 'bakade'}
# p2 = Person("john","watson")

# print(dir(p1))                           #id', 'name', 'surname' __dict__', '__dir__', '__doc__ '__init__'
# print(p1.__dict__.get("name"))           # as dir(p1) has dict we can use methods of dict like ,get


# class Person:
#     """"del, attach var to object, attach arguments, hasattr--setattr--getattr, isinstance, aliasing"""  # doc string
#     country = "India"
#     def __init__(self, pid, nm, srnm, add = "wardha", *args, **kwargs):  # default args,variable length ,vl keyword args
#         # print("in init method", self)     
#         self.id = pid                   #  vaariable initialise
#         self.name = nm 
#         self.middle = args
#         self.surname = srnm
#         self.occ = kwargs     
        
        # del (self.id)                   #delete inside constructor
        # self.address = add  # attach var inside constructor
        
# p1 = Person(102,"shubham", "bakade","pune","vijay",)   
# del (p1.id)                       # delete outside class
# print(p1.__dict__)                #{'name': 'shubham', 'middle': ('vijay',), 'surname': 'bakade', 'occ': {}, 'address': 'pune'}
# p1.age = 22                       #attach variable outside method---attached to p1 only not to other objects
# print(p1.__dict__)                #{'name': 'shubham', 'surname': 'bakade', 'address': 'pune', 'age': 22}

"""doc string"""
# print(Person.__doc__)             # prints doc string of class Person

# p2 = Person(103, nm="amol", srnm="zade", add="dubai", domain = "python", at = "ibm")    #keyword args
# print(p2.__dict__)     #{'name': 'amol', 'middle': (), 'surname': 'zade', 'occ': {'domain': 'python', 'at': 'ibm'}, 'address': 'dubai'}

"""hasattr----getattr----setattr"""
# print(hasattr(p2, "surname"))         #(__obj: object, __name: str, /)--gives true or false
# print(getattr(p2, "surname"))         # returns value of attribute
# setattr(p2, "car", "figo") # 'car': 'figo' set or attach attribute and val to object
# print(p2.__dict__) 

"""isinstance"""
# print(isinstance (p2, Person) )       #(__obj: object, __class_or_tuple: type | tuple[type | tuple, ...], /)

"""object aliasing"""
# p3 = p2
# print(p2.__dict__)
# print(p3.__dict__)                    # same dict as we are alaising not copying if p1 changes p2 also changes

"""class level variable"""
# print(p2.country)

"""instance method-----CRUD operation"""
# class Person:
#     """"access create delete update, to create object always use constructor method"""  # doc string
#     country = "India"
#     def __init__(self, pid, nm, srnm, add = "wardha", *args, **kwargs):  
#         # print("in init method", self)     
#         self.id = pid            #  vaariable initialise
#         self.name = nm 
#         self.middle = args
#         self.surname = srnm
#         self.address = add
#         self.occ = kwargs
        # print(self.country)

#     def show_details(self):       #to READ --getter/ accessor         # ya self la bydefault p1 cha reference yeto
#         # print(self)                         # check reference ala ka p1 cha
#         print(f"""personal details:
# ID:-{self.id}
# Name:- {self.name}
# Middle Name:- {self.middle}
# surname:- {self.surname}
# Address:- {self.address}  
# country:- {self.country}    """)

#     def set_age(self, ag):       # setter / mutator -- to create/attach instance variable we have to use set
#         self.age = ag

#     def remove_var(self):        # delete   
#         del self.name    

#     def update_var(self,new):    #update
#         self.name = new    


# p1 = Person(102,"shubham", "bakade","pune","vijay",)   
# print(p1)      #<__main__.Person object at 0x000001AB2B347940>
# p1.show_details()        #same memory as p1---jevha apan show_ call karto tevha by default p1 cha reference jato def show_details(ref of p1)
# p1.set_age(25)
# p1.remove_var()          #removes from p1 as we called in p1 only{'id': 102, 'middle': ('vijay',), 'surname': 'bakade', 'address': 'pune', 'occ': {}}
# print(p1.__dict__)       #'age': 25


# p2 = Person(103, nm="amol", srnm="zade", add="dubai", domain = "python", at = "ibm")    #keyword args
# p2.show_details()
# p2.set_age(30)
# p2.update_var("John")   # updates name as we call update_var method in p2 only
# print(p2.__dict__)      #age': 30

#DRY
"instance variable"

class Product:
    """instance var, str method, repr method, CRUD, static var"""      # doc string contains class info
    Platform_name = "Amazon"
    # print(Platform_name)                                             # can be access inside class

    def __init__(self,prodbrand,prodname,prodcat,prodprice,prodquan):  #constructor method
        self.prodBrand = prodbrand                                     # instance variable
        self.prodName = prodname
        self.prodCategory = prodcat
        self.prodPrice = prodprice
        self.prodQuantity = prodquan
        self.Platform_name= "Flipkart"                                 # instance var or local var for particular object
        # print(self.Platform_name)                                    # prints flipkart automatically as it is in constructor
        # print(Product.Platform_name)                                 # static var

    def __str__(self):                                      # dunder/ magic method instance method
        print("in str method")
        # print(self.Platform)                              # class level var access inside instance method
        return f"\n {self.__dict__}"                        #represent dict but type is class product----\n for new line
        # return f"{self.prodName} ----{self.prodBrand}"    # to return Prodname, prodbrand  -  Galaxy note ----samsung
        
    def __repr__(self):                                     #repr mandatory to print object list
        print("in repr method")
        return str(self)                                    # if using str then __str__ is mandatory

    def m1(self):
        print(Product.Platform_name) 
        print(Product.address)  
         
        print(self.prodName)  

    def m2(self):
        Product.address = "Banglore"              # new static var but incorrect approach as it depends on reference var
    
    @classmethod                                  # decorator--makeup-beutification
    def get_class_var(cls):                       # cls -- reserved to access class level variable
        print(cls)                                #<class '__main__.Product'>
        print(cls.Platform_name)                  # Amazon  ---cls = Product as self = p1 just on is inside & other is outside
        cls.address = "kolkata"
        print(cls.address)                        # accessed inside class method
        # del cls.address                           #after deletion AttributeError: type object 'Product' has no attribute 'address'


# p1 = Product("samsung", "Galaxy note", "Mobile",75000, 20)  # object creation-- calls init automatically--if print is present in init it will directly print  
# p2 = Product("blaupunkt", "wiper", "Car accessories",750, 15)

# p3 = Product("godrej", "Fridge", "Electronics",75000, 3) 
# p4= Product("Peperfry", "sofa", "furniture",45000, 2)   
# p2.m2()
# print(Product.address)            #to print this we have to call m2 method as it is defined inside m2

# print(p1)
# print(type(p1))                   # shows in dict but type is product
# print(type(p1.__dict__))          #<class dict> shows dictionary
# print(p1.prodName)                # same as before

"""to get output by print p1 w/o using dict we have to add method __str__ in class"""

# print(p1.__dict__)
# print(p1.__dict__, p2.__dict__, p3.__dict__, p4.__dict__)    # normal approach
# print(p1, p2, p3, p4)

"""to print objects in list we have to add representation method __repr__ in class"""  
# to save all dict in one place we have to save it in list format

# prod_list = [p1, p2, p3, p4]  # to get o/p in list form---but shows memory location instead
# print(prod_list)   #but shows memory location instead as we are printing list not objects

# for i in prod_list:                    # to print data of sequence but for this also we have another method
#     if i.prodBrand == "godrej":
#         # print(i)                     #{'prodBrand': 'godrej', 'prodName': 'Fridge', 'prodCategory': 'Electronics', 'prodPrice': 75000, 'prodQuantity': 3}
#         print(i.prodName)
# "using list comprehension"
# l = [i.prodName for i in prod_list if i.prodBrand == "samsung"]  
# print(l)                               #['Galaxy note']

#--------or-------- create repr method and print prod list to print all object in list
# str(p1)                                # calls __Str__ method 
# res = p1.__str__()
# print(res, type(res))                  # calls str method & type is <class 'str'>  as we have return value in string in str method

# p2.vendor = "Flipkart"                 # update or declare new instance var outside class for p2
# print(p2)                              #'vendor': 'Flipkart'} added in p2 only
# print(Product.__doc__)                   # prints doc string---- instance var, str method, repr method, CRUD, static var 

"""Class level variable or Static variable"""
# print(Product.Platform_name)                    # access outside class ---Amazon
# print(p1.Platform_name)                         # access using p1
# print(p1)
# Product.Platform_name = "Snapdeal"
# print(Product.Platform_name)
# del p2.Platform_name                            # delete instance var from p2
# print(p2)                                       #

"class method"
# Product.get_class_var()                         #<class '__main__.Product'>-- weh ave to call 1st to access declared var in class method
# print(Product.address)                          #kolkata -- acccess outside same as platform_name



""""Notes
1.  updating instance variable outside class is same as defining it-p1.var_name = new_value 
    but if var is not already present in constructor it will create new var for that object only
2.  as python is case sensative if we made mistake in var name during update it will create new instance var
3.  for print(p1) to give dict we have to define method called __str__ 
4.  for print(list(objects) we have to define __repr__ method)
5.  __init__ is called constructor method in class
6.  p1 is automatically called while object creation and if print stat is present in constructor it will print
7.  static varibale are called class level variable--common var for all objects---it can be defined anywhere 
    in class but outside method
8.  can be accessed in class, constructor--className.statvar_name or self.statvar_name
    in method--className.statvar_name
    can be access outside class--className.statvar_name-----can be declare--className.statvar_name = new value
9.  static variable should be always accessed using className not self.statvar xxxx
10. static var should be declare before delcaring instance var not after consructor as satic is common to all
    it should not be dependable on any object
11. we can define static var in instance method but it is incorrect approach
12. we have to add class method in class and to accesss class level variable we have reserved keyword "cls"
    -to differentiate between instance and class method we have to use decorator "@classmethod"             
    -to manipulate class level var we have class method--- as self point to current object like that
     cls point to className 
13. to access class lvl var outside the class first call the class method and then access that class var  
14. wherever we declare variable we can access that variable  
15. decorator  -- to enhance the feature of function/method --enhancing funtionality of existing function without modifying it 
"""
"to check total number of objects created we have"

# class Employee:                         # to check total objects
#     total = 0                           # class lvl var
#     def __init__(self, id, name):       # use dunder
#         Employee.total += 1             # to access class lvl car we have ClassName.statvar
#         self.ID = id
#         self.Name = name

    # @classmethod
    # def get_no_objects(cls):
    #     print("total number of objects", cls.total) 

    # def __repr__(self):
    #     return F"{self.ID}-----{self.Name}"     # for list printing

    # def m1(self):
    #     print("inside m1")
    # def m2(self):
    #     print("inside m2") 
    #     self.m1()   


# e1 = Employee(101, "D")
# e1 = Employee(101, "D").m1()      # same as e1.m1()
# e1.m2()                           # calls m2 and in m2 calls m1 

# e2 = Employee(102, "E")        
# e3 = Employee(103, "A")        
# e4 = Employee(104, "C")        
# e5 = Employee(105, "B")        

# print(Employee.total)         # this uses self so avoid it and use class method for access class lvl var
# Employee.get_no_objects()     # call method outside using classname

"""sort by lambda"""
# emp_list = ["A Denver", "F Sanfrancisco", "T Newyork", "B California"]
# emp_list.sort()                # sorts on basis of 1st letter
# emp_list.sort(key = lambda x: x.split()[1])     # splits 1st string and sort with index 1 element 
# emp_list.sort(key = lambda x: x.split()[1],reverse=True)     # to sort in decending order 
# print(emp_list)

# empl_list = [e1, e5, e2, e3, e4]             # for this we have to add repr method
# # empl_list.sort()                           #'<' not supported between instances of 'Employee' and 'Employee' does not sort directly we have to give sorting measure 
# empl_list.sort(key =lambda emp: emp.ID)      # gives memory location we have to add repr method
# empl_list.sort(key =lambda emp: emp.ID, reverse=True) # sort in decending order
# print(empl_list)                             # sort and print return from repr method

# l1 = [(4, "H"), (2, "F"), (3, "R"), (1, "A")]  # tuple inside list
# l1.sort(key= lambda x: x [1], reverse=True)    # on basis of 1 index position element of tuple
# print(l1)

# """sorted()---creates new list without hampering original one"""
# print(sorted(empl_list, key=lambda x:x.Name))   #sort by employee name
# print(empl_list)

# t1 = (10,50,5,60,90,2)
# t1.sort()
# print(t1)         #AttributeError: 'tuple' object has no attribute 'sort'

# class
# variables
#         instance 
#         class level variable/ static variable 
#         local 
#         global 
# method
#         instance method #--self reserved keyword--declare,del,access,update ----operates on instance variable---CRUD- Create Read Update Delete
#          ---accessor ---getter
#          ---mutator --- setter   
#         class method 
#         static method --utility method

"static method"
class Employee:                         # to check total objects
    total = 0                           # class lvl var
    def __init__(self, id, name):       # use dunder
        Employee.total += 1             # to access class lvl car we have ClassName.statvar
        self.ID = id
        self.Name = name

    def m1(self): 
        """shubham please use all arguments for practice"""
        pass

    # def static():                 # no reserved args --- if no args it will be static
    #     pass

    # def calculation(a, b):        # if args added 1st arg will be considered self and method will be instance method
    #     print("inside static", a + b)
    @staticmethod #optional but should always use to avoid conflicts b/w instance m and static m
    def calculation_1(a, b):
        print("inside cal", a + b) 

    @staticmethod #
    def stat_in_stat():
        Employee.calculation_1()   #calls static above method



# e2 = Employee(102, "E")  
# e2.calculation(1, 2)          #TypeError:calculation() takes 2 positional arguments but 3 were given-- as e2 = self and a =1 b=? missing
# Employee.calculation(1, 2)    # always use className to call static method--here no reference var present so a=1 b=2

# Employee.calculation_1(10, 20)   #inside cal 30
# e2.calculation_1(15, 30)         #call using instance -- as e2 is not referenced in method--and a=15 b=30
# Employee.stat_in_stat()          #static in static method
"""
1  always use className to call static method
2. no reserved keywords --- if no args it will be static
3. static decorator is optional but should always use to avoid conflicts b/w instance m and static m
4. can be called using instance but decorator should be declared  e1.method(args)
5. we can use default arguments
6. if called w/o deco and has arguments then it will consider 1st args as address of instance and raise error"""













"""properties/feature of oops"""
# inheritance
# polymorphism  --- one person many things
# encapsulation
# accsertion

"Polymorphism"
# --- +

#built-in polymorphism
# ----Duck typing philosophy
# ----operator overloading
# ----method overloading
# ----method overriding

# Duck typing philosophy

#--varibles--methods----functions-- can behave differently
"""
*   Using Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute.
*   Attributes having same name are considered as duck typing
*   Duck-typing emphasis what the object can really do, rather than what the object is.
*   Duck Typing is a concept related to Dynamic Typing, where the type or the class of an object is less important 
    than the method it defines.
*   """
class Duck:
    def talk(self):
        print("Quack")   

class Goose:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("hi hello")

class Dog:
    def bark(self):
        print("bow bow") 

class Bird:
    def chirp(self):
        print("ku ku kooo")               

def call_methods(obj):     # using common fucntion to -- behaves diff for duck goose bark--i.e one thing many forms
    if hasattr(obj, "talk"):
        obj.talk()
    elif hasattr(obj, "bark"): 
        obj.bark()   
    elif hasattr(obj, "chirp"):
        obj.chirp()    
    else:
        print("incorrect object passed")   

class ItQuacks:            # using class to call from geeks4geeks
    def __init__(self,animal):
        animal.talk()
class ItChirps:
    def __init__(self,animal):
        animal.chirp()

# d1 = Duck()
# call_methods(d1)    # as we call function  --quack quack

# h1 = Human()
# call_methods(h1)    # hi hello

# d2 = Dog()
# call_methods(d2)    # bow bow

# b1 = Bird()           # ku ku kooo
# call_methods(b1)

# ItQuacks(Duck())
# ItQuacks(Goose())
# ItQuacks(Human())
# ItQuacks(Dog())    #AttributeError: 'Dog' object has no attribute 'talk'
# ItChirps(Bird())   #AttributeError: 'Bird' object has no attribute 'talk'---add new class --ku ku kooo

# Operator overloading
""" as + has many forms like it behaves different with datatypes 
*   For example operator + is used to add two integers as well as join two strings and merge two lists.
    It is achievable because ‘+’ operator is overloaded by int class and str class.
*   the same built-in operator or function shows different behavior for objects of different classes, 
    this is called Operator Overloading.
*   Consider that we have two objects which are a physical representation of a class (user-defined data type) and
    we have to add two objects with binary ‘+’ operator it throws an error, because compiler don’t know how to 
    add two objects. So we define a method for an operator and that process is called operator overloading.
*   We can overload all existing operators but we can’t create a new operator.
*   when we use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined.
*   You define methods in your class and operators work according to that behavior defined in methods
*   There by changing this magic method’s code, we can give extra meaning to the + operator.
*   """

class Book1:
    def __init__(self, pages, price, a):
        self.NumberofPages = pages
        self.Price = price
        self.Quantity = a

    def __add__(self, other): 
        # print(self, other)  #<__main__.Book1 object at 0x000001B1A3C01C10> <__main__.Book2 object at 0x000001B1A3C01C70>
        return self.NumberofPages + other.NumberofPages   # on what basis tou have to add

    def __sub__(self, other):
        return self.Price - other.Price   

    def __mul__(self, other):
        return self.Quantity * other.Quantity

class Book2:
    def __init__(self, pages, price, b):
        self.NumberofPages = pages
        self.Price = price
        self.Quantity = b
    def __mul__(self, other):
        return self.Quantity * other.Quantity

    def __sub__(self, other):
        return self.Price - other.Price     

b1 = Book1(52, 1200, 10)
b2 = Book2(100, 1520, 15)

# print(b1 + b2)     #unsupported operand type(s) for +: 'Book1' and 'Book2'
# print(b1 + b2)     # directly calls add method in book1 and self becomes b1 and other becomes b2
# print(b2 +b1)      # error as add is defined under book1 not book2---python will consider 1st operand and call method
# print(b2 - b1)     # method added in book 2
# print(b2 * b1)     # multiplication operator
# print(int.__add__(2, 3))


class Employee:
    def __init__(self,salary, name):
        self.perdaysalary = salary
        self.Name = name

    def __mul__(self, other):     # self will be 1st operand and other will be 2nd operand
        return self.perdaysalary * other.Days

class Attendance:
    def __init__(self, name, days):
        self.Name = name
        self.Days = days

# e1 = Employee(780, "John")
# a1 = Attendance("John", 22)
# print("total salary is:", e1 * a1)             #TypeError ----add mul method in class
# method overloading  -concept in java -- no concept in python -- but we can achieve this

#-----------------------J A V A ------------------------------
# signature --- method name , no of args , type of args --- 
# in java method name can be same but the behaviour changes according to requirement

# class A:
#     def m1(self):
#         print("m1 method with 1 args")

#     def m1(self, int a):
#         print("m1 method with 2 args")

#     def m1(self, int a, int b):
#         print("m1 method with 2 int")

#     def m1(self, str a, str b):
#         print("m1 method with 2 string")

#     def m1(self, int a, str b):
#         print("m1 method with int and str")        

#     def m1(self, str a):
#         print("m1 method with str")

# obj = A() 
# obj.m1("h")       
"""
*   If a class has multiple methods having same name but different in parameters, it is known as Method Overloading
*   in java when method with same name is defined and object is created and when we call method m1 using object
    then the method we satisfy the condition will be executed
*   but in python if we use same method name it will directly consider latest method avoiding previous one but 
    it will raise an error
*   if signature is different then method overloading is possible
*   in java method overloading depends upon signature of that object--method name, no. of args, type of args
    it differentiate on basis of signature and if slight change in method is observed then it will be execute
*   if all signature are same then it will be considered as method overriding    """




# to achieve method overloading in python

class Calculation:

    @staticmethod       # staticmethod should be called by className only
    def addition(a=None, b=None, c=None):
        if a and b and c:
            print(a + b + c)
        elif a and b:
            print(a + b)
        elif b and c:
            print(b + c)
        elif a and c:
            print(a + c)  
        else:
            print("no values to add")

# Calculation.addition()
# Calculation.addition(a=10, b=55, c= 458)

"""
*   in python we use is static method
*   we call static method by using className
*   in one method we can achieve method overiding by applying checks like if-else condition
*   same method but different behavior according to the requirement as in java we have to add mulltiple method 
    with same name to achieve this in python single method is enough"""

class Calculation:

    @staticmethod       # staticmethod should be called by className only
    def addition(*args):
        if len(args) == 0:
            print("no values provided")
        elif len(args) == 1:
            print("add atleast 2 values")    
        elif len(args) > 1:
            # print(sum(args))          # backend sum((10,20,55))
            total = 0
            for i in args:
                if type(i) == int:
                    total += i
            print(total)
                # else:
                #     print("please pass integer value")
                #     break    
                

# Calculation.addition(10, "20",50, 60)
# ---------------------------------------------------------------------------------------------------------------

# Inheritance

# all class has default parent class--object
# class A():                # super class ---parent class--
#     def __init__(self):
#         pass
# class B(A):             #  --- child class ---derived class ---inherited class
#     pass

"""
*   accessing properties from parent / super class
*   e.g father has a bike then his son can access it or use it
*   parent/ super class cannot access properties from child/ derived class
*   parent class should be always defined before child class
*   setter
*   getter
*    """

class Teacher(object):             # by default parent class    --- object
    def set_Name(self, name):      # setter --to set instance var ---- mutator
        print("inside parent name")
        self.Name = name

    def set_Surname(self, srname):
        self.Surname = srname

    def set_salary(self, slry):
        self.Salary = slry

    def get_Name(self):           # getter --to access instance var-- accessor
        print(self.Name)

    def get_Surname(self):
        print(self.Surname)        

    def get_Salary(self):
            print(self.Salary)

    def __repr__(self):
        return f"{self.__dict__}"        


class student(): 
    def set_mark(self, marks):
        self.Marks = marks

    def get_marks(self):
        print(self.Marks)    

# t1 = Teacher()
# t1.set_Name("Shubham")
# t1.set_Surname("Bakade")
# t1.set_salary(10700)
# print(t1)            # as we have define repr method---{'Name': 'Shubham', 'Surname': 'Bakade', 'Salary': 10700}

# s1 =student()          # as no relation shown
# print(s1)              # as repr is defined in parent class
# s1.set_mark(55)
# s1.set_Name("John")    # student has no set method so it will look into its parent class-- Teacher class
# s1.set_Surname("Watson")
# print(s1.__dict__)     #using parent all will be added --{'Marks': 55, 'Name': 'John', 'Surname': 'Watson'}
# s1.get_Name()          # John --- from parent

# print(dir(s1))         # to check s1 methods 



# -------------------------------------------------------------------------------------
class A(object):
    """parent child relation"""
    def __init__(self, name):
        self.Name = name
        print("in super class",)

class B(A):
    def __init__(self, age):  # if B has constructor then it will use its own method and not A's method
        # self.Name = name
        self.Age = age
        print("in child class")

# a1 = A("harry")
## b1 = B("John")     # as B is child of A ,constructor of A will be called and we need to provide name"""
# b1 = B("john", 25)
# b1 = B(25)           
# b1.Name ="John"
# print(b1.__dict__)

# print(b1.__dict__)   #{'Name': 'john', 'Age': 25}

# print(getattr(b1, "Age"))                #IMPORTANT

# setattr(b1, "class", 3)                  #IMPORTANT
# print(b1.__dict__)

#--------------------------------------------------------------------------



class Father:
    def __init__(self, bike):
        self.Father_Bike = bike
        print("in father's init")
    
    def get_bike(self):
        print(f" father's Bike: {self.Father_Bike}")

class Son(Father):
    def __init__(self, bike, f_bike = None):
        self.sonbike = bike
        print("in Son init")
        # self.Father_Bike = f_bike   # if son and father's bike are mentioned in constructor-- DRY principle unfollow
        if f_bike:
            super().__init__(f_bike)      # by this parents properties are used in child class--calls father's constructor
        # if hasattr(s1, "Father_Bike"):

    def get_bike(self):      # overridden method
        if hasattr(self, "Father_Bike"):
            print(f"son's bike: {self.sonbike}-----father's bike: {self.Father_Bike}")
        else:
            print(f"son's bike: {self.sonbike}")    

# f1 = Father("Unicorn") 
# print(f1.__dict__)          #<__main__.Father object at 0x0000021E3F8F2340>---{} as father has method

# s1 = Son("unicorn")           # calls father constructor 
# s1 = Son( "Bullet")           # this will fail if only 1 args is passed so here comes super() class
                              # AttributeError: 'Son' object has no attribute 'Father_Bike'--declare father_bike attribute but it is against DRY 
# print(s1.__dict__)
s1 = Son( "Bullet","unicorn")
s1.get_bike()

# scenarios
# 1. father ke pass init tha, son ke pass nahi tha--- father ka init call kiya 
# 2. father ke pass init tha, son ke pass init tha --- son ka init use kiya
# 3. father ke pass init tha, son ke pass init tha --- son ka init me father ka init call kiya --- dono init
"""in separete forms"""
"""1. father ke pass init tha, son ke pass nahi tha--- father ka init call kiya"""
class Father:
    def __init__(self, car_name):
        self.Car_Name = car_name
        print("in Father's init")

    def get_Car_Name(self):
        print("father's car: ", self.Car_Name)

class Son(Father):
    pass

# s1 = Son("Honda City")          # son's object-- calls father's init
# print(s1.__dict__)              #{'Car_Name': 'Honda City'}
# s1.get_Car_Name()

"""2. father ke pass init tha, son ke pass init tha --- son ka init use kiya"""

class Father:
    def __init__(self, car_name):
        self.FCar_Name = car_name
        print("in Father's init")

    def get_Car_Name(self):
        print(f"father' car: {self.FCar_Name}")

class Son(Father):
    def __init__(self, scar_name):
        self.SonCar_Name = scar_name
        print("in Son's init")

    def get_scar_Name(self):
        print(f"Son's car: {self.SonCar_Name}")    

# s1 = Son("Mahindra Thar")          # son's object-- calls father's init
# print(s1.__dict__) 
# s1.get_scar_Name()

# f1 = Father("Honda City")
# f1.get_Car_Name()

"""3. father ke pass init tha, son ke pass init tha --- son ka init me father ka init call kiya --- dono init"""
class Father:
    def __init__(self, car_name):
        self.FCar_Name = car_name
        print("in Father's init")

    def get_Car_Name(self):
        print(f"father' car: {self.FCar_Name}")

class Son(Father):
    def __init__(self, scar_name, Fcar=None):    # default value if only 1 args is provided
        self.SonCar_Name = scar_name
        print("in Son's init")
        # self.FCar_Name = Fcar      # voilate DRY principle
        if Fcar:
            super().__init__(Fcar)       # raise error as 2 args required so use if condition

    def get_scar_Name(self):
        # print(f"Son's car: {self.SonCar_Name}------{self.FCar_Name}")    # x x x x if DRY voilets
        if hasattr(self, "Fcar"):
            print(f"Son's car: {self.SonCar_Name}------{self.FCar_Name}")  
        else:
            print(f"Son's car: {self.SonCar_Name}")

# s1 = Son("Mahindra Thar", "Honda City")          # son's object-- calls father's init
# print(s1.__dict__) 
# s1.get_scar_Name()


class C:
    def m1(self):
        print("in C - m1")

class D(C):
    def m1(self):
        super().m1()             #calls D m1
        print("in D - m1")

    def m2(self):
        print("in D - m2")

    def m3(self):
        super().m1()    
# d1 = D()
# d1.m1()
# d1.m2()
# d1.m3()


# levels in inheritance
# ---Single level 
# ---Multilevel
# ---Multiple level
# ---Hierarchical
# ---hybrid

# single level 
#  B is a child of A (parent class)
# bydefault A's parent class is object
class A(object):
    pass
class B(A):
    pass

# multilevel inheritance

class A(object):  # base clase
    def m1(self):
        print("A - m1")

class B(A):       # child of A class
    def m1(self):
        print("B - m1")

class C(B):       # child of B class
    def m1(self):
        print("C - m1")

class D(C):       # child of C class
    pass
    # def m1(self):
    #     print("D - m1")

# d1 = D()  
# d1.m1()  

"""MRO - method resolution order
the order in which it looks for methods if it doesn't have"""

# print(D.mro())     #[<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
# print(D.__mro__)   #(<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

# multiple Inheritance
# --two parents and one child 
"""c3 linearisation algorithm --
when having multipple parents then child will always look method in a parent which is present to the left side of it (Child)
left most parent is prefered first then right one
if it finds method in left parent then it wont look in right parent """

class Father:
    def height(self, height):
        self.FHeight = height
        
    def complexion(self, complex):      #
        self.FComplexion = complex

class Mother:
    def complexion(self, complex):
        self.MComplexion = complex

class Child(Father, Mother):            #or Child(Mother, Father)
    pass

# c1 = Child() 
# c1.height("6")
# c1.complexion("whiteish")
# print(c1.__dict__)

# Hierarchical
"""
* opposite of multiple level
* one parent two child
"""
class A:
    # pass
    def m1(self):
        print("in A - m1")

class B(A):
    def m1(self):
        print("in B - m1")

class C(A):
    pass
    # def m1(self):
    #     print("in C - m1") 

# c1 = C()
# c1.m1()
# b1 = B()
# b1.m1()


# Hybrid
"""
* mix of all levels i.e single, multi, multiple, heirarchical
"""
class A:
    def m1(self):
        print("A --- m1")
        super().m1()

class B:
    def m1(self):
        print("B --- m1")
        super().m1()

class C:
    def m1(self):
        print("C --- m1")

class X(A, B):
    def m1(self):
        print("X --- m1")
        super().m1()

class Y(B, C):
    def m1(self):
        print("Y --- m1")
        super().m1()

class Z(X, Y, C):
    def m1(self):
        print("Z --- m1")
        super().m1()

# z1 = Z()
# z1.m1()

# Z --- m1    #seq
# X --- m1
# A --- m1
# Y --- m1
# B --- m1
# C --- m1

# OR

class A:
    def m1(self):
        super().m1()
        print("A --- m1")

class B:
    def m1(self):
        super().m1()
        print("B --- m1")

class C:
    def m1(self):
        print("C --- m1")

class X(A, B):
    def m1(self):
        super().m1()
        print("X --- m1")

class Y(B, C):
    def m1(self):
        super().m1()
        print("Y --- m1")

class Z(X, Y, C):
    def m1(self):
        super().m1()
        print("Z --- m1")

# z1 = Z()
# z1.m1()
# print(Z.mro())   #[<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.A'>,
                #     <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

# C --- m1
# B --- m1
# Y --- m1
# A --- m1
# X --- m1
# Z --- m1                



# Encapsulation --- read geeksforgeeks


"""Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
* It describes the idea of wrapping data and the methods that work on data within one unit. 
* This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
* To prevent accidental change, an object’s variable can only be changed by an object’s method.
* A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.  """

# class R:
#     a = 10
#     print(a)

# R.a = 20   # can access and modify static var
# print(R.a)

# -Access Specifiers
# it is a concept which is utilized in encapsulation
# it defines the scope to which a user can have access to the data(variable and method)

# types of variable an access specifier uses
# ----Public variable
# ----Protected variable ----: _varname --- starts with single underscore   --- can be protected method
# ----Private variable/ stricktly protected ---: __varname --- starts with double underscore

# public variable -- same or is instance var -- can be accessed
# -- within class
# ---outside class
# ---in child class ---call method in child class(instance method)

class X:
    def __init__(self):
        self.Brand = "Apple"
        # print("in base init")

    def m1(self):                  # instance var 
        print(self.Brand)   
        self.Brand = "HTC"         # can access and modify inside instance method
        
class Y(X):
    def __init__(self):
        # print("inside dervied init")
        super().__init__()        # calls init of base-----access 
        print(self.Brand)

    # def m1(self):
    #     print("D --- m1", self.Brand)

    def m2(self):
        # X.m1(self)             # works same as super() but need to provide self args
        # self.Brand = "Haier"    # can access and modify method also
        self.m1()                  # call parent m1 if its m1 not there 
        print(self.Brand) 

# x1 = X("Samsung", "s22") 
# x1.Brand = "Apple"  # can access and modify outside class
# x1.m1()              # public method can access outside 
# print(x1.__dict__)   #{'Brand': 'HTC', 'Mobile_Name': 's22'}

# y1 =Y()
# y1("Nokia", 6600)        #AttributeError:  ---- calls parent
# print(y1.__dict__)
# y1.m2()


# Protected variable ---
# can access modify just like public variable
# _Varname -- single underscore---special varcan be accessed same as public variable 
# _varname raha toh pata chalega ki protected hai
# protected variable should not be accessed outside class and if want to access then access via calling method 
# so that accidental modification can be prevented

# can be accessed same as Public var
# -- within class
# ---outside class
# ---in child/ derived class ---call method in child class(instance method)
class Base:
    def __init__(self):
        print("in base init")
        self._a = "XYZ"      # _a special var or protected var
    def _m1(self):             # can access and modify protected var
        print(self._a)   
         

# b1 = Base()   
# print(b1._a) 
# b1._a = 8                  # can access and modify
# print(b1.__dict__)         #{'_a': 8}
# b1.m1()

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("in derived init")
    def m2(self):            # protected method
        Base._m1(self)        # calls m1 of base
        
# d1 = Derived()
# print(d1._a)     #  calls base init
# d1._a = 20
# d1.m2()

# Private variable / Stricktly protected  ----: __Varname  -- starts with double underscore
# redtricted to access 

"""
* generally we cannot access private variable outside class
* by using 'Name Mangling Concept' we can access outside---: _ClassName__Varname
* within same class can be accessed and modified 
* in child class it can be accessed using Name Mangling Concept but by normal method can't access
* can create private method and that can be accessed using Name mangling concept same"""

# can be accessed 
# -- within class anywhere
# ---outside class using Name Mangling Concept
# ---in child/ derived class ---using Name Mangling Concept
class Base:
    def __init__(self):
        self.ID = 101
        self._Age = 25
        self.__Name = "Alex"       # double under score--- in backend _Base__Name
        print(self.ID, self._Age, self.__Name)

    def __m1(self):                  # access outside using name Mangling---- private method
        print(self.__Name)    
        self.__Name = "Bruno"
    

class Derived(Base):
    def __init__(self):
        super().__init__()
        print(self._Base__Name)     # using name mangling concept can be accessed but by noraml method can't access
    
    def m2(self):
        super()._Base__m1()         # privte method can be accessed using name mangling : _Base__methodname()
        # print(self.__Name)    # cannot access directly
    
# b = Base()        
# print(b.__Name)            #'Base' object has no attribute '__Name'
# print(b.__dict__)          # {'_Base__Name': 'Alex'}--- mangling concept
# print(b._Base__Name)       #  access using name mangling concept---obj._ClassName__privatevar
# b._Base__Name = "Oreo"     #  modify using name mangling concept---obj._ClassName__privatevar = new value
# b._Base__m1()

# d = Derived()
# print(d._Base__Name)    # uses relationship and class base init
# d._Base__Name = "OMG"
# print(d.__dict__)
# d.m2()



from abc import ABC, abstractmethod

class RBI(ABC):      # Abstract class-- parent ABC
    
    @abstractmethod  # cannot implement in same class
    def loan(self):
        pass
    @abstractmethod
    def Fd(self):
        pass
    @abstractmethod
    def atm(self):
        pass
    
    def main_Branch(self):          # normal method commmon to all sub class --concrete method
        print("Nagpur City")

# r1 = RBI()    # object --cannot create of abstract class 
# print(r1)     # Can't instantiate abstract class RBI with abstract methods Fd, atm, loan

"""
* abstract method --- jiske under implementation NAHI hota
* concrete method jiske under implementation HOTA hai
* abstract method cannot be implemented in same class or abstract class
* methods can be implemented in sub classes/ child class
* if concrete method present in abstract class it is common to all subclass-- can be accessed"""

class HDFC(RBI):

    def loan(self):                      # concrete method
        print("loan facility available")
    
    def Fd(self):
        print("FD at 10 % - interest")
    
    def atm(self):
        print("minimum 5 atm in the city")

# h1 = HDFC()   # type error as it is associated parent class RBI---implement abstract method in sub class
# h1.loan()
# h1.Fd()
# h1.atm()
# h1.main_Branch()    # search in parent class---common to all child class

class Car(ABC):
    pass

class TATA(Car):
    pass

class Mahindra(Car):
    pass




# Interface -- 
# like zoom,skype is an interface where people connects
# website is an user interface where user can access data stored into some database 
# application is an interface

"""
* files --- text, pdf, excel, etc"""

class Myfiles(ABC):
    
    @abstractmethod
    def Open(self):
        # print("file opened")
        pass

    @abstractmethod
    def Proccessed(self):
        pass

    @abstractmethod
    def Close(self): 
        pass   

# m1 = Myfiles() #Can't instantiate abstract class Myfiles with abstract methods Close, Open, Proccessed

class Text():

    def Open(self):
        print("Text file opened")

    def Processed(self):
        print("Text file processed")

    def Close(self): 
        print("Text file closed")

class Excel():
    def Open(self):
        print("Excel file opened")

    def Processed(self):
        print("Excel file processed")

    def Close(self): 
        print("Excel file closed")

class Pdf():
    def Open(self):
        print("Pdf file opened")

    def Processed(self):
        print("Pdf file processed")

    def Close(self): 
        print("Pdf file closed")

# class FileAccess:      # creating interface
#     user_ip = input("enter file type :")
#     print(user_ip)
#     # print(globals())      #'Text': <class '__main__.Text'>, 'Excel': <class '__main__.Excel'>, 'Pdf': <class '__main__.Pdf'>}
#     cls_Name =globals()[user_ip]       # will get className by providing key user_ip
#     print(cls_Name)
#     obj = cls_Name()
#     obj.Open()
#     obj.Processed()
#     obj.Close()

#enter file type :Text
# Text
# <class '__main__.Text'>
# Text file opened
# Text file processed
# Text file closed
