#AUTHOR: Trevor Conger UNWSP
#DATE: 10/30/24
#TITLE: Generate numbers!!

import random

def main():
    generateNumbers()

#FUNCTION to generate numbers
#USER enters a number 1-1000, if not try again
#GENERATE numbers and write them to file numbers.txt
#1stTRY CATCH VALUE ERROR for not a number
#2ndTRY CATCH IOError for error writing to file
def generateNumbers():
    while True:
        try:
            count = input("How many numbers would you like to generate (1-1000)? ")
            count = int(count)
            if not 1 <= count <= 1000:
                print("Please enter a number between 1 and 1000.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    try:
        with open("numbers.txt", "w") as file:
            for _ in range(count):
                number = random.randint(1, 500)
                file.write(f"{number}\n")
        print(f"Successfully generated {count} numbers in 'numbers.txt'")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()