#Question 1: Write a function to print “hello_USERNAME!” USERNAME is the input of the function. 
#The first line of the code has been defined as below.
def hello_name(user_name):
    print("hello_" + user_name)

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.
def first_odds():
    #I could have performed this on a range of 100, instead, with some code to check if the number was odd. 
    #I figured that this would be more efficient. 
    for counter in range(50):
        print(2*counter+1)

#Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.   
def max_num_in_list(a_list):
    #Setting the initial value, to avoid the issue of false reporting of a 'zero', in a list with negative numbers. 
    max= a_list[0]
    for items in a_list:
        #For each item, it compares it to the initial 'max' value.
        #If the item is larger than the current max, it replaces it as the new max. Otherwise, nothing happens. 
        if items>max:
            max = items
    return max


#Question 4: Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    #I could write this in one line, so I decided to do so. It's a little difficult to read, but 
    #takes up less space.
    return ((a_year % 4 ==0 and a_year %100 !=0) or (a_year % 4 ==0 and a_year %100 ==0) and (a_year % 400 == 0))


#Question 5: Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#  The return should be boolean Type.
def is_consecutive(a_list):
    #'init' exists as a storage for the previous item in the comparison.
    init = a_list[0]
    #By initializing it at the first array of the element, I avoid the issue of attempting to
    #check the prior number at a_list[0].
    for itemNumber in range(1,len(a_list)):
        if a_list[itemNumber]==init+1:
            init = a_list[itemNumber]
        else: 
            #If there is ever a single nonconsecutive number, then the sequence is not consecutive. 
            #Thus, at the first point of failure, the program will immediately return 'false'. 
            return False
        #If the program makes it to the end of the list without finding a non-consecutive number,
        #it then returns true. 
    return True
