# in Python here is three typesof datasets
    # list immutable
    # dictionary mutable
    # tuple mutable

name_list = ["shilpa", "javeriya","prajwal","dhruv"]
# score_and_class_list = [[90,8],[80,85]]

# dimensions = [[[[[[90]]]]]]
# print(name_list)

# name_list[0] = "nayan"
# print(name_list)

# immutable and mutable 
# immutable 

# for i in range(0, len(name_list)):
#     name_list[i] = name_list[i]*1

# print(name_list)

# empty_list = []

# for i in empty_list:
#     print(i)
    # print("is it render")


# num_list = []
# for i in range(0,10):
    # append adds a new element to the end of a list
    # num_list.append(i)

# num_list.append("this is last element")
# print(num_list)


# t1 = [1,2,3]
# t2 = [4,5,6]

# t1.extend(t2) # t1 = t1 + t2

# t = ['d', 'c', 'e', 'b', 'a']
# sort 
# t.sort()
# print(t)


# total = 0
# for i in num_list:
#     total += i # total = total + i

# print(sum(num_list))


# print("Dhruv".isspace())

# list_digit = ["a","A","shilpa","JAVERIYA"]

# for i in list_digit:
#     if not i.isupper():
#         list_digit.remove(i)

# print(list_digit)

# string = "this is a string without a space"
# list_digit = string.split()

# list_digit = " ".join(list_digit)
# list_digit = list(string)

# for i in list_digit:
#     if i.isspace():
#         list_digit.remove(i)

# print(list_digit)

# a = "apple"
# b = "banana"

# print(a is b)

a = [1,2,3,4]
# b = [1,2,3,5]

# def check_list(list1, list2):
#     if len(list2) != len(list1):
#         return False
#     else:
#         for i in range(0,len(list1)):
#             if list2[i] == list1[i]:
#                 pass
#             else:
#                 return False
#         return True



# print(check_list(a,b))



b = a
b[0] = 45
print(a)