def is_admin(func):
    def wrapper(*args, **kwargs):
        user_type = kwargs.get("user_type")
        if user_type == "admin":
            return func(*args, **kwargs)
        else:
            raise ValueError("Permission denied")

    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    print("Success")


try:
    show_customer_receipt(user_type='user')
except ValueError as e:
    assert str(e) == "Permission denied"


show_customer_receipt(user_type='admin')
show_customer_receipt(user_type='user')


def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Found 1 error during execution of your function: KeyError no such key as foo")

    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})
