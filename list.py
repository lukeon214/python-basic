choice = int(input("""Enter a number of the list you want to see: 
1. food
2. transport
3. programming
"""))

list1 = ["apple", "strawberry", "melon"]
list2 = ["car", "plane", "boat"]
list3 = ["java", "python", "fun"]

if choice == 1:
    print(", ".join(list1))
elif choice == 2:
    print(", ".join(list2))
elif choice == 3:
    print(", ".join(list3))
else:
    print("Invalid input!")
