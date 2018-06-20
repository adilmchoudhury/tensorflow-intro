import array

### review of basic programming

### variables in python

print ("--Variable in python doesn't need type declaration. you can assign any types of data to any variable")

i = 100			    # data type is implicitly set to integer
print (i)
i = 200 + 10.1		# data type is changed to float
print (i)
i = "forty"         # string data type
print (i)

print("--string is array and you can print by index starting from 0 and ending from -1")
print(i[0])

print (i[-1])


## python variable memory allocation


print ("--saving the same value into two variable will allocate the same memory")
x = 10
print (id(x))
y = 10
print (id(y))


print ("--saving the different value into two variable will allocate different memory")
x = 10
print (id(x))
y = 11
print (id(y))

print("--string in python is not changeable")

print("--python operator IS and == is not same. if line have special char then use ==")

print("-- python integer array")

a = array.array('i',(1 for i in range(0,9)))
print(a)

print(a[2])

a[2] = 100

print(a)



### input and output in python




### if else in python



### loops in python

print("-- range --")
n = 10
sum = 0
for i in range(1,n):
    sum = sum + i
print (sum)
