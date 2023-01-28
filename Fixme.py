#!/usr/bin/python3
'''
Complete each function below so that the test cases pass.
Your solutions should use the map and filter functions,
and not for loops or list comprehensions.
'''

def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.

    >>> evens(10)
    [0, 2, 4, 6, 8, 10]
    >>> evens(11)
    [0, 2, 4, 6, 8, 10]
    >>> evens(0)
    [0]
    >>> evens(1)
    [0]
    >>> evens(-1)
    []
    '''
    LC = [x for x in range(0,n + 1) if x%2 == 0]
    return LC
print("even(10)=",evens(10))
print("even(11)=",evens(11))
print("even(0)=",evens(0))
print("even(1)=",evens(1))

def threes(n):
    '''
    Returns a list of all numbers from 0 to n inclusive that contain the digit 3.

    >>> threes(2)
    []
    >>> threes(3)
    [3]
    >>> threes(10)
    [3]
    >>> threes(20)
    [3, 13]
    >>> threes(50)
    [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43]
    '''
    LC = []
    for x in range(0, n + 1):
        x = str(x)
        for int in x:
            if int == '3':
                LC += [x] 
    LCI = [eval(x) for x in LC]
    return LCI
        
print("threes(2)=",threes(2))
print("threes(10)=",threes(10))
print("threes(20)=",threes(20))
print("threes(50)=",threes(50))

def small_words(text):
    '''
    Returns a list of all words in the input text that are less than 5 characters long.

    HINT:
    Recall that text.split() converts the text variable into a list of words.

    >>> small_words('this is a simple test case')
    ['this', 'is', 'a', 'test', 'case']
    >>> small_words('really enormous words')
    []
    >>> small_words('')
    []
    >>> small_words('a big word is bad')
    ['a', 'big', 'word', 'is', 'bad']
    '''
    text_split = text.split()
    LC = [x for x in text_split if len(x)<5]
    return LC

    

print("small_words('this is a simple test case')=", small_words('this is a simple test case'))
print("small_words('really enormous words')=", small_words('really enormous words'))
print(" small_words('')=",small_words(''))

def squares(n):
    '''
    Returns a list of all square number between 1 and n inclusive.
    Recall that the nth square number is defined to be n*n.

    >>> squares(1)
    [1]
    >>> squares(2)
    [1, 4]
    >>> squares(3)
    [1, 4, 9]
    >>> squares(10)
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    '''
    LC = [x*x for x in range(1,n + 1)]
    return LC

print("squares(1)=", squares(1))
print("squares(2)=", squares(2))
print("squares(3)=", squares(3))
print("squares(10)=", squares(10))

def lengths(strings):
    '''
    Given a list of strings, returns a list of the lengths of the corresponding strings.

    >>> lengths([])
    []
    >>> lengths(['test'])
    [4]
    >>> lengths(['this','is','a','test'])
    [4, 2, 1, 4]
    '''
    LC = [len(x) for x in strings]
    return LC

print("lengths([])=", lengths([]))
print("lengths(['test'])=", lengths(['test']))
print("lengths(['this','is','a','test'])=", lengths(['this','is','a','test']))
