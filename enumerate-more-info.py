x = ("apple", "banana", "cherry")
y = enumerate(x)

print(list(y))

"""_summary_

    Output: 
    [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
    
    enumerate(iterable, start)
    
    Parameter   Description
    iterable	An iterable object
    start	    A Number. Defining the start number of the enumerate object. Default 0

    When it comes to printing use the list keyword otherwise you are going to 
    be printing the object itself and not the content
"""

