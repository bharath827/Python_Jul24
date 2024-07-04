# loops =>
# for loop / while loop

# is used to iterate over a sequence (list, string, tuples, dictio, range)



# syntax

#
# sequence = [1,2,3,4,5]
#
# for item in sequence:
#     print(item)
#
# message ="Hello World!"
#
# for char in message:
#     print(char)
#
# numbers = (1,2,3,4,5)
#
# for number in numbers:
#     print(number)

#
# numbers = [1,2,3,4,5,6,7,8,9,10]
#
# sum=0;
# for number in numbers:
#     # sum = sum + number
#     sum += number
# print("sum of numbers is : ",sum)
#
# list1 = ["a", "b", "c"]
# list2 = [1,2,3]
#
# for item1 in list1:
#     for item2 in list2:
#         print(f"({item1}, {item2})")

# range() => for loops to generate sequence of numbers

# range(start, stop, step)

# range(5) => 0,1,2,3,4
#
# for i in range(5):
#     print(i)

# for i in range(2, 6):
    # print(i)

# for  i in range(1,10,2):
#     print(i)
#
# for i in range(10, 0, -2):
#     print(i)
#
#
# configs = {
#     "hostname" :"example.com",
#     "port" : 25,
#     "username" : "admin"
# }

# [(),(),()]


#
# for key, value in configs.items():
#     print(key, value)


services = ["web", "database", "cache"]

# for service in services:
#     print("Deploying "+ service + " service...")
#     print(f"{service} service is deployed successfully")
#
#
# matrix = [
#     ["hostname", "example.com"],
#     ["port", 20],
#     ["username", "admin"],
#
# ]
#
# for item in matrix:
#     print(f"{item[0]} : {item[1]}")


servers = [
    {
      "name":"server1",
        "ip" : "192.168.1.1",
        "services" : ["web", "database"]
    },
    {
        "name": "server2",
        "ip": "192.168.1.2",
        "services": ["cache", "web"]
    },
    {
        "name": "server3",
        "ip": "192.168.1.3",
        "services": ["database", "cache"]
    },

]


server = {
      "name":"server1",
        "ip" : "192.168.1.1",
        "services" : ["web", "database"]
    }

#
# # print(server["services"])
# print("=======================================")
# for server in servers:
#     print(f"Server Name :{server['name']}")
#     print(f"IP Address :{server['ip']}")
#     print("Services :") # ["web", "database"]
#     for services in server["services"]:
#         print(f"  -{services}")


environments = {
    "development" : {
        "server1" : {
            "ip" :"192.168.1.1",
            "services" : ["cache", "web"]
        },
         "server2" : {
            "ip" :"192.168.1.2",
            "services" : ["web", "database"]
        },
    },
    "production" : {
        "server3" : {
            "ip" :"192.168.1.3",
            "services" : ["cache", "web"]
        },
         "server4" : {
            "ip" :"192.168.1.4",
            "services" : ["web", "database"]
        },
    }

}





#
# env = "development",
# servers =  {
#         "server1" : {
#             "ip" :"192.168.1.1",
#             "services" : ["cache", "web"]
#         },
#          "server2" : {
#             "ip" :"192.168.1.2",
#             "services" : ["web", "database"]
#         }
#
# server_name = server1
# server_info = {
#             "ip" :"192.168.1.1",
#             "services" : "cache"
#         },

for env, servers in environments.items():
    print(f"Environment : {env}")
    for server_name, server_info in servers.items():
        print(f"Server name: {server_name}")
        print(f"Ip address : {server_info['ip']}")
        print("Services")
        for service in server_info['services']:
            print(f"   -{service}")



