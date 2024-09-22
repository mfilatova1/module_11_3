from inspect import getmodule


def introspection_info(obj):
    return {
        'type':type(obj).__name__,
        'attributes': obj.__dict__,
        'methods': dir(obj),
        'module': getmodule(obj)
    }


class MyClass:
    pass

obj1 = MyClass()
class_info = introspection_info(obj1)
print(class_info)




