# while loop => execute a block of code repeatedly till condition became false
#
# while condition:
#     # code block to execute

#
# count = 0;
#
# while count < 5:
#     print(f"Count is: {count}")
#     count += 1


# for i in range(5):
#     print(i)


# total = 0;
# number =1;
#
# while total<10:
#     total += number;
#     print(f"Added{number}, total is now {total}")
#     number+=1
#
# user_input =""



# while user_input.lower() !="exit":
#     user_input = input("Enter input (type exit to quit) ")
#
#     if user_input.lower() =="exit":
#         print("exiting...")
#     else:
#         print(f"you entered: {user_input}")



# polling service untill it become available

service_up = False;
attempts  = 0;
max_attempts = 5;

while not service_up and attempts < max_attempts:
    attempts +=1
    print(f"checking service status (asttempts ({attempts})...)")

    if attempts == 3:
        service_up = True
        print("Servicce is up")
    else:
        print("Service is not available yet, Retrying...")

if not service_up:
    print("Service did not  become available within the maximum attempts...")
else:
    print("Proceeding with next steps")