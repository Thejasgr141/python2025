try:
    with open("output.txt", "a") as file:  
        text = input("Enter text to append to the file: ")  
        file.write("\n" + text)  
        print("Text successfully appended to output.txt")
except Exception as e:
    print("An error occurred:", e) 
