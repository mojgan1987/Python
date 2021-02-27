# https://app.codility.com/programmers/task/palindromes/
# Arsenicum 2018
# NOT WORKING

def solution(S):
    # write your code in Python 3.6
    # length 600,000

    # for each word, if the reverse is inside add

    words = S.split(' ')
    no_space = S.replace(' ', '')

    print(no_space)

    reversable = []
    end = []
    for word in words:
        if word[::-1] in words:
            reversable.append(word)
        if len(reversable) != 0:
            for w in reversable:
                print(w, ' ')
        print(f'word={word}, revrese= {word[::-1]}')
        if word[::-1] in no_space:
            reversable.append(word)
            end.append(word[::-1])
            print(f'accepted: {reversable}')


    if len(reversable) == 0:
        return 'No'
    else:
        output = ''
        for word in reversable:
            output+=word
            # output+=' '
        print(output)
        print(end)
        return output

