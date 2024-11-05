#AUTHOR: Trevor Conger UNWSP
#DATE: 10/30/24
#TITLE: Count lines in txt file


#FUNCTION: This function counts the lines in a .txt file with a read operation
#RETURN: Number of lines
def count_file_lines():
    try:
        with open('names.txt', 'r') as file:
            lines = file.readlines()
            lineCount = len([line.strip() for line in lines if line.strip()])
            print(f"Number of names in file: {lineCount}")
    except FileNotFoundError:
        print("Error: 'names.txt' file not found.")
    except PermissionError:
        print("Error: Permission denied accessing 'names.txt'.")
    except IOError as e:
        print(f"Error reading file: {e}")

# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()