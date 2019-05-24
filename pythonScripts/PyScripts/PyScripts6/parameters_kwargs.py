def get_kwargs(**kwargs): # **表示kwargs是个字典
    print(kwargs)

def get_age(name, age):
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    get_kwargs()
    get_kwargs(name='bob', gender='male', age=25)
    info = {'name': 'bob', 'age': 25}
    # get_age(*info)  分解出来了'name'和'age'
    get_age(**info)  # name='bob', age=25
