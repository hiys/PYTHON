class A:
    pass

if __name__ == '__main__':
    adict = {'name': 'bob', 'age': 25, 'genda': 'male'}
    a = A()
    a.__dict__.update(adict)
    print(a.name, a.age, a.genda)
