# REMINDER: Only do one challenge at a time! Save and test after every one.

# Challenge 0: Remember, what's the first thing you should add to any Python
# file you are working with?
# (Answer: add a "print", to make sure you are editing the right file!)
print('python time')

print('Challenge 1 -------------')
# Challenge 1:
# 1. Create 3 variables. Store in them:
#   - your name
#   - your favorite color
#   - how many hours of sleep you got last night
# 2. Print out all 3 values using "print".

a = 'SUsana'
b = 'blue'
c = '8'

print(a + b + c)

# my_name = 'Susana'
# favorite_color = 'blue'
# sleep = '8'
# myself = my_name + favorite_color + sleep
# print(myself)




print('Challenge 2 -------------')
# Challenge 2:
# Create a list of your favorite book authors.
# Put it into a variable called "authors_list".

Susana_list = [
    'Poe',
    'Galdos',
    'Benny'
]
print(Susana_list)



# authors_list = [
#     'Poe', 
#     'Galdos', 
#     'Dickens',
# ] 
# print(authors_list)





print('Challenge 3 -------------')
# Challenge 3:
# Write an "if-statement" to check if the top author on that list is equal to
# "Douglas Adams". If it is, print "Don't panic!". Otherwise, print "Panic!"

# Hint: The very first author is accessible with authors_list[0]

x = "Douglas Adam"

if x == Susana_list[0]:
    print('Dont panic')
else:
    print('Panic')





# x = 'Douglas Adams'

# if x == authors_list[0]:
#     print('panic!')
# else:
#     print('dont panic')





print('Challenge 4 -------------')
# Challenge 4:
# 1. Uncomment the provided code. What does it do?
# 2. Using a while loop, use this as a clue to write code to "loop through"
# your favorite authors list, printing each one on a separate line, along with
# its index.

# i = 0
# print(authors_list[i])
# length = len(authors_list)
# print('There are', length,  'favorite authors')


# Challenge 4 hint: The following lines of code might be helpful, although not
# necessarily in this order or indentation:
#          i = i + 1
#          while i < length:



print('Challenge 5 -------------')
# Challenge 5:
# 1. Uncomment the provided code. What does it do?
# 2. Using this a start, create a while loop that keeps on looping until the
# user says "Stop". Have it print back whatever they say each time it loops.

# answer = None
# while answer != 'Stop':
    
# user_input = input('Stop? ')







print('-------------')
# Bonus Challenge:
# Create a chat bot!
# - Using a dictionary and a while / input loop, every time a user enters text
# check in the dictionary for a pre-set set of replies (e.g. "hi" responds with
# "hello").
# - It should exit if the person says "bye" or something similar.
# - How can you make it more robust and respond to more spelling or grammar
# differences?


