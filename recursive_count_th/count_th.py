'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

base case - string has less than 2 characters
string has two characters
    increase count if match

how to get there - flug the function with less characters

return a count


'''
def count_th(word):    
    if len(word) < 2:
        return 0
    count = 0
    if word[0:2] == "th":
        count += 1
    count += count_th(word[1:])

    return count

print(count_th('thth'))