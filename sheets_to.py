with open("values.txt", "r") as values_file:
    for value in values_file:
        print("\""+value.rstrip("\n")+"\",")