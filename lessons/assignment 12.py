def is_admin(func):
    def wrapper(*args, **kwargs):
        return wrapper()


@is_admin
def show_customer_receipt(user_type: str):
    # Some very dangerous operation

try:
    show_customer_receipt(user_type='user')
    raise ValueError("Permission denied")

show_customer_receipt(user_type='admin')




