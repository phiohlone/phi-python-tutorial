def hello():
    print("Hello World")

hello()

def f(x):
    y = x**2+21.5*x+3.321
    # ** = power function
    return y

print(f(5))
print(f(5.0))

def L():
    A = []
    A.append(5.)
    A.append(6.)
    A.append(7.)
    
    print (A.pop())
    print (A.pop())
    print (A.pop())

    B = []
    B.insert(0,'Boo')
    B.insert(0,'hoo')

    for item in B:
        print(item)

L()
