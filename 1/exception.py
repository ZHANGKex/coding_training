def exception_example():
    try:
        numbers = [1, 2, 3]
        print(numbers[5]) # IndexError

        value = int('abc') # Value Error
        print(value)

        result = 10 / 0 # ZeroDivisionError
        print(result)
        file = open("Nonexistent_file.txt", "r") #FileNotFOundError
        print(file)

    except IndexError as e:
        print(f"IndexError - {e}")
    except ValueError as e:
        print(f"ValueError - {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError - {e}")
    except FileNotFoundError as e:
        print(f"filenotfoundError - {e}")
    except Exception as e:
        print(f"UnknowError - {e}")
    finally:
        print("no matter what it will always happen")

exception_example()


class MyException(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise MyException("input invalide")
    
try:
    check_positive(-1)
except MyException as e:
    print(f"error:{e}")


class ValidationError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

def validate_age(age):
    if age < 0:
        raise ValidationError("age is invalide", 400)
    
try:
    validate_age(-1)
except ValidationError as e:
    print(f"error - {e}, code is - {e.code}")


class ApplicationError(Exception):
    pass

class DatabaseError(ApplicationError):
    pass

class NetworkError(ApplicationError):
    pass

def connect_to_database():
    raise DatabaseError("error with connection database")

try:
    connect_to_database()
except DatabaseError as e:
    print(f"catch database error - {e}")
except ApplicationError as e:
    print(f"appication error {e}")

class AuthenticationError(Exception):
    def __init__(self, message, username, error_code):
        super().__init__(message)
        self.username = username
        self.error_code = error_code
    
    def __str__(self):
        return f"{self.args[0]} username: {self.username} , errorcode: {self.error_code}"
    

class OrderError(Exception):
    pass

class InvalidOrderAmountError(OrderError):
    def __init__(self, amount):
        super().__init__(f"amount is invalide, amount: {amount}")
        self.amount = amount

class InsufficientStockError(OrderError):
    def __init__(self, stock, required_quantity):
        super().__init__(f"not enough, now: {stock}, required: {required_quantity}")
        self.stock = stock
        self.required_quantity = required_quantity

class InvalidOrderStatusError(OrderError):
    def __init__(self, current_status, new_status):
        super().__init__(f"order status invalid, now: {current_status}, required: {new_status}")
        self.current_status = current_status
        self.new_status = new_status

def validate_order(amount):
    if amount < 0:
        raise InvalidOrderAmountError(amount)
    print("valide amount")

def check_inventory(stock, required_quantity):
    if stock < required_quantity:
        raise InsufficientStockError(stock, required_quantity)
    print("valide required quantity")

def update_order_status(current_status, new_status):
    if current_status == "Cancelled":
        raise InvalidOrderStatusError(current_status, new_status)
    print("valide status change")

try:
    amount = -100
    validate_order(amount)
except InvalidOrderAmountError as e:
    print(f"amount error - {e}")

try:
    stock = 5
    required_quantity = 10
    check_inventory(stock, required_quantity)
except OrderError as e:
    print(f"order error - {e}")

try:
    update_order_status("Cancelled", "Shipped")
except OrderError as e:
    print(f"order error - {e}")

