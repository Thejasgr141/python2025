try:
    with open("sample.txt", "r") as file:  
        content = file.read()  
        char_count = len(content)  
        print(f"Number of characters in the file: {char_count}")
except FileNotFoundError:
    print("Error: The file does not exist.")  
except Exception as e:
    print("An error occurred:", e)  
