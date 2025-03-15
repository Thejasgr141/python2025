try:
    with open("sample.txt", "r") as file:  
        content = file.read()  
        print("File Contents:\n", content) 
except FileNotFoundError:
    print("Error: The file does not exist")
