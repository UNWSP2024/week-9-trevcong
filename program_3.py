#AUTHOR: Trevor Conger UNWSP
#DATE: 10/30/24
#TITLE: Add all numbers in numbers.txt!


def main():
    sumNumberInTxtFile = sum_numbers_from_file()
    print("The sum of all the numbers in 'numbers.txt' is : ", sumNumberInTxtFile)

#FUNCTION to sum number from a file given the file name
#TRY CATCH open file as read, if unable except IOError
#TRY CATCH total sum, if unable except ValueError
#RETURN TOTAL sum
#OR RETURN 
def sum_numbers_from_file():
    total = 0
    try:
        with open('numbers.txt', 'r') as file:
            for line in file:
                try:
                    number = float(line)
                    total += number
                except ValueError:
                    print(f"Warning: Skipping invalid number in file")
                    continue
        return total
            
    except IOError as e:
        print(f"Error reading file: {e}")
        return 0

if __name__ == '__main__':
    main()