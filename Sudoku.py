import sys, time, pdb, random
sys.setrecursionlimit(20000)
##blueprint:
blueprint={
    "0_0":[
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ],
    "0_1":[
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ],
    "0_2":[
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ],
    "1_0":[
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ],
    "1_1":[
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ],
    "1_2":[
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ],
    "2_0":[
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ],
    "2_1":[
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ],
    "2_2":[
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]
}

# sudoku={
#     "0_0":[
#     [1, 8, 7],
#     [None, 4, 5],
#     [None, None, None]
#     ],
#     "0_1":[
#     [3, None, None],
#     [7, None, 9],
#     [5, None, None]
#     ],
#     "0_2":[
#     [None, 5, 9],
#     [3, None, None],
#     [4, None, 7]
#     ],
#     "1_0":[
#     [5, None, None],
#     [None, 1, None],
#     [None, 7, None]
#     ],
#     "1_1":[
#     [2, None, 4],
#     [None, 3, None],
#     [None, None, None]
#     ],
#     "1_2":[
#     [None, 6, None],
#     [5, 7, 2],
#     [None, 4, None]
#     ],
#     "2_0":[
#     [None, 2, None],
#     [4, None, None],
#     [7, 6, None]
#     ],
#     "2_1":[
#     [None, None, None],
#     [8, None, 7],
#     [None, 9, 3]
#     ],
#     "2_2":[
#     [7, 3, None],
#     [6, 9, 1],
#     [None, 2, 5]
#     ]
# }

# sudoku={
#     "0_0":[
#     [9, None, None],
#     [6, 5, None],
#     [None, 4, None]
#     ],
#     "0_1":[
#     [None, None, 8],
#     [4, 9, None],
#     [None, 1, 7]
#     ],
#     "0_2":[
#     [None, None, None],
#     [None, 1, None],
#     [None, 5, None]
#     ],
#     "1_0":[
#     [None, 9, None],
#     [None, 6, 3],
#     [None, None, None]
#     ],
#     "1_1":[
#     [None, None, None],
#     [7, 8, 5],
#     [None, None, None]
#     ],
#     "1_2":[
#     [None, None, None],
#     [4, 9, None],
#     [None, 2, None]
#     ],
#     "2_0":[
#     [None, 2, None],
#     [None, 1, None],
#     [None, None, None]
#     ],
#     "2_1":[
#     [9, 4, None],
#     [None, 5, 6],
#     [8, None, None]
#     ],
#     "2_2":[
#     [None, 8, None],
#     [None, 7, 4],
#     [None, None, 2]
#     ]
# }

sudoku={
    "0_0":[
    [None, None, 6],
    [None, 8, None],
    [5, None, 2]
    ],
    "0_1":[
    [7, None, None],
    [1, None, None],
    [None, 4, None]
    ],
    "0_2":[
    [None, None, None],
    [5, None, None],
    [1, None, 7]
    ],
    "1_0":[
    [None, 4, None],
    [3, None, None],
    [None, None, None]
    ],
    "1_1":[
    [3, 7, None],
    [None, None, None],
    [None, 9, 6]
    ],
    "1_2":[
    [None, None, None],
    [None, None, 2],
    [None, 7, None]
    ],
    "2_0":[
    [6, None, 5],
    [None, None, 4],
    [None, None, None]
    ],
    "2_1":[
    [None, 1, None],
    [None, None, 9],
    [None, None, 7]
    ],
    "2_2":[
    [7, None, 9],
    [None, 1, None],
    [6, None, None]
    ]
} ##lacking Sudoku stuctured in squares

## *python quit unexpectedly*
# sudoku={
#     "0_0":[
#     [8, None, None],
#     [None, None, 3],
#     [None, 7, None]
#     ],
#     "0_1":[
#     [None, None, None],
#     [6, None, None],
#     [None, 9, None]
#     ],
#     "0_2":[
#     [None, None, None],
#     [None, None, None],
#     [2, None, None]
#     ],
#     "1_0":[
#     [None, 5, None],
#     [None, None, None],
#     [None, None, None]
#     ],
#     "1_1":[
#     [None, None, 7],
#     [None, 4, 5],
#     [1, None, None]
#     ],
#     "1_2":[
#     [None, None, None],
#     [7, None, None],
#     [None, 3, None]
#     ],
#     "2_0":[
#     [None, None, 1],
#     [None, None, 8],
#     [None, 9, None]
#     ],
#     "2_1":[
#     [None, None, None],
#     [5, None, None],
#     [None, None, 7]
#     ],
#     "2_2":[
#     [None, 6, 8],
#     [None, 1, None],
#     [4, None, None]
#     ]
# }

