#1 
# def first_and_last(first,last):
#     return "Hello,"+first + " " + last +"."
# print(first_and_last("Marianne", "Smythe"))

#2
# def two_num_sum(num1, num2):
#     return "The sum of " + str(num1) + " and " + str(num2) + " is " + str(num1+num2)
# print(two_num_sum(2,3))

#3
# numlist = [1,2,3,62,41,73,18,27,12,15]
# def sum_all(list):
#     counter = 0
#     for i in list:
#         counter+= i
#     return counter
# print(sum_all(numlist))

#4
# def reverse_string(string):
#     return string[::-1]
# print(reverse_string('1234abcd'))

#5
# def is_in_range(number,range):
#     return number >= range[0] and number <= range[1]
# print(is_in_range(5, (0,10)))

#6
def return_newname(name):
    return 'John' if name != 'John' else 'Sam'
johnsname = 'John'
samsname = return_newname(johnsname)
print(samsname)