#Exercise 1 calculate the multiplication and sum of two numbers
number1 = 40
number2 = 30
answer = (number1*number2) if (number1*number2) > 1000 else (number1+number2)

print(answer)

#Exercise 2 Print the sum of the current number and the previous number

for i in range(1, 10):
    print("Current Number " + str(i) + " Previous Number " + str(i-1) + " Sum: " + str(i+i-1))

#Exercise 3 Print characters from a string that are present at an even index number

stringinput = input('Enter a word ')
word = stringinput
for i in word[::2]:
    print(i)

#Exercise 4: Remove first n characters from a string
def remove_chars(word, slicesize):
    print(word[slicesize:])

remove_chars("pynative", 4)

#Exercise 5: Check if the first and last number of a list is the same
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def first_and_last_are_same(list1):
    return list1[0] == list1[len(list1)-1]

print(first_and_last_are_same(numbers_x))
print(first_and_last_are_same(numbers_y))

#Exercise 6: Display numbers divisible by 5 from a list
givenlist = [10, 20, 33, 46, 55]
numbers = [12, 34,10, 20, 33, 46, 55, 1, 4, 4, 67, 37, 9, 0, 81]
def return_if_divisble_by_five(arr):
    # return print([number for number in numbers if number % 5 == 0])
    #  figure this out ^ 
    for i in arr:
        if i % 5 == 0 :
            print(i)
        

return_if_divisble_by_five(givenlist)

#Exercise 7: Return the count of a given substring from a string

def count_how_many(sentence, substring):
    counter = sentence.count(substring)
    return counter

print(count_how_many("Emma is good developer. Emma is a writer", "Emma"))

#Exercise 8: Print the following pattern

def print_pattern():
    for i in range(1,6):
        print( str(i) * i )

print_pattern()

#Exercise 9: 
def number_is_pallindrome(number):
    if str(number)[::-1] == str(number):
        print('Yes, given number is palindrome number')
    else:
        print("No, given number is not palindrome number")

number_is_pallindrome(121)

#Exercise 10: Create a new list from a two list using the following condition
# from list 1 append all values that are odd and from list 2 all that are even
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
def create_merged_list(list1,list2):
    list3 = []
    if len(list1) == len(list2):
        for i in range(0,len(list1)):
            list1val = list1[i]
            list2val = list2[i]
            if list1val % 2 == 1:
                    list3.append(list1[i])
            if list2val % 2 == 0:
                    list3.append(list2[i])
    # list3 = []
    # for i in list1:
    #     if i % 2 == 1:
    #         list3.append(i)
    # for j in list2:
    #     if j % 2 == 0:
    #         list3.append(j)
    
    return list3
    # return list3
print(create_merged_list(list1,list2))