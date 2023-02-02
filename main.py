# This program was made to demostrate The Levenshtein distance
# Prints out the matrix of distances between prefixes as well as the Levenshtein distance value 

import numpy

first = "hello"
second = "henloo"

def levenshteinDistance(firstString, secondString):

    # Create 2D matrix of the strings
    distanceMatrix = numpy.zeros((len(firstString) + 1, len(secondString) + 1))

    # First string defines the amount of rows in matrix
    for rows in range(len(firstString) + 1):
        distanceMatrix[rows][0] = rows

    # Second string defines the amount of columns in matrix
    for columns in range(len(secondString) + 1):
        distanceMatrix[0][columns] = columns

    # Values
    valueA = 0
    valueB = 0
    valueC = 0

    # Calculate distances between prefixies
    for i in range(1, len(firstString) + 1):
        for j in range(1, len(secondString) + 1):
            # Checks if two characters in comparison are the same and moves to the next one if they are
            if (firstString[i - 1] == secondString[j - 1]):
                distanceMatrix[i][j] = distanceMatrix[i - 1][j - 1]
            else:
                # Notations 
                #   lev(i - 1,j) + 1
                #   lev(i,j - 1) + 1
                #   lev(i - 1, j - 1) + 1
                valueA = distanceMatrix[i][j - 1]
                valueB = distanceMatrix[i - 1][j]
                valueC = distanceMatrix[i - 1][j - 1]

                if(valueA <= valueB and valueA <= valueC):
                    distanceMatrix[i][j] = valueA + 1
                elif(valueB <= valueA and valueB <= valueC):
                    distanceMatrix[i][j] = valueB + 1
                else:
                    distanceMatrix[i][j] = valueC + 1
                
    printMatrix(distanceMatrix, len(firstString), len(secondString))
    return distanceMatrix[len(firstString)][len(secondString)]

# Function to print matrix into console   
def printMatrix(matrix, firstStringLen, secondStringLen):
    for rows in range(firstStringLen + 1):
        for columns in range(secondStringLen + 1):
            print(int(matrix[rows][columns]), end=" ")
        print()

distance = levenshteinDistance(first, second)
print("The Levenshtein distance between " + first + " and " + second + " is: " + str(int(distance)))