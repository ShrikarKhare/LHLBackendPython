from collections import Counter, defaultdict, deque, namedtuple
#1 print empty set
# new_empty_set = set()
# print(new_empty_set)

#2 print non-empty set
new_non_empty_set = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6}
# print(new_non_empty_set)
# 3 Iterate over the set and print 
# for i in new_non_empty_set:
#     print(i)
# 4 Add a single item to set
# new_non_empty_set.add(24)
# print(new_non_empty_set)

#5 Add multiple items to list
# new_non_empty_set.update([24,46,212])
# print(new_non_empty_set)

#6 Remove item from a set if present in set
# new_non_empty_set.remove(46)
# print(new_non_empty_set)
#7 find min and max of a set
# print(min(new_non_empty_set), max(new_non_empty_set))
#8 print length of set
# print(len(new_non_empty_set))
#9 
# x = {'this', 'is', 'one','set'}
# y = {'this', 'is', 'another','set'}
# print(x.intersection(y))
#10
# print(x.union(y))
#11
# print(x.difference(y))

#Collections
sentence = "For each word in the sentence count the occurence".split()
sentence = set(sentence)
# #12 counter
# print(Counter(sentence))
#13 most common
# print(Counter(sentence).most_common)

#14 defaultdict counter
# newsentence = defaultdict(str)
# newsentence = sentence
# print(Counter(sentence))
# sentence = sum(dict.values)
# print(sentence)
# print(defaultdict(sentence))

#15 
# newlist = deque(new_non_empty_set)
# print(newlist)

#16 append 100
# newlist.append(100)
# print(newlist)

#17 remove right end deque
# newlist.pop()
# print(newlist)
#18 remove left end deque
# newlist.popleft()
# print(newlist)
#19 delete all elements
# newlist.clear()
# print(newlist)

#20 named tuple 
# fullname = namedtuple("fullname", "name, surname")
# myname = fullname("shrikar", "khare")
#21 print name surname
# print(myname.name , myname.surname)

#22 try except block
# randomwords = ['this', 'basic', 'squash', 'pumpernickel', 'coyote', 'chicken', 1 ,'blue']
# for i in randomwords:
#     try:
#         print(i.upper())
#     except:
#         print(str(i) + " is not a string")
        
# print('done trying')


#23 Star Wars

def relation_to_luke(text):
    _dict = {}
    _dict["Darth Vader"] = "father"
    _dict["Leia"] = "sister"
    _dict["Han"] = "brother in law"
    _dict["R2D2"] = "droid"

    try:
        print(f"Luke, I am your {_dict[text]}")
    except KeyError:
        print(text + ' is not in the relation with Luke')

relation_to_luke("Darth Vader")
relation_to_luke("Leia")
relation_to_luke("Han")
relation_to_luke("R2D2")
relation_to_luke("aaaa")