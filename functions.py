# functions =>
# reusable block of code and to avoid repetition

#
#
# a = 10;
# b = 20;
#
# sum = a+b;
#
#
# c = 40;
# d = 60;
#
# sum1 = c +d;



# syntax

# def function_name(parameters):
    #function body
    #optional return statement


# def greet(name):
#     print(f"Hello, {name}")
#
#
# greet("Sachin")
# greet("Ravi")


def add(a,b):
    # print(a+b)
     a+b


result = add(1,3)
print(result)


# msg = "hello"
# msg2=  msg.upper()

# print(
#     msg2
# )


# print(result)
# print(add(5,6))



# variable scope
# global
# local

# msg = "this is a msg" #Global Variable
#
# def local_scope():
#     local_var = "I'm Local"
#     print(local_var, msg)
#
#
# local_scope()
# print(local_var)

def check_service_status(service_name):
    if service_name == "webserver":
        return "running"
    else:
        return ("stopped")

service = "database"
status = check_service_status(service)
print(f"Service {service} is {status}.")


#report

def generate_report(service_status, resource_usage):

    report = f"Service status : {service_status}\n"
    report += "Resource usage:\n"

    # report = Service status : {service_status}
    #           Resource usage:
    #             CPU : 75%
    #             Memory: 60%

# report = report + "Resource usage:\n"
#  print("hello" + "world")

    for resource, usage in resource_usage.items():
        report += f"{resource} : {usage} \n"
    return  report


service_status ="running"
resource_usage = {
    "CPU" : "75%",
    "Memory" : "60%",
    "Disk" : "80%"
}

print('---------------')
report = generate_report(service_status, resource_usage)
print(report)



def validate_config(config):
    required_keys = ["host","port","timeout"]

    for  key in required_keys:
        if key not in config:
            return False, f"Missing required configuration : {key}"
    return True, "Configuration is valid","qwerty"




config = {
    "host" : "localhost",
    "port" : 8080,
    "qwert" : 30
}


is_valid, message = validate_config(config)
print(is_valid,message)