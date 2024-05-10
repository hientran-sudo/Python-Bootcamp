inputs = eval(input())


def logging_decorator(function):

  def wrapper(*args):
    print(f"You called {function.__name__}")
    result = function(args[0], args[1], args[2])
    print(result)

  return wrapper


@logging_decorator
def a_function(a, b, c):
  return a * b * c


a_function(inputs[0], inputs[1], inputs[2])

# input [1,2,3]
# output 
# You called a_funtion 
# 6
