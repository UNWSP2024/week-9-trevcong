#AUTHOR: Trevor Conger UNWSP
#DATE: 10/30/24
#TITLE: Generate numbers!!

import random

def main():
    userInput = int(input("How many numbers would you like to be generated"))
    generateNumbers(userInput)

def generateNumbers(x):
    file1 = open("numbers.txt", "a") 
    for i in range(x): 
        numberRandom = random.randint(1, 500)
        file1.write(str(numberRandom) + "\n")
    file1.close() 

if __name__ == "__main__":
    main()