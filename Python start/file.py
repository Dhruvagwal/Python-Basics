# w - write
# r = read
# a - append
# file_txt = open('data.txt','a')

# text = file_txt.write(str(32))

# file_txt.close()


# file_txt.write("new data")

import os
# path = os.path.abspath('data.txt')


# print(path)

# exists = os.path.exists("./data/car/lambo/huracan/gtr468")
# if not exists:
#     os.mkdir("./data/car/lambo/huracan/gtr468i")

# dirs = os.listdir('./')

# print(dirs)

# def walk(dirname):
#     dirs = os.listdir(dirname)
#     for i in dirs:
#         path = os.path.join(dirname,i)
#         if os.path.isfile(path):
#             print(path)
# walk('./')

# import dbm
# db = dbm.open('captions', 'c')
# db['cleese.png'] = 'Photo of John Cleese.'
# print(db['cleese.png'])

# import pickle
# list = [1,2,3,4,5,6]

# file = open('pickle.p','w')
# pickle.dump(str(list),file)
# file.close()

# pickle.load('pickle.p')

# cmd = 'mkdir data'
# fp = os.popen(cmd)
# res = fp.read()
# fp.close()
# print(res)


import sum
print(sum.sum(5,5))
