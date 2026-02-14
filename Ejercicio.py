#Predice el resultado de los siguientes códigos y después compruébalos
#Strings
#1.
fruit = 'banana'
l = len(fruit)
print(l)

#2.
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

#3.
fruit = 'banana'
for letter in fruit:
    print(letter)

#4.
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

#5.
word = 'banana'
new_word = word.upper()
print(new_word)

#6.
word = 'banana'
index = word.find('a')
print(index)

#Listas
#7.
cheeses = ['Cheddar', 'Edam', 'Gouda']
for cheese in cheeses:
    print(cheese)

#8.
numbers = [3, 5, 2, 1, 6]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

#9.
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

#10.
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)

#11.
t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)

#12.
s = 'pining for the fjords'
t = s.split()
print(t)

#Diccionarios
#13.
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp['two'])

#14.
eng2sp = dict()
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'
print(eng2sp)

#15.
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
for clave in eng2sp:
    print(clave, eng2sp[clave])

#16.
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
vals = eng2sp.values()
print(vals)

#17.
s = 'brontosaurus'
d = dict()
for c in s:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
print(d)