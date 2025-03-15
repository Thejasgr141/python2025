with open(file_name, "r") as file:
        content = file.read()  

    new_content = content.replace(word_to_find, replacement_word)  

    with open(file_name, "w") as file:
        file.write(new_content)  

    print(f"'{word_to_find}' replaced with '{replacement_word}' in {file_name}.")

except FileNotFoundError:
    print("Error: The file does not exist.") 
except Exception as e:
    print("An error occurred:", e)  
