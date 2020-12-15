from django.shortcuts import render
import numpy as np

def index(request):

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
    sValue = np.array([\
        [None, None, None, None, None, None, None, None, None, None],\
        [None, 3, 9, 8, 0, 0, 0, 0, 0, 0],\
        [None, 0, 0, 2, 0, 8, 0, 3, 5, 9],\
        [None, 0, 0, 0, 1, 0, 0, 4, 0, 0],\
        [None, 0, 4, 9, 0, 1, 0, 0, 0, 0],\
        [None, 8, 0, 0, 6, 9, 5, 0, 0, 4],\
        [None, 0, 0, 0, 0, 4, 0, 5, 9, 0],\
        [None, 0, 0, 5, 0, 0, 3, 0, 0, 0],\
        [None, 7, 8, 6, 0, 2, 0, 1, 0, 0],\
        [None, 0, 0, 0, 0, 0, 0, 7, 8, 2],\
        ])

    validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
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

    curCell = 14
    curCellStr = str(14)
    curLoc = {"x": int(curCellStr[0]), "y": int(curCellStr[1])}
    exclusionValue = {"row": [], "square": []}
    # iterate through the row of the current cell, add the value of the given cells to the exclusionValue dict
    for item in sValue[curLoc["x"]]:
        if item != 0 and item in validNumbers:
            exclusionValue["row"].append(item)
    _3x3_square_address = []
    # Find addresses of the 3x3 square that this current cell belong to:
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

    context = {
        "color": "green"
    }
    return render(request, "index.html", context)