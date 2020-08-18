debug = False

'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word = '') -> int:
    if word == '':
        return 0

    if debug: print(f"word: {word}")
    try:
        if 'th' in word:
            i = word.index('th')
            w = word[i+2:]
            if debug: print(f"i={i}, w: {w}")
            return 1 + int(count_th(w))
        else:
            return 0
    except ValueError:
        return 0
