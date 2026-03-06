# 1. Use map() with a lambda to add 5 to every element of the following nested list [[1,2], [3,4], [5,6]]

l=[[1,2], [3,4], [5,6]]
print(list(map(lambda y:list(map(lambda x:x+5, y)), l)))

# 2. Given a dictionary: d = {"apple": 100, "banana":40, "cherry": 150}. Use filter() to keep only the keys whose values are greater than 50.

d={"apple":100, "banana":40, "cherry":150}

keys=d.keys()
print(list(filter(lambda x:d[x]>50,keys)))
print(list(filter(lambda x:d[x]>50,d)))

# 3. Use functools.reduce() with a lambda to find the largest number from a given list dynamically.
from functools import reduce
#l=[10,32]
l=[10,32,51]
print(reduce(lambda x,y:x if x>y else y, l))

# 4. What happens if the lambda passes to reduce() accepts only one parameter or three parameters? Explain the output or error.
'''reduce() function always expects a function with 2 parameters. '''

# 5. Use map() on a string to convert each character into its ACSII value (using ord()). Print the result list.
s='Jyothi'
print(list(map(lambda x:ord(x),s)))

# 6. Use filter() to remove all vowels from a string and print the final string.
s='Jyothi'
v='aeiouAEIOU'
print(list(filter(lambda x:x not in v,s)))
print(list(filter(lambda x:x not in v, 'Goal Hustlers')))
print(list(filter(lambda x:x not in v, 'Google')))

# 7. Use reduce() to concatenate a list of characters into a single string.
# Example input: ['p','y','t','h','o','n']

l=['j','y','o','t','h','i']
print(reduce(lambda x,y:x+y, l))
print(reduce(lambda x,y:x+y,['G','O','O','G','L','E']))

# 8. Given a list of integers, use map() with id() to print the memory address of each element.
# Example: [10,350,10,350,20] - explain why some address repeat.

l=[10,350,10,350,20]
print(list(map(lambda x:id(x),l)))
l=[32,12,2,12,32,1]
print(list(map(lambda x:id(x),l)))
print(list(map(lambda x:id(x),[1,34,4,1])))

# 9. Explain the difference between:
'''map(str, [1,2,3])
map(lambda x:str(x), [1,2,3])
Which one is faster and why? '''
# map(str,list) -- directly uses built-in function -- It is faster. Bcz, No lambda overhead, Direct function call.
# map(lambda x: str(x)) -- creates extra lambda function

# 10. Given a list of numbers:
''' [5,10,15,20,25,30]
Perform the following in a single pipeline:
    . Use map() to square each number 
    . Use filter() to keep only numbers divisible by 5 
    . Use reduce() to calculate the sum of remaining numbers '''

l=[5,10,15,20,25,30]
'''print(reduce(lambda x,y:x+y,l))
print(list(filter(lambda x:x%5==0,l)))
print(list(map(lambda x:x**2,l))) '''
print(reduce(lambda x,y:x+y,(filter(lambda x:x%5==0,(map(lambda x:x**2,l))))))

# 11. Explain the difference between map(), filter(), and reduce() in python.
''' . What does each function return?
    . What should you prefer lambda function over normal functions?  '''
    
# map() -- Apply a function to every element in an iterable(convert to list).
# filter() -- Select elements based on a condition.
# reduce() -- Combine all elements into one single value.
'''
1. map() -- iterable object ni return chestundhi.
         -- result of applying the function to each element.
2. filter() -- iterable object ni return chestundhi.
            -- Which contains only the elements that satisfy the condition.
3. reduce() -- Single value ni return chestundhi.
. Lambda functions are preferred when the functions is small, simple, and used only once, especially with functions like map(), filter(), and reduce(), to make the code shorter and more consice
'''

# 12. Give two lists:
'''a=[1,2,3,4] b=[10,20,30,40]
Use map() with a lambda to create a new list containing the  sum of corresponding elements.
What happens if the lists are of unequal length? '''

a=[1,2,3,4]
b=[10,20,30,40]
print(list(map(lambda x,y:x+y, a,b)))
c=[10,2,4]
d=[1,2,4,6,7]
print(list(map(lambda x,y:x+y,c,d)))
# map() stops when shortest list ends.

# 13. Given a list:
'''
nums=[12,15,7,18,20,21,25]
use filter() and lambda to keep numbers that are divisible by 3 OR divisible by 5 but NOT divisible by both.
Explain how the logical condition works. '''

nums=[12,15,7,18,20,21,25]
print(list(filter(lambda x:(x%3==0 or x%5==0) is not (x%3==0 and x%5==0), nums)))

# 14. Given a list:
''' nums = [1,2,3,4]
Use reduce() with a lambda to compute the sum, but start with an initial value of 10.
Explain how the initial value affects the reduction process.
'''
nums=[1,2,3,4]
print(reduce(lambda x,y:x+y,nums,10))

# 15. Consider the code below:
''' nums = [[1,2],[3,4],[5,6]] result=list(map(lambda x:x.append(10),nums))
print("Result:", result) print("Nums: ",nums)
Questions
    . What will be the output of result?
    . What will be the output of nums?
    . What does map() behave this way with list.append()?
    . What can you modify the lambda so that nums is not changed?
'''
nums=[[1,2],[3,4],[5,6]]
result=list(map(lambda x:x.append(10),nums))
print("Result:", result)
print("Nums: ",nums)
'''
1. result = [None, None, None, None] -- bcz, append() does not return the modified list. It only changes the list internally.
2. Nums = [[1,2,10],[3,4,10],[5,6,10]]
3. map() stores the return value of the function
    append() returns None 
    But it modifies the list in-place
4. x+[10] creates a new list instead of modifying the original list.
   --To avoid modifying nums, replace x.append(10) with x+[10] so that a new list is created instead of changing the original list.
'''