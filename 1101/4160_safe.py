""" 4160 - Safe """
print(sum([i if i < 13 else 26-i for i in map(lambda i: abs(ord(i[0])-ord(i[1])), \
zip(list(input()), list(input())))]))
# # More readability version
# lst = zip(list(input()), list(input())) #Convert each string to list and zip it together.
# lst = map(lambda i: abs(ord(i[0])-ord(i[1])), lst) #Convert to distance between character.
# cnt = 0
# for i in lst:
#     if i < 13: #If distance is less than 13. Add the distance to cnt.
#         cnt += 1
#     else: #If not minus the distace with 26 to get backward distance.
#         cnt += 26 - i
# print(cnt) #Finally print the result out.
