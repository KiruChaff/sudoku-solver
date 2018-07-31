import sys, pdb, random, copy
sys.setrecursionlimit(20000)
## sudokus to be filled:
##empty Sudoku:
#sudoku={
#     "0_0":[
#     [None, None, None],
#     [None, None, None],
#     [None, None, None]
#     ],
#     "0_1":[
#     [None, None, None],
#     [None, None, None],
#     [None, None, None]
#     ],
#     "0_2":[
#     [None, None, None],
#     [None, None, None],
#     [None, None, None]
#     ],
#     "1_0":[
#     [None, None, None],
#     [None, None, None],
#     [None, None, None]
#     ],
#     "1_1":[
#     [None, None, None],
#     [None, None, None],
#     [None, None, None]
#     ],
#     "1_2":[
#     [None, None, None],
#     [None, None, None],
#     [None, None, None]
#     ],
#     "2_0":[
#     [None, None, None],
#     [None, None, None],
#     [None, None, None]
#     ],
#     "2_1":[
#     [None, None, None],
#     [None, None, None],
#     [None, None, None]
#     ],
#     "2_2":[
#     [None, None, None],
#     [None, None, None],
#     [None, None, None]
#     ]
# }

# sudoku={
#     "0_0":[
#     [5, 6, None],
#     [3, None, 2],
#     [4, None, 9]
#     ],
#     "0_1":[
#     [None, None, 9],
#     [None, None, None],
#     [6, 5, None]
#     ],
#     "0_2":[
#     [8, None, 4],
#     [None, None, None],
#     [None, None, 3]
#     ],
#     "1_0":[
#     [7, None, None],
#     [None, 5, None],
#     [8, None, None]
#     ],
#     "1_1":[
#     [None, None, 2],
#     [None, None, None],
#     [5, None, None]
#     ],
#     "1_2":[
#     [None, None, None],
#     [9, None, None],
#     [None, None, None]
#     ],
#     "2_0":[
#     [9, None, None],
#     [6, None, 1],
#     [None, None, 8]
#     ],
#     "2_1":[
#     [2, None, 6],
#     [9, None, 5],
#     [None, None, None]
#     ],
#     "2_2":[
#     [None, None, None],
#     [None, None, None],
#     [None, 9, None]
#     ]
# }

# sudoku={
#     "0_0":[
#     [None, None, 6],
#     [None, 8, None],
#     [5, None, 2]
#     ],
#     "0_1":[
#     [7, None, None],
#     [1, None, None],
#     [None, 4, None]
#     ],
#     "0_2":[
#     [None, None, None],
#     [5, None, None],
#     [1, None, 7]
#     ],
#     "1_0":[
#     [None, 4, None],
#     [3, None, None],
#     [None, None, None]
#     ],
#     "1_1":[
#     [3, 7, None],
#     [None, None, None],
#     [None, 9, 6]
#     ],
#     "1_2":[
#     [None, None, None],
#     [None, None, 2],
#     [None, 7, None]
#     ],
#     "2_0":[
#     [6, None, 5],
#     [None, None, 4],
#     [None, None, None]
#     ],
#     "2_1":[
#     [None, 1, None],
#     [None, None, 9],
#     [None, None, 7]
#     ],
#     "2_2":[
#     [7, None, 9],
#     [None, 1, None],
#     [6, None, None]
#     ]
# }
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
    [None, None, None],
    [9, None, 3],
    [None, None, None]
    ],
    "0_1":[
    [None, None, 3],
    [None, None, None],
    [4, 7, 2]
    ],
    "0_2":[
    [1, 6, None],
    [None, None, 7],
    [3, 8, None]
    ],
    "1_0":[
    [None, None, None],
    [3, None, None],
    [None, 1, 6]
    ],
    "1_1":[
    [1, 6, 5],
    [8, None, 7],
    [3, 9, 4]
    ],
    "1_2":[
    [2, 9, None],
    [None, None, 1],
    [None, None, None]
    ],
    "2_0":[
    [None, 7, 4],
    [1, None, None],
    [None, 3, 2]
    ],
    "2_1":[
    [6, 3, 1],
    [None, None, None],
    [7, None, None]
    ],
    "2_2":[
    [None, None, None],
    [7, None, 4],
    [None, None, None]
    ]
}

