file_path = input("write the path :").strip()
with open(file_path, "w") as file:
    file.write("Hello, this is the content of the file.\n")
    