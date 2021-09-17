start = input("Enter the function to be executed: ")
if start == "1":
    x = int(input("Height:"))

    print("xxx\n"*x)

elif start == "3":
    x = int(input("List Length:"))

    while x>0:
        print(x)
        x-=1
