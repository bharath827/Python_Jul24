# conditional statement => control the the flow of the execution based on the condition


# IF statement  => executes only if condition is true

# if condition :
#     # block of code to execute



# x = 10;
#
# if x<5 :
#     print("X is greater than 5")
#
# age = 18;
# if age>=18:
#     print("Your eligible to Vote")
#
#
# number = -1;
# if number > 0:
#     print("Number is Positive")
# else:
#     print("Number is Negative")



# Number is even or odd

# number = 20;
#
# if number % 2 == 0:
#     print("The Number is Even");
# else:
#     print("The Number is Odd")



# password = "secret"
#
# if password == "secret":
#     print("Access Granted");
# else:
#     print("Access Denied");


# if elif else statement : allows to you check multiple condition.

# if condition1:
#     print("qwerty"_)
# elif conditio2:
#  # execution
# elif condition3:
#  #execution
#
#
# else :
#  # execution

score = 80

if score>30:
    print("Grade F");
elif score>80:
    print("Grade B");
elif score>70:
    print("Grade C");
elif score>60:
    print("Grade D");
elif score>50:
    print("Grade E");
else :
    print("Grade F")







# total_space = 100 #Gb
# used_space = 50
# free_space = total_space - used_space
# threshold = 20
#
#
# if free_space < threshold :
#     print("Warning : Low Disk Space")
# elif free_space < threshold*2:
#     print("Caution: Disk Space is Getting Low")
# else:
#     print("Disk space is Sufficient")
#


# load = 65 #%
#
# if load < 30:
#     print("server load is low")
# elif load<70:
#     print("Server load is moderate")
# elif load<90:
#     print("Server is high")
# else:
#     print("Warning: server load is critical")


# branch = "develop"
#
# if branch=="main":
#     print("Deploying to production server.....")
#
# elif branch=="develop":
#     print("Deploying to staging server")
#
# elif branch =="feature":
#     print("Deploying to feature testing environment")
#
# else:
#     print("No deployment needed for this branch")


build_status = "success" #simulated build status


if build_status == "success":
    print("Build succeeded. Deploying the build...")
elif build_status == "failed":
    print("Build is failed. sending alert");
else:
    print("Build status is unknown. Please check the build logs")






