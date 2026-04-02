# it allows us to enhance the funtion()
# def decorator(func):
#     def wrapper():
#         print("i'm about to print hello")
#         func()
#         print("i printed the function")
#     return wrapper
# @decorator
# def hell():
#     print("heyy")
# hell()
  
# f = decorator(hell)
# f()

# Decorator with ARGS
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper 
    return decorator   
@repeat(7)
def hell(a):
    print(f"HELLO {a}")

hell("ronit")