list = ["dhruv","aggarwal","car"]
# dict = {}

import time

# list[0]

# tuple1 = ("dhruv","aggrwal","car","lambo")
# tuple2 = ("A",)

# name, cast = list

# print(tuple[0])

# print(type(tuple))
# print(tuple[0:2])

# tuple3 = tuple2 + tuple1
# print(tuple3)

tuple1 = (1,2,5)
tuple2 = (0,5,4)
# print(tuple1<tuple2)

# tuple = (4,) + tuple[1:]
# print(tuple)

# a,b = list

# email = "dhruvagwal@gmail.com"
# email_split = email.split("@")

# email_header, domain = email_split
# print(email_header)

# def print_2():
#     return ["dhruv", "aggarwal"]


# name, cast  = print_2()
# print(name)


# def exponent(*params):
#     res = params[0]
#     for i in params[1:]:
#         res = res**i

#     return res

# res = exponent(3,3,3)
# print(res)

# list1=[1,2,3,4,10]
# list2=[5,6,7,8,9]

# start = time.time()

# for num1, num2 in zip(list1,list2):
#     print(num1, num2)

# zip_data = zip(list1,list2)
# print(list(zip_data))

# end = time.time()
# print(end-start)


# start = time.time()
# for i in range(len(list1)):
#     print(list1[i], list2[i])

# end = time.time()
# print(end-start)


d = {'a':0, 'b':1, 'c':2}

# for key, value in d.items():
#     print(key)


items = d.items()
new_d = dict(items)
print(new_d)