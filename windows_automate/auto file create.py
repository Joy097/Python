file_path = input("write ")
with open(file_path, "w") as file:
    file.write("Hello, this is the content of the file.\n")
    file.write("This is another line of content.")
    
print("File created and content written.")