def set_color(func):
    def color_red():
        return "\033[31;1m%s\033[0m" % func()
    return color_red

@set_color    # say_hi = set_color(say_hi)
def say_hi():
    return 'hello world!'

@set_color    # hello = set_color(hello)
def hello():
    return 'how are you?'

if __name__ == '__main__':
    print(say_hi())
    print(hello())

