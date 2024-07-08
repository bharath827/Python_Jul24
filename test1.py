def upadte_server(filePath, key, value):
    with open(filePath, "r") as file:
        lines = file.readlines()


    with open(filePath, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value+ "\n")

            else:
                file.write(line)


upadte_server("config.py", "TIMEOUT", "1000")