# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

print("The original list is : " + str(test_list))

# Swap elements in String list
# using replace() + list comprehension
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]

# printing result 
print ("List after performing character swaps : " + str(res))

