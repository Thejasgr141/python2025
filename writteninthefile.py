try:
    with open("output.txt", "w") as file:  
        text = input("Enter text to write into the file: ")
        file.write(text)  
        print("Text successfully written to output.txt")
except Exception as e:
    print("An error occurred:", e)  
