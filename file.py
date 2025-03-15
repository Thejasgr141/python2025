try:
    with open("sample.txt", "r") as file:  
        lines = file.readlines() 
        line_count = len(lines) 
        print(f"Number of lines in the file: {line_count}")
except 
    print("Error: The file does not exist.")  
except Exception as e:
    print("An error occurred:", e)  
