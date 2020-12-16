import numpy as np
import random

sValues2 = np.array([\
        [None, None, None, None, None, None, None, None, None, None],\
        [None, 3, 9, 8, 0, 0, 0, 0, 0, 0],\
        [None, 0, 0, 2, 0, 8, 0, 3, 5, 9],\
        [None, 0, 0, 0, 1, 0, 0, 4, 0, 0],\
        [None, 0, 4, 9, 0, 1, 0, 0, 0, 0],\
        [None, 8, 0, 0, 6, 9, 5, 0, 0, 4],\
        [None, 0, 0, 0, 0, 4, 0, 5, 9, 0],\
        [None, 0, 0, 5, 0, 0, 3, 0, 0, 0],\
        [None, 7, 8, 6, 0, 2, 0, 1, 0, 0],\
        [None, 0, 0, 0, 0, 0, 0, 7, 8, 2]\
        ])
sValues1 = np.array([\
        [None, None, None, None, None, None, None, None, None, None],\
        [None, 0,0,0,0,8,5,0,2,0],\
        [None, 0,0,0,0,8,5,0,2,0],\
        [None, 0,0,8,0,4,0,9,0,0],\
        [None, 0,0,0,0,0,0,0,8,0],\
        [None, 9,7,3,0,1,0,2,4,5],\
        [None, 0,4,0,0,0,0,0,0,0],\
        [None, 0,0,6,0,5,0,1,0,0],\
        [None, 0,8,0,0,0,0,0,0,3],\
        [None, 0,8,0,0,0,0,0,0,3]\
        ])
sValues = np.array([\
        [None, None, None, None, None, None, None, None, None, None],\
        [None, 0,0,8,0,6,0,9,1,4],\
        [None, 0,0,0,0,0,0,6,0,0],\
        [None, 0,6,0,4,0,2,0,5,0],\
        [None, 1,0,0,0,5,0,0,4,0],\
        [None, 0,5,6,9,0,7,3,8,0],\
        [None, 0,8,0,0,3,0,0,0,9],\
        [None, 0,1,0,5,0,8,0,9,0],\
        [None, 0,0,5,0,0,0,0,0,0],\
        [None, 8,4,7,0,2,0,1,0,0]\
        ])
originalValues = sValues

def findPossibleValues(curCell, sAddress, sValues, validNumbers):
    
        _3x3_square_pool = np.array([\
            [11, 12, 13, 21, 22, 23, 31, 32, 33],\
            [14, 15, 16, 24, 25, 26, 34, 35, 36],\
            [17, 18, 19, 27, 28, 29, 37, 38, 39],\
            [41, 42, 43, 51, 52, 53, 61, 62, 63],\
            [44, 45, 46, 54, 55, 56, 64, 65, 66],\
            [47, 48, 49, 57, 58, 59, 67, 68, 69],\
            [71, 72, 73, 81, 82, 83, 91, 92, 93],\
            [74, 75, 76, 84, 85, 86, 94, 95, 96],\
            [77, 78, 79, 87, 88, 89, 97, 98, 99]\
            ])

        column_Pool = np.array([\
            [11, 21, 31, 41, 51, 61, 71, 81, 91],\
            [12, 22, 32, 42, 52, 62, 72, 82, 92],\
            [13, 23, 33, 43, 53, 63, 73, 83, 93],\
            [14, 24, 34, 44, 54, 64, 74, 84, 94],\
            [15, 25, 35, 45, 55, 65, 75, 85, 95],\
            [16, 26, 36, 46, 56, 66, 76, 86, 96],\
            [17, 27, 37, 47, 57, 67, 77, 87, 97],\
            [18, 28, 38, 48, 58, 68, 78, 88, 98],\
            [19, 29, 39, 49, 59, 69, 79, 89, 99]\
            ])
        
        curCellStr = str(curCell)
        curLoc = {"x": int(curCellStr[0]), "y": int(curCellStr[1])}
        neighborValue = {"row": [], "column": [], "square": []}
        # iterate through the row of the current cell, add the value of the given cells to the neighborValue dict
        for item in sValues[curLoc["x"]]:
            if item != 0 and item in validNumbers:
                neighborValue["row"].append(item)

        # iterate through the column of the current cell, add the value of the given cells to the neighborValue dict
        column_address = column_Pool[curLoc["y"]-1]
        for address in column_address:
            addStr = str(address)
            location = {"x": int(addStr[0]), "y": int(addStr[1])}
            value = sValues[location["x"]][location["y"]]
            if value != 0 and value in validNumbers:
                neighborValue["column"].append(value)


        # Find addresses of the 3x3 square that this current cell belong to:
        _3x3_square_address = []
        if curLoc["x"] in [1, 2, 3] and curLoc["y"] in [1, 2, 3]:
            _3x3_square_address = _3x3_square_pool[0]
        elif curLoc["x"] in [1, 2, 3] and curLoc["y"] in [4, 5, 6]:
            _3x3_square_address = _3x3_square_pool[1]
        elif curLoc["x"] in [1, 2, 3] and curLoc["y"] in [7, 8, 9]:
            _3x3_square_address = _3x3_square_pool[2]

        elif curLoc["x"] in [4, 5, 6] and curLoc["y"] in [1, 2, 3]:
            _3x3_square_address = _3x3_square_pool[3]
        elif curLoc["x"] in [4, 5, 6] and curLoc["y"] in [4, 5, 6]:
            _3x3_square_address = _3x3_square_pool[4]
        elif curLoc["x"] in [4, 5, 6] and curLoc["y"] in [7, 8, 9]:
            _3x3_square_address = _3x3_square_pool[5]

        elif curLoc["x"] in [7, 8, 9] and curLoc["y"] in [1, 2, 3]:
            _3x3_square_address = _3x3_square_pool[6]
        elif curLoc["x"] in [7, 8, 9] and curLoc["y"] in [4, 5, 6]:
            _3x3_square_address = _3x3_square_pool[7]
        elif curLoc["x"] in [7, 8, 9] and curLoc["y"] in [7, 8, 9]:
            _3x3_square_address = _3x3_square_pool[8]

        # iterate through _3x3_square_address, get value of each item to add to the exclusion pool
        for address in _3x3_square_address:
            addStr = str(address)
            location = {"x": int(addStr[0]), "y": int(addStr[1])}
            value = sValues[location["x"]][location["y"]]
            if value != 0 and value in validNumbers:
                neighborValue["square"].append(value)
        # print(neighborValue)

        # group the neighbor values to one array
        neighborValueList = []
        for val in neighborValue["row"] + neighborValue["column"] + neighborValue["square"]:
            if val not in neighborValueList:
                neighborValueList.append(val)
        # print("neighborValueList: ",neighborValueList)

        # generate possible value for the current cell:
        possibleValues = []
        for num in validNumbers:
            if num not in neighborValueList:
                possibleValues.append(num)
        print(curCell, ", possibleValues: ", possibleValues)
        return possibleValues


