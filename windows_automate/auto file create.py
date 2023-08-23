file_path = input("write the path :").strip()
rounds = int(input("How many times? :").strip())
count = 0
for i in range(rounds):
    
    with open(file_path, "w") as file:
        file.write("Hello, this is the content of the file.\n")
    