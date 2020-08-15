#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) N^5

b) n log n

c) 2^n

## Exercise II

'''
Where the case works: 
f + 1 breaks, f no break


take in building height and function to check if egg is broken

    assign the top floor to n
    assume the bottom floor to start is zero

    perfect floor has no status

    while the perfect floor not found:

        to minize the number of checks we will assign middle to be the average between the top floor or highest floor checked where egg breaks, and the bottom floor

        if dropped from the middle floor and the egg breaks
            perfect floor not found
            assign top floor to be a floor lower than middle
        or else if the egg doesnt brea:
            check if egg is dropped from one floor higher and breaks:
                perfect floor is found
            otherwise : 
                perfect floor is not found
                assign bottom flor value to be just above the middle value

    return middle

complexity is Ologn, using binary search method

'''