# sudoku={
#     "0_0":[
#     [None, None, None],
#     [9, None, 3],
#     [None, None, None]
#     ],
#     "0_1":[
#     [None, None, 3],
#     [None, None, None],
#     [4, 7, 2]
#     ],
#     "0_2":[
#     [1, 6, None],
#     [None, None, 7],
#     [3, 8, None]
#     ],
#     "1_0":[
#     [None, None, None],
#     [3, None, None],
#     [None, 1, 6]
#     ],
#     "1_1":[
#     [1, 6, 5],
#     [8, None, 7],
#     [3, 9, 4]
#     ],
#     "1_2":[
#     [2, 9, None],
#     [None, None, 1],
#     [None, None, None]
#     ],
#     "2_0":[
#     [None, 7, 4],
#     [1, None, None],
#     [None, 3, 2]
#     ],
#     "2_1":[
#     [6, 3, 1],
#     [None, None, None],
#     [7, None, None]
#     ],
#     "2_2":[
#     [None, None, None],
#     [7, None, 4],
#     [None, None, None]
#     ]
# }

mNums=[]
aNums=[]
usedNums = {'0_0':{},'0_1':{},'0_2':{},'1_0':{},'1_1':{},'1_2':{},'2_0':{},'2_1':{},'2_2':{}}

def copy(iniSudoku): ##creates a duplicate of original sudoku
    import copy;duplicate=copy.deepcopy(iniSudoku)
    return duplicate
tempSudoku=copy(sudoku)
def missingNo(mat): ##creates an array for each square and contains missing numbers
    list=[x for x in range(1,10)]
    for y in range(0,len(mat)):
        for x in range(0,len(mat[y])):
            if mat[y][x] in list:
                list[mat[y][x]-1]=-1
    return list
def fill(mat, key, sudoku, n, usedNums, x, y):
    if n<0: ## available numbers are exhausted
        return False
    if mat[y][x]==None: ## position xy in square is empty
        while aNums[n]==-1:
            n-=1
            if n<0: ## might be able to 'DRY'
                return False
        mat[y][x]=aNums[n] ## fills spot with an available number
        y_key=key[0]
        x_key=key[2]
        ## checks if put in number is apropriate
        if check(mat, mat[y][x], x_key, y_key, x, y, usedNums, sudoku):
            aNums.pop(n)
            y_x=str(y)+"_"+str(x)
            ## asigns number to 'usedNums' so it is not being used in the same spot again
            if not y_x in usedNums:
                usedNums[y_x]=[]
            usedNums[y_x].append(mat[y][x])
            return True
        else:
            mat[y][x]=None
            ## if check returned false it tries different number
            return fill(mat, key, sudoku, n-1, usedNums, x, y)
    else:
        return True ## spot in square wasn't empty -> move forward
def secure(mat, usedNums, x, y):
    usedNums.pop(str(y)+"_"+str(x), None) ## used numbers prior alter so they're irrelevent
    if x>1:
        if y>1:
            return []## can not find coordinates prior
        else:
            y+=1
            x=0
    else:
        x+=1
    if mat[y][x] in mNums:
        aNums.append(mat[y][x]) ## set backtracked number available again
        mat[y][x]=None ##empty the spot being altered
        return [y,x] ## return new current xy-coordinates
    ## in case spot was filled to begin with
    else: return secure(mat, usedNums, x, y)
def fillSquare(mat, key, sudoku, n, usedNums, x=2, y=2, secured=[]):##fills the lacking Sudoku with numbers of missing-list
    if y<0 or len(aNums)==0: ## base case
        return True
    if not fill(mat, key,sudoku, n, usedNums, x, y): ## fills square at x y
        secured=secure(mat, usedNums, x, y) ## in case square at x y couldn't get filled; finds new xy-coordinates
        if secured==[]: ## in case new prior coordinates couldn't be found
            return False
        else: y=secured[0];x=secured[1]
        return fillSquare(mat, key, sudoku, len(aNums)-2, usedNums, x, y)
    ## move ahead in square
    elif x<1:
        y-=1
        x=2
    else:
        x-=1
    return fillSquare(mat, key, sudoku, len(aNums)-1, usedNums, x, y) ## call recursively
