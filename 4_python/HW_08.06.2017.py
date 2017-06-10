dict = {'first_name': 'Yurii',
        'last_name': 'Khomych',
        'email': 'yuriykhomich@gmail.com',
        'age': 29,
        'hight': 175
        }
list = []

for key, value in dict.items():
    if type(value) == str and len(value) > 5 and 'a' in value:
       list.append(value)
    elif type(value) == int and value in range(25,40):
        list.append(value)


for element in list:
    if type(element) == str and ('m' in element or 'n' in element):
        list.remove(element)
    elif type(element) == int:
        str(element)

list.extend((1,2,3,4,5))
list.sort(reverse=True)
print(list)
new_string = ''
for element in list:
    new_string += str(element) + ','
    new_string.remove()
print(new_string)

new_string = new_string.split(',')
print(new_string)