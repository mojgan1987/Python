# print words starting with s
st = 'Print only the words that start with s in this sentence'
ml = st.split()
for word in ml:
    if word[0].lower() == 's':
        print(word)

# list of all numbers between 1 and 50 that are divisible by 3.
[num for num in range(1,51) if num%3 == 0]