# XXX: is too difficulty for the program to handle
## -> python quit unexpectedly

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
#     [None, None, 5],
#     [8, None, None],
#     [None, 7, None]
#     ],
#     "0_1":[
#     [3, None, None],
#     [None, None, None],
#     [None, 1, None]
#     ],
#     "0_2":[
#     [None, None, None],
#     [None, 2, None],
#     [5, None, None]
#     ],
#     "1_0":[
#     [4, None, None],
#     [None, 1, None],
#     [None, None, 3]
#     ],
#     "1_1":[
#     [5, None, None],
#     [None, None, None],
#     [None, None, 9]
#     ],
#     "1_2":[
#     [3, None, None],
#     [None, None, 6],
#     [None, 8, None]
#     ],
#     "2_0":[
#     [None, 6, None],
#     [None, None, 4],
#     [None, None, None]
#     ],
#     "2_1":[
#     [5, None, None],
#     [None, None, None],
#     [None, None, 9]
#     ],
#     "2_2":[
#     [None, None, 9],
#     [None, 3, None],
#     [7, None, None]
#     ]
# }

class FillSudoku:
    def __init__(self, sudoku):
        self.sudoku=sudoku
        self.mNums=[]
        self.aNums=[]
        self.usedNums={}
        for i in range(3):
            for j in range(3):
                self.usedNums[str(i)+"_"+str(j)]={}
        self._sudoku=self._copy(sudoku)
        self.key="0_0"
        self.square=[]
    def _copy(self,init):
        ##creates a duplicate of original sudoku
        duplicate=copy.deepcopy(init)
        return duplicate
    def _missingNums(self, square):
        ##creates an array for each square and contains missing numbers
        list=[x for x in range(1,10)]
        for i in range(3):
            for j in range(3):
                if not square[i][j]==None:
                    list.remove(square[i][j])
        return list
    def _check(self, num, x, y):
          ##checks every number on the same y and x coordinate
        y_key=self.key[0]
        x_key=self.key[2]
        to_check_x=[]; to_check_y=[]
        y_x=str(y)+"_"+str(x)
        if y_x in self.usedNums[self.key]: ## prevents numbers to be filled in the same spot->ending in a cycle
            if num in self.usedNums[self.key][y_x]:
                return False
        for i in range(3):
            if i!=int(y_key): to_check_y.append(str(i)+"_"+str(x_key))
            if i!=int(x_key): to_check_x.append(str(y_key)+"_"+str(i))
        for i in to_check_y:    ## checks every number in the same row to be the same
            for j in range(3):
                if num==self._sudoku[i][j][x]:
                    return False
        for i in to_check_x:    ## checks every number in the same column to be the same
            for j in range(3):
                if num==self._sudoku[i][y][j]:
                    return False
        return True ## no interference
    def _secure(self, x, y):
         ## used numbers prior alter so they're irrelevent
        self.usedNums[self.key].pop(str(y)+"_"+str(x), None)
        if x>1:
            if y>1:
                return [] ## can not find coordinates prior
            else:
                y+=1
                x=0
        else: x+=1
        if self.square[y][x] in self.mNums:
            self.aNums.append(self.square[y][x]) ## set backtracked number available again
            self.square[y][x]=None  ##empty the spot being altered
            return [y,x]    ## return new current xy-coordinates
        ## in case spot was filled to begin with
        else: return self._secure(x, y)
    def fillSpot(self, n, x, y):
        if n<0: ## available numbers are exhausted
            return False
        if self.square[y][x]==None: ## position xy in square is empty
            self.square[y][x]=self.aNums[n]## fills spot with an available number
            ## checks if put in number is apropriate
            if self._check(self.square[y][x], x, y):
                self.aNums.pop(n)
                y_x=str(y)+"_"+str(x)
                ## asigns number to 'usedNums' so it is not being used in the same spot again
                if y_x not in self.usedNums[self.key]:
                    self.usedNums[self.key][y_x]=[]
                self.usedNums[self.key][y_x].append(self.square[y][x])
                return True
            else:
                self.square[y][x]=None
                ## if check returned false it tries different number
                return self.fillSpot(n-1, x, y)
        else: return True ## spot in square wasn't empty -> move forward
    def fillSquare(self, n, x=2, y=2, secured=[]):
        if y<0 or len(self.aNums)==0:  ## base case
            return True
        if not self.fillSpot(n, x, y):   ## fills square at x y
            secured=self._secure(x, y)  ## in case new prior coordinates couldn't be found
            if secured==[]:
                return False
            else: y=secured[0];x=secured[1]
            return self.fillSquare(len(self.aNums)-2, x, y)
        ## move ahead in square
        elif x<1:
            y-=1
            x=2
        else:
            x-=1
        return self.fillSquare(len(self.aNums)-1, x, y) ## call recursively
    def fillSudoku(self, safe=True):
        ## main function
        x_key=int(self.key[2])
        y_key=int(self.key[0])
        if y_key>2: ## base case
            return self._sudoku
        self.square=self._sudoku[self.key] ##current square
        self.mNums=self._missingNums(self.sudoku[self.key]) ##creates an array with missing numbers
        random.shuffle(self.mNums)  ##shuffles the missing numbers so that the result of the blueprint is different every time
        if not safe:    ## in case the last square couldn't be filled ->backtracking
            ## check for the last number that got filled artificially
            prev_y=0
            prev_x=0
            prev_num=self.square[prev_y][prev_x]
            while not safe:
                if prev_num in self.mNums:
                    while len(self.aNums)>0:
                        self.aNums.pop()
                    self.aNums.append(prev_num)
                    safe=True
                elif prev_x>1:
                    prev_y+=1
                    prev_x=0
                else: prev_x+=1
                prev_num=self.square[prev_y][prev_x]
            self.square[prev_y][prev_x]=None    ## set the last number to none so it has to change it
            ## fills the prior square and returns if it was successful
            safe=self.fillSquare(len(self.aNums)-1, prev_x, prev_y)
        else:
                ## if it goes forward in the whole algorithm this is the standart procedure->fills square
                ## sets available numbers for square
            self.aNums=self._copy(self.mNums)
            safe=self.fillSquare(len(self.aNums)-1)
        self._sudoku[self.key]=self.square
        if not safe:    ## in case the last algorithm had no success in filling the current squares->prepare for backtracking
            if x_key<1:
                y_key-=1
                x_key=2
            else:
                x_key-=1
        else:    ## sets the yx-coordinates ahead
            if x_key>1:
                y_key+=1
                x_key=0
            else:
                x_key+=1
        self.key=str(y_key)+"_"+str(x_key)  ##updates the key for sudoku hash table
        return self.fillSudoku(safe)    ## calls itself recursively

