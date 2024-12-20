my_list = [2,3,4]
my_tuple = (2,3,4)

print(type(my_list))
print(type(my_tuple))

my_list[0] = 2
print(my_list)
# my_tuple[0] = 2 | desteklenmez.

my_list.append(2)

# tuplelarda count ve index metotları vardır.

my_tuple2 = tuple([1,2,5]) # listeyi tuple yapma
print(my_tuple2)

my_list2 = list((1,22,3)) # tupleyi list yapma.
print(my_list2)