heights = [1.82,1.75,1.68,1.76,1.5]
#1
# for i in heights:
#     print(i)
#2
# for i in heights:
#     if(i > 1.75):
#         print(i)
#3
# for i in heights:
#     if i == 1.68:
#         print(i)
#         break
#     else:
#         print(i) 
#4
# for i in heights:
#     if i == 1.68:
#         continue
#     else:
#         print(i) 
#5
# for i in heights:
#     if i > 1.75:
#         print("high")
#     elif i < 1.75 and i > 1.68:
#         print("medium")
#     else:
#         print("small")

#6
# i = 0
# while i < 5:
#     print(i)
#     i+=1
#7
# i = 0
# while i < 15:
#     if i % 2 == 0:
#         print(i)
#     i+=1

#8
# i = 0
# while i < 15:
#     if i > 4 :
#         print(i)
#     i+=1

actors = [
    "Nathan Fillion",
    "Gina Torres",
    "Alan Tudyk",
    "Morena Baccarin",
    "Adam Baldwin",
    "Jewel Staite",
    "Sean Maher",
    "Summer Glau",
    "Ron Glass"
]

roles = [
    "Captain Malcolm Reynolds",
    "Zoe Washburn",
    "Hoban Washburn",
    "Inara Serra",
    "Jayne Cobb",
    "Kaylee Frye",
    "Dr. Simon Tam",
    "River Tam",
    "Derrial Book"
]
print('Featuring:')
print('===========')
for i in range(0, len(actors)):
    print(actors[i] + " as " + roles[i])
