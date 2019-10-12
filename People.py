import person

Wen = person.person()
Wen.setName("Wen")
Wen.setAge(567)
Wen.getInfo()

test = person.stack()
print(test.isEmpty())
print(test.getSize())
test.push(1)
print(test.isEmpty())
print(test.getSize())
print(test.pop())