def check(mat, num, x_key, y_key, x, y, usedNums, tempSudoku):     ##checks every number on the same y and x coordinate
    to_check_x=[];to_check_y=[]
    y_x=str(y)+"_"+str(x)
    if y_x in usedNums:
        if num in usedNums[y_x]: ## prevents numbers to be filled in the same spot->ending in a cycle
            return False
    for i in range(3):
        if i!=int(y_key): to_check_y.append(str(i)+"_"+str(x_key))
        if i!=int(x_key): to_check_x.append(str(y_key)+"_"+str(i))
    for i in to_check_y: ## checks every number in the same row to be the same
        for j in range(3):
            if num==tempSudoku[i][j][x]:
                return False
    for i in to_check_x: ## checks every number in the same column to be the same
        for j in range(3):
            if num==tempSudoku[i][y][j]:
                return False
    return True ## no interference
def fillSudoku(sudoku, tempSudoku, square="0_0", safe=True, z=1):   ##main function
    y=int(square[0])
    x=int(square[2])
    if y>2: ## base case
        return
    newSqr=tempSudoku[square] ##current square
    list=missingNo(sudoku[square]) ##creates an array with missing numbers (*function above*)
    while len(mNums)> 0:
        mNums.pop()
    for item in list:
        mNums.append(item)
    random.shuffle(mNums) ##shuffles the missing numbers so that the result of the blueprint is different every time
    if not safe: ##in case the last square couldn't be filled ->backtracking
        ## check for the last number that got filled artificially
        prevX=0
        prevY=0
        lastNum=newSqr[prevY][prevX]
        while not safe:
            if lastNum in mNums:
                while len(aNums)>0:
                    aNums.pop()
                aNums.append(lastNum)
                safe=True
            elif prevX>1:
                prevY+=1
                prevX=0
            else:
                prevX+=1
            lastNum=newSqr[prevY][prevX]
        newSqr[prevY][prevX]=None ## set the last number to none so it has to change it
        ## fills the prior square and returns if it was successful
        safe=fillSquare(newSqr, square,   tempSudoku, len(aNums)-1, usedNums[square], prevX, prevY)
    ## if it goes forward in the whole algorithm this is the standart procedure->fills square; sets available numbers for square
    else:
        list=copy(mNums)
        while len(aNums)>0:
            aNums.pop()
        for item in list:
            aNums.append(item)
        safe=fillSquare(newSqr, square,  tempSudoku, len(aNums)-1, usedNums[square])
    if not safe: ## in case the last algorithm had no success in filling the current squares->prepare for backtracking
        if x<1:
            y-=1
            x=2
        else:
            x-=1
    else: ## sets the yx-coordinates ahead
        if x>1:
            y+=1
            x=0
        else:
            x+=1
    square=str(y)+"_"+str(x) ##updates the key for sudoku hash table
    # z+=1
    # print(z)
    return fillSudoku(sudoku, tempSudoku, square, safe) ## calls itself recursively
def displaySudoku(sudoku, key="", x=0, y=0, i=0):     ##displays the Sudoku in order
    if y>2:
        return
    result="| "
    for x in range(0,3):
        key=str(y)+"_"+str(x)
        for j in sudoku[key][i]:
            if j==None:
                result+="  "
            else:result+=str(j)+" "
        result+="| "
    print(result)
    if i>1:
        i=0
        y+=1
        print("------------------------")
    else:
        i+=1
    displaySudoku(sudoku, key, x, y, i)
def createSudoku(sudoku, dif=5): ##takes lacking sudoku/blueprint and creates a new lacking Sudoku; takes difficulty
    copy_sudoku=copy(sudoku)
    fillSudoku(sudoku, copy_sudoku) ## completes the Sudoku
    for square in copy_sudoku:
        for i in range(3):
            for j in range(3):
                num = int(random.random()*10) ## picks a number ranging from 0 to 10 (excluding 10)
                ## if random number is smaller than the degree of difficulty (10->complete; 1->almost empty)
                ## creates gap in Sudoku; undoes
                if num < dif:
                    copy_sudoku[square][i][j]=None
    return copy_sudoku
displaySudoku(tempSudoku)
fillSudoku(sudoku, tempSudoku)
displaySudoku(tempSudoku)
print("_________________________________\n")
newSudoku=createSudoku(blueprint, 7)
displaySudoku(newSudoku)