def solveSudoku(sValues, originalValues):
    # 1. Get input from user on the given values on the sudoku
    # 1a. Check if input is valid
    # this step is pending

    # 2. Populate the given values to the sValues array
    # this step is pending

    # 3. Find the possible value for each cell with no given value
    sAddress = np.array([\
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],\
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],\
        [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],\
        [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],\
        [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],\
        [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],\
        [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],\
        [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],\
        [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],\
        [90, 91, 92, 93, 94, 95, 96, 97, 98, 99],\
        ])
    
    validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    

    possibleValueDict = {}
    knownValues = {}
    knownValueArr = sValues
    # keep a count of cell with single possible value. 
    # if there is no cell with single possible value, we'll need to pick a value from cells with 2 possible values
    countOfSingleValRange = 0
    
    # doubleValRangeList to store address of cells with 2 possible values, to use when there's no single possible value
    doubleValRangeList = []

    # iterate through the sValues array and find possible values for all the values not given
    for row in range (1, len(sValues)):
        for col in range (1, len(sValues[row])):
            curCell = int(str(row)+str(col))
            if sValues[row][col] in validNumbers:
                knownValues[curCell] = sValues[row][col]
            if sValues[row][col] == 0 and sValues[row][col] is not list:
                valueRange = findPossibleValues(curCell, sAddress, sValues, validNumbers)
                # if any of the possible value range is empty, that means the random choice we made wasn't good --> restart the function all over again
                if len(valueRange) == 0:
                    knownValueArr = originalValues
                    solveSudoku(knownValueArr, originalValues)
                elif len(valueRange) == 1:
                    knownValueArr[row][col] = valueRange[0]
                    knownValues[curCell] = valueRange[0]
                    countOfSingleValRange += 1
                    # note: this can be used for hints
                elif len(valueRange) == 2:
                    possibleValueDict[curCell] = valueRange
                    doubleValRangeList.append(int(str(row)+str(col)))
                elif len(valueRange) > 2:
                    possibleValueDict[curCell] = valueRange
    # in case of no single possible value:
    if countOfSingleValRange == 0:
        # pick a random item of the list of double possible value:
        randomItem = random.randint(0,len(doubleValRangeList)-1)
        randomItemAddress = doubleValRangeList[randomItem]
        # remember that doubleValRangeList [] contains addresses of cells with double possible value. Therefore randomItemAddress refers to an address 
        # get value of that address out from the possibleValueDict:
        selectedRange = possibleValueDict[randomItemAddress]
        # then, pick a random item from one of the 2 value:
        randomValNum = random.randint(0,1)
        selectedVal = selectedRange[randomValNum]
        # convert the address back to row and col
        r = int(randomItemAddress/10)
        c = int(randomItemAddress%10)
        # assign this value to the knownValueArr:
        knownValueArr[r][c] = selectedVal

    # print("knownValues: ", knownValues)
    print("knownValueArr: ", knownValueArr)
    # print("possibleValueDict: ", possibleValueDict)

    # recurse:
    # Exit when all the values are filled
    countOfKnownValues = 0
    for row in range (1, len(knownValueArr)):
        for col in range (1, len(knownValueArr[row])):
            if knownValueArr[row][col] in validNumbers:
                countOfKnownValues += 1
    if countOfKnownValues == 81:
        return knownValueArr
    else:
        solveSudoku(knownValueArr, originalValues)

solveSudoku(sValues, originalValues)

