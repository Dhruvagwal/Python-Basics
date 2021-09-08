# num_list = ["1","2","3","4"]
# print(num_list[0])

# dict = {0:"1",1:"2",2:"3"}
# dict = {"cv":"computer vision","dp":"deep learning","ml":"machine learning"}
# print(dict[0])

# isValid = "computer vision" in dict.values()
# print(isValid) 

import time

sentence  = """I mentioned earlier that a dictionary is implemented using a hashtable and that means that
the keys have to be hashable.
A hash is a function that takes a value (of any kind) and returns an integer. Dictionaries
use these integers, called hash values, to store and look up key-value pairs.
This system works fine if the keys are immutable. But if the keys are mutable, like lists,
bad things happen. For example, when you create a key-value pair, Python hashes the key
and stores it in the corresponding location. If you modify the key and then hash it again, it
would go to a different location. In that case you might have two entries for the same key,
or you might not be able to find a key. Either way, the dictionary wouldn’t work correctly.
That’s why keys have to be hashable, and why mutable types like lists aren’t. The simplest
way to get around this limitation is to use tuples, which we will see in the next chapter.
Since dictionaries are mutable, they can’t be used as keys, but they can be used as values.
"""

# {"you":3,"are":3,"awesome":1,"genius":1,"beautiful":1}

list_of_words = sentence.split()
bag_of_word = {}

for i in list_of_words:
    if i in bag_of_word:
        bag_of_word[i] += 1

    else:
        bag_of_word[i] = 1

# print(bag_of_word)

start = time.time()
for key, value in bag_of_word.items():
    if value > 1:
        time.sleep(0.1)

end = time.time()
print(end-start)


# {3:["you", "are"],1:["awesome", "genius","beutiful"]}

# for i in list_of_words:
#     if i in bag_of_word.values():

index_to_word = {} 

start = time.time()
for key,value in bag_of_word.items():

    if value in index_to_word:
        index_to_word[value].append(key)
    else:
        index_to_word[value] = [key]

for i in index_to_word.keys():
    if i>1:
        time.sleep(0.1)
        # print(index_to_word[i])
end = time.time()
print(end-start)

# frame per second