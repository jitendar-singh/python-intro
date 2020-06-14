# def hello_func(greeting, name="You"):
#     return "{}, {} Function".format(greeting, name)


# print(hello_func("Hi"))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['math','Arts']
info = {'name':'Jitendar', 'age': 22}

student_info(*courses, **info)