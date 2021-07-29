#Lab 4
#File name: MatrixGame.py
#Author:Andora Zuniga
#Date: September 12th, 2019
#Purpose:   allows a user to enter the values of two, 3x3 matrices and then select from
#           options including, addition, subtraction, matrix multiplication, and element by element multiplication

#import statement
import numpy as np

#Start of program 
#welcome message
print("*****************Welcome to the Matrix Application*****************")

choice = ''
menuSelection = ''

rows = 3
columns = 3

while choice != 'n':
    choice = input("\nDo you want to play the Matrix Game? y or n: ")
    if choice == 'y':
     #initialise 
        matA=[]
        matB=[]
    #Create first matrix
    #input each row at a time,with each element separated by a space
        print("Enter your first %s x %s matrix: "% (rows, columns))
        for i in range(rows):
            while True:
                try:
                    matA.append(list(map(int, input().rstrip().split())))
                    break
                except:
                    print("Incorrect input, try again")
        firstMatrix = np.array(matA)
        print("This is your first Matrix: \n")
        print(firstMatrix)
        
    #Create second matrix
    #input each row at a time,with each element separated by a space
        print("Enter your second %s x %s matrix: "% (rows, columns))
        for i in range(rows):
            while True:
                try:
                    matB.append(list(map(int, input().rstrip().split())))
                    break
                except:
                    print("Incorrect input, try again")
        secondMatrix = np.array(matB)
        print("\nThis is your second  Matrix: ")
        print(secondMatrix)
        
        #Start math menu
        print("Select a Matrix Operation from the list below:")
        print("a. Addition")
        print("b. Subtraction")
        print("c. Matrix Multiplication")
        print("d. Element by element multiplication")
        menuSelection = input()
        
        if menuSelection == 'a':
            print("\nYou selected Addition, the results are: ")
            resultsMatrix = np.array(firstMatrix + secondMatrix)
            print(resultsMatrix)
            print("\nThe transpose is: ")
            print(resultsMatrix.T)
            print("The row and column mean values of the results are: ")
            print("Row: ")
            print(resultsMatrix.mean(axis=0))
            print("Column: ")
            print(resultsMatrix.mean(axis=1))
            
        if menuSelection == 'b':
            print("\nYou selected Subtraction, the results are: ")
            resultsMatrix = np.array(firstMatrix - secondMatrix)
            print(resultsMatrix)
            print("\nThe transpose is: ")
            print(resultsMatrix.T)
            print("The row and column mean values of the results are: ")
            print("Row: ")
            print(resultsMatrix.mean(axis=0))
            print("Column: ")
            print(resultsMatrix.mean(axis=1))
            
        if menuSelection == 'c':
            print("\nYou selected Matrix Multiplication, the results are: ")
            resultsMatrix = np.matmul(firstMatrix, secondMatrix)
            print(resultsMatrix)
            print("\nThe transpose is: ")
            print(resultsMatrix.T)
            print("The row and column mean values of the results are: ")
            print("Row: ")
            print(resultsMatrix.mean(axis=0))
            print("Column: ")
            print(resultsMatrix.mean(axis=1))
            
        if menuSelection == 'd':
            print("\nYou selected Element by Element multiplication the results are: ")
            resultsMatrix = np.array(firstMatrix * secondMatrix)
            print(resultsMatrix)
            print("\nThe transpose is: ")
            print(resultsMatrix.T)
            print("The row and column mean values of the results are: ")
            print("Row: ")
            print(resultsMatrix.mean(axis=0))
            print("Column: ")
            print(resultsMatrix.mean(axis=1))
        
    if choice == 'n':
        print("\nThank you for trying the Matrix Application!")
        print("\n******************************Bye!!!!!!!!!!******************************")
    