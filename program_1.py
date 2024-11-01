#AUTHOR: Trevor Conger UNWSP
#DATE: 10/30/24
#TITLE: Count lines in txt file



#FUNCTION: This function counts the lines in a .txt file with a read operation
#RETURN: Number of lines
def count_file_lines():
    with open('names.txt', 'r') as file:
        lines = file.readlines()
        lineCount = len(lines)

    print("Number of lines:", lineCount)

# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()