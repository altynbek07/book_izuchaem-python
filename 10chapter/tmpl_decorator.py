from functools import wraps


def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Код для выполнения ПЕРЕД вызовом декорируемрй функции.

        # 2. Вызов декорируемой функции и возврат
        # полученных от нее результатов.
        return func(*args, **kwargs)

        # 3. Код для выполнения ВМЕСТО вызова декорируемой функции.
    return wrapper
