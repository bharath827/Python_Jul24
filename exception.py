def divide():


    try:
        a = float(input("eneter a  : "))
        b = float(input("eneter b : "))
        result = a / b
    except ZeroDivisionError:
        print("invalid divison by zero not allowed")
    except NameError:
        print("but input must be numbers")
    except TypeError:
        print("typeerror")
    else:
        print(f"rsult: {result}")
    finally:
        print("succesful")

divide()