class DisplaySudoku:
      ##displays the Sudoku in the form of a grid
    def __init__(self, sudoku, x=0, y=0, i=0):
        if y>2:
            return
        result="| "
        for x in range(3):
            self.key=str(y)+"_"+str(x)
            for j in sudoku[self.key][i]:
                if j==None:
                    result+="  "
                else: result+=str(j)+" "
            result+="| "
        print(result)
        if i>1:
            i=0
            y+=1
            print("------------------------")
        else: i+=1
        self.__init__(sudoku, x, y, i)

class CreateSudoku(FillSudoku):
    ## takes blueprint and creates a new lacking Sudoku; takes difficulty
    def __init__(self):
        ## sets a completely empty sudoku grid
        self.blueprint={}
        for i in range(3):
            for j in range(3):
                self.blueprint[str(i)+"_"+str(j)]=[]
                for k in range(3):
                    self.blueprint[str(i)+"_"+str(j)].append([None,None,None])
    def createSudoku(self, difficulty=5):
        ## fills the blueprint with arbitrary numbers
        FillSudoku.__init__(self, self.blueprint)
        newSudoku=FillSudoku.fillSudoku(self)
        for square in newSudoku:
            for i in range(3):
                for j in range(3):
                    num = int(random.random()*10) ## returns an arbitrary integer between 0-9
                    if num < difficulty: ## the larger the difficulty is set; the more numbers get erased
                        newSudoku[square][i][j]=None ## ctreates whitespace to be filled
        return newSudoku

## ____________________________________________________________ ##

print("\nEmpty Sudoku: ")
print(" ________________________")
initSudoku=DisplaySudoku(sudoku)
sudoku=FillSudoku(sudoku)
sudoku.fillSudoku()
print("Filled Sudoku: ")
print(" ________________________")
filledSudoku=DisplaySudoku(sudoku._sudoku)
sudoku=CreateSudoku()
new_sudoku=sudoku.createSudoku(3)
print("Created Sudoku: ")
print(" ________________________")
foo=DisplaySudoku(new_sudoku)
