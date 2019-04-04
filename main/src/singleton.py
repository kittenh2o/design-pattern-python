from functools import wraps

class LazySingleton:
    """ Lazy initialisation """
    _instance = None

    def __new__(self, *args, **kwargs):
        if not LazySingleton._instance:
            LazySingleton._instance = super(LazySingleton, self).__new__(self, *args, **kwargs)
        return LazySingleton._instance


class MetaSingleton(type):
    _instances = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in MetaSingleton._instances.keys():
            MetaSingleton._instances[cls] = super().__call__(*args, **kwargs)
        return MetaSingleton._instances[cls]


# A singleton decorator
def singleton(cls):
    _instances = dict()
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in _instances.keys():
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return wrapper

# class decorator
class SingletonClassDecor:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None
    def __call__(self, *args, **kwargs):
        if not self.instance:
            self.instance = self.cls(*args, **kwargs)
        return self.instance