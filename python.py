#try and except block will try to do something and if it fails it will do something else

#while loop is a loop that will keep running until a condition is true

#basic example of while loop

#i = 0
#while i < 10:
#    print(i)
#    i += 1
    # break #breaks out of the loop
    # continue #skips the current iteration of the loop




#for loops is a control flow statement for specifying iteration, which allows code to be executed repeatedly.
#iterate means how many times you want to run the loop
#range allows to iterarte by a certain value
#use the for loop when you know how many times you want to iterate
#use the while loop when you don't know how many times you want to iterate
"""
for i in range(5):
    print(i)

for i in range(1, 5): #start from 1 and end at 5
    print(i)

for i in range(1, 10, 2): #start from 1 and end at 10 and increment by 2
    print(i)        
"""
# [] List is a collection of elements in a particular order
# () Tuple is a collection of elements in a particular order
# {} Dictionary is a collection of key value pairs

#list example [1, 2, 3, 4, 5] ,[1, 'a', 2.0, True], [1, [2, 3], 4]


#list below

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

#another one 
numbers = [1, 2, 3, 4, 5]
print(numbers[0]) #prints 1

#another one
numbers = [1, 2, 3, 4, 5]
numbers.append(6) #adds 6 to the end of the list
print(numbers)


#ethra ind adhinu anusarichu cheyyan we use len function

fruits =[ 'apple', 'banana', 'cherry']

for i in range(len(fruits)):
    print(fruits[i])

    ````
    #what i am gonna do is take the names email and all
#names = []
#ages = []
#emails = []



#name = input("Enter your name: ")
#age =input("Enter your age: ")
#email = input(" email: ")

#names.append(name)
#ages.append(age)
#emails.append(email)

#print(names,ages,emails)

#the above code is not efficient because we have to create a new list for each new contact

#instead we can use a dictionary to store all the information for each contact

people =[]

d ={}
#d['name'] = 'john'  #key value pair #we can add like this also