def greet(name):
    print(f'hello, {name}!')
    greet2(name)
    print('getting ready ti say bye...')
    bye(name)


def greet2(name):
    print(f'how are you {name}?')


def bye(name):
    print('ok bye')


greet('maggi')
