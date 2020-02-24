'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # If 'th' is not in word return 0
    if not 'th' in word:
        return 0
    # Check the first two letters, if it is 'th' increment count
    elif 'th' in word[:2]:
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])   
    # TBC
print(count_th('th'))


