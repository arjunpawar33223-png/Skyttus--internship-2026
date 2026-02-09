try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a / b)
except Exception as e:
    f = open("error.log", "a")
    f.write(str(e) + "\n")
    f.close()
    print("Error logged to file")