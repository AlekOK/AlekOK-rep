# 1. import ZenPython
# import this
# zen = '''Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!'''
# # 1.a Print zen 
# print(zen)
# # Find amount of words "better"
# b_word = zen.find("better")
# # Find print amount of words "never"
# n_word = zen.find("never")
# # Find print amount of words "is"
# i_word = zen.find("is")
# #Print result
# print(b_word, n_word, i_word)

# #1.b all in upper
# zen_in_upper = zen.upper()
# print(zen_in_upper)

# #1.c change "i" to "&"
# zen_change = zen.replace("i", "&") 
# print(zen_change)
###############################################################            
# #2. Task with number (my number is 1234)
# #2.a multiplication all digits of my number
# my_number = 9215

# first_number = my_number //1000
# second_number = my_number % 1000//100
# third_number = my_number % 100 //10 
# fourth_number = my_number % 10
# print(first_number, second_number, third_number, fourth_number)
# result_of_multiplication = first_number * second_number * third_number * fourth_number
# print(result_of_multiplication)

# #2.b Reverse my number
# list_numbers = [first_number, second_number, third_number, fourth_number]
# print(list_numbers[3], list_numbers[2], list_numbers[1], list_numbers[0])

# #2.c sort the number
# sorted_number = sorted(list_numbers)
# print(sorted_number)
##################################################################
# # change imutables
# first_imut = 3
# second_imut = 8
# first_imut, second_imut = 8, 3
# print("{} {}".format(first_imut, second_imut))
   