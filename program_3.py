#AUTHOR: Trevor Conger UNWSP
#DATE: 10/30/24
#TITLE: Add all numbers in numbers.txt!


def main():
    sumNumberInTxtFile = sum_numbers_from_file()
    print("The sum of all the numbers in 'numbers.txt' is : ", sumNumberInTxtFile)


def sum_numbers_from_file():
    total = 0
    with open('numbers.txt', 'r') as file3:
        for line in file3:
            for number in line.split():
                try:
                    total += float(number)
                except ValueError:
                    pass 
    return total

if __name__ == '__main__':
    main()