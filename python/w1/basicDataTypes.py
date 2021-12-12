#Numbers
#1
# num_1 = 1
# num_2 = 1.0
# total = num_1 + num_2
# print(total)
# print(type(total))

#2
# height = 180
# weight = 95
# bmi = weight / (height*height) * 10000 #10000 cause the example said no, no other reasoning

# print(bmi)

#Strings
#3
# name = 'shrikar'
# surname = 'khare'
# name_surname = name + " "  + surname
# print(name_surname)
# print(name_surname[0])
# print(name_surname.replace(" ", ""))
# print(surname*10)
# greeting = "Hello my name is " + name_surname
# print(greeting)

#Lists
#4
# empty_list = []
# heights = [10,20,30,40,50]
# print(heights)
# print(type(heights))
# print(heights[1])
# heights_2 = heights[2:len(heights)]
# print(heights_2)
# list_all = heights+heights_2
# print(list_all)
# print(type(list_all))

#Tuples
#5
# empty_tuple = ()
# empty_tuple[0] = ('this won\'t work')

#Dictionaries
#6
empty_dict = {}
heights_dict = {
    "shrikar" : "188" ,
}
heights_dict["nikkita"] = "152.4"
print(heights_dict)
print(heights_dict["shrikar"])
print(heights_dict.values())
print(heights_dict.keys())
print("shrikar" in heights_dict)