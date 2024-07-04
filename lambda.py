# lambda function =>


# syntax
#
# lambda arguments : expression


def square(x):
    return x*x


print(square(5))


square_lambda = lambda x : x*x
print(square_lambda(5))


# def add(x,y)

add_lambda = lambda x,y : x+y

print(add_lambda(2,3))



format_log = lambda message, timestamp : f"{timestamp} : {message}"
print(format_log("System Rebooted", "2024-07-04 18:12:00"))