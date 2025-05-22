#Define the Decorator

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

#DEFINE A FUNCTION AND APPLY THE DDECORATOR
@log_function_call
def say_hello():
    print("Hello")
if __name__ == "__main__":
  say_hello()