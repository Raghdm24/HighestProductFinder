################################################## Import ##################################################
import math
#################################################Functions#################################################
def CanProductRight(col):
    return True if col + Neighbors -1 < MatrixSize and col >= 0 else False

def CanProductLeft(col):
    return True if col - Neighbors + 1 >= 0 and col < MatrixSize else False

def CanProductDown(row):
    return True if row + Neighbors - 1 < MatrixSize and row < MatrixSize else False

def CanProductUp(row):
    return True if row - Neighbors + 1 >= 0 and row >= 0 else False

def CanProductDiagonalRightU(col,row):
    return True if CanProductRight(col) and CanProductUp(row) else False

def CanProductDiagonalLeftU(col,row):
    return True if CanProductLeft(col) and CanProductUp(row) else False

def CanProductDiagonalLeftD(col,row):
    return True if CanProductLeft(col) and CanProductDown(row) else False

def CanProductDiagonalRightD(col,row):
    return True if CanProductRight(col) and CanProductDown(row) else False

def PointRight(col,row):
    return numMatrix[row][col:col+Neighbors] if CanProductRight(col) else [0] * Neighbors

def PointLeft(col,row):
    return numMatrix[row][col-Neighbors +1:col+1] if CanProductLeft(col) else [0]*Neighbors


def PointUp(col,row):
    if CanProductUp(row):
        list = []
        for i in range(row-Neighbors+1,row+1):
            list.append(numMatrix[i][col])
        return list
    else:
        return [0] * Neighbors

def PointDown(col,row):
    if CanProductDown(row):
        list =[]
        for i in range(row,row+Neighbors):
            list.append(numMatrix[i][col])
        return list
    else:
        return [0] * Neighbors

def PointDiagonalRightUP(col,row):
    if CanProductDiagonalRightU(col,row):
        list=[]
        for i in range(col,col+Neighbors):
            list.append(numMatrix[row][i])
            row -= 1
        return list
    else:
        return [0]*Neighbors

def PointDiagonalLeftUp(col,row):
    if CanProductDiagonalLeftU(col,row):
        list = []
        for i in range(col-Neighbors +1,col+1):
            list.append(numMatrix[row+1-Neighbors][i])
            row = row+1
        return list
    else:
        return [0]*Neighbors

def PointDiagonalLeftDown(col,row):
    if CanProductDiagonalLeftD(col,row):
        list = []
        for i in range(col-Neighbors +1,col+1):
            list.append(numMatrix[row-1+Neighbors][i])
            row= row -1
        return list
    else:
        return [0]*Neighbors

def PointDiagonalRightDown(col,row):
    if CanProductDiagonalRightD(col,row):
        list= []
        for i in range(col,col+Neighbors):
            list.append(numMatrix[row][i])
            row = row + 1
        return list
    else:
        return [0]*Neighbors

def mul(list):
    return math.prod(list)

def mulAll():
    allList = []
    for r in range(0,MatrixSize):
        for c in range(0,MatrixSize):
            cellList = []
            cellList.append(mul(PointRight(c,r)))
            cellList.append(mul(PointLeft(c,r)))
            cellList.append(mul(PointUp(c,r)))
            cellList.append(mul(PointDown(c,r)))
            cellList.append(mul(PointDiagonalRightUP(c,r)))
            cellList.append(mul(PointDiagonalRightDown(c,r)))
            cellList.append(mul(PointDiagonalLeftUp(c,r)))
            cellList.append(mul(PointDiagonalLeftDown(c,r)))

            index = GetHighestIndex(cellList)
            direction = switcher(index)

            allList.append([cellList[index], direction , (c,r)])
    return allList

def GetHighestIndex(list):
    return list.index(max(list))

def switcher(x):
    return {
        0:'right',
        1:'left',
        2: 'up',
        3: 'down',
        4: 'rightUp',
        5: 'rightDown',
        6: 'leftUp',
        7: 'leftDown',
    }[x]

def RunAllTests():
    if TestCanProductRight()==False:
        return "TestCanProductRight,fails during test"
    if TestCanProductLeft()==False:
        return "TestCanProductLeft , fails during test"
    if TestCanProductDown()==False:
        return "TestCanProductDown, fails during test"
    if TestCanProductUp()==False:
        return "TestCanProductUp , fails during test"

    if TestCanProductDiagonalRightU()==False:
        return "TestCanProductDiagonalRightU , fails during test"
    if TestCanProductDiagonalLeftU()==False:
        return "TestCanProductDiagonalLeftU , fails during test"
    if TestCanProductDiagonalLeftD()==False:
        return "TestCanProductDiagonalLeftD, fails during test"
    if TestCanProductDiagonalRightD()==False:
        return "def TestCanProductDiagonalRightD, fails during test"

    if TestPointRight()==False:
        return "TestPointRight , fails during test"
    if TestPointLeft()==False:
        return "TestPointLeft , fails during test"
    if TestPointUp()==False:
        return "TestPointUp , fails during test"
    if TestPointDown()==False:
        return "TestPointDown , fails during test"

    if TestPointDiagonalRightUP()==False:
        return "TestPointDiagonalRightUP , fails during test"
    if TestPointDiagonalRightDown()==False:
        return "TestPointDiagonalRightDown , fails during test"
    if TestPointDiagonalLeftUp()==False:
        return "TestPointDiagonalLeftUp , fails during test"
    if TestPointDiagonalLeftDown()==False:
        return "TestPointDiagonalLeftDown , fails during test"

    if TestMul()==False:
        return "Testmul ,fails during test"
    if TestGetHighestIndex()==False:
        return "GetHighestIndex , fails during test"

    return "All test passed , there is no errors"

#################################################Statics##################################################
MatrixSize = 20
Neighbors = 4

someWierdInput = "99 00 99 99 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n"
someWierdInput +="49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n"
someWierdInput +="81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n"
someWierdInput +="52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n"
someWierdInput +="22 31 16 71 51 67 63 89 41 92 36 54 22 99 40 28 66 33 13 80\n"
someWierdInput +="24 47 32 60 99 03 45 02 44 75 33 53 00 36 84 20 35 17 12 50\n"
someWierdInput +="32 98 81 28 64 23 67 10 26 38 40 99 59 54 70 66 18 38 64 70\n"
someWierdInput +="67 26 20 99 99 00 99 20 95 63 99 39 63 08 40 91 66 49 94 21\n"
someWierdInput +="24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n"
someWierdInput +="21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n"
someWierdInput +="78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n"
someWierdInput +="16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n"
someWierdInput +="86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n"
someWierdInput +="19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 99 89 55 40\n"
someWierdInput +="04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 00 27 98 66\n"
someWierdInput +="88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 99 93 53 69\n"
someWierdInput +="04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 23 62 76 36\n"
someWierdInput +="20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n"
someWierdInput +="20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n"
someWierdInput +="01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
################################################## Tests ##################################################
def TestCanProductRight():
  if CanProductRight(16) !=True:
      return False
  if CanProductRight(17) !=False:
     return False
  if CanProductRight(5) !=True:
     return False
  if CanProductRight(20)!=False:
     return False
  if CanProductRight(-1)!=False:
     return False
  return True

def TestCanProductLeft():
  if CanProductLeft(3)!=True:
      return False
  if CanProductLeft(2)!=False:
      return False
  if CanProductLeft(8)!=True:
      return False
  if CanProductLeft(0)!=False:
    return False
  if CanProductLeft(20)!=False:
      return False
  if CanProductLeft(4)!=True:
      return False
  return True

def TestCanProductDown():
  if CanProductDown(16)!=True:
      return False
  if CanProductDown(18)!=False:
      return False
  if CanProductDown(8)!=True:
      return False
  if CanProductDown(17)!=False:
    return False
  if CanProductDown(20)!=False:
      return False
  return True

def TestCanProductUp():
  if CanProductUp(3)!=True:
      return False
  if CanProductUp(1)!=False:
      return False
  if CanProductUp(15)!=True:
      return False
  if CanProductUp(2)!=False:
      return False
  if CanProductUp(-1)!=False:
      return False
  return True

def TestCanProductDiagonalRightU():
    if CanProductDiagonalRightU(17,2)!=False:
        return False
    if CanProductDiagonalRightU(3,17)!=True:
        return False
    if CanProductDiagonalRightU(3,16)!=True:
        return False
    if CanProductDiagonalRightU(18,3)!=False:
        return False
    if CanProductDiagonalRightU(0,0)!=False:
        return False
    return True

def TestCanProductDiagonalLeftU():
    if CanProductDiagonalLeftU(4,4)!=True:
        return False
    if CanProductDiagonalLeftU(2,2)!=False:
        return False
    if CanProductDiagonalLeftU(0,0)!=False:
        return False
    if CanProductDiagonalLeftU(3,16)!=True:
        return False
    if CanProductDiagonalLeftU(13,15)!=True:
        return False
    if CanProductDiagonalLeftU(2, 3)!=False:
        return False
    return True

def TestCanProductDiagonalLeftD():
    if CanProductDiagonalLeftD(3,3)!=True:
        return False
    if CanProductDiagonalLeftD(0,2)!=False:
        return False
    if CanProductDiagonalLeftD(3,0)!=True:
        return False
    if CanProductDiagonalLeftD(16,3)!=True:
        return False
    if CanProductDiagonalLeftD(2,16)!=False:
        return False
    return True

def TestCanProductDiagonalRightD():
    if CanProductDiagonalRightD(16,16)!=True:
        return False
    if CanProductDiagonalRightD(17,15)!=False:
        return False
    if CanProductDiagonalRightD(16,18)!=False:
        return False
    if CanProductDiagonalRightD(6,12)!=True:
        return False
    if CanProductDiagonalRightD(17,0)!=False:
        return False
    return True

def TestPointRight():
    if PointRight(3,2)!=[73, 55, 79, 14]:
        return False
    if PointRight(18,6)!=[0,0,0,0]:
        return False
    if PointRight(6,12)!=[89, 7, 5, 44]:
        return False
    if PointRight(19,17)!=[0,0,0,0]:
        return False
    return True

def TestPointLeft():
    if PointLeft(3,5)!=[24,47,32,60]:
        return False
    if PointLeft(0,0)!=[0,0,0,0]:
        return False
    if PointLeft(3,2)!=[81,49,31,73]:
        return False
    if PointLeft(2,10)!=[0,0,0,0]:
        return False
    return True

def TestPointUp():
    if PointUp(5,3)!=[15,81,79,60]:
        return False
    if PointUp(0,2)!=[0,0,0,0]:
        return False
    if PointUp(10,7)!=[36,33,40,94]:
        return False
    if PointUp(19,0)!=[0,0,0,0]:
        return False
    return True

def TestPointDown():
    if PointDown(0,16)!=[4,20,20,1]:
        return False
    if PointDown(10,18)!=[0,0,0,0]:
        return False
    if PointDown(2,15)!=[68,16,36,35]:
        return False
    if PointDown(19,19)!=[0,0,0,0]:
        return False
    return True


def TestPointDiagonalLeftUp():
    if PointDiagonalLeftUp(5,5)!=[31,23,51,3]:
        return False
    if PointDiagonalLeftUp(0,0)!=[0,0,0,0]:
        return False
    if PointDiagonalLeftUp(4,8)!=[47,81,68,66]:
        return False
    if PointDiagonalLeftUp(2,11)!=[0,0,0,0]:
        return False
    return True

def TestPointDiagonalLeftDown():
    if PointDiagonalLeftDown(19,19,)!=[0,0,0,0]:
        return False
    if PointDiagonalLeftDown(1,1)!=[0,0,0,0]:
        return False
    if PointDiagonalLeftDown(3,2)!=[24,31,95,73]:
        return False
    if PointDiagonalLeftDown(19,0)!=[37,13,62,8]:
        return False
    return True

def TestPointDiagonalRightUP():
    if PointDiagonalRightUP(5,5)!=[3,63,42,93]:
        return False
    if PointDiagonalRightUP(0,0)!=[0,0,0,0]:
        return False
    if PointDiagonalRightUP(0,3)!=[52,49,99,97]:
        return False
    if PointDiagonalRightUP(8,0)!=[0,0,0,0]:
        return False
    return True

def TestPointDiagonalRightDown():
    if PointDiagonalRightDown(0,0)!=[8,49,31,23]:
        return False
    if PointDiagonalRightDown(19,19)!=[0,0,0,0]:
        return False
    if PointDiagonalRightDown(16,5,)!=[35,38,94,72]:
        return False
    if PointDiagonalRightDown(17,2)!=[0,0,0,0]:
        return False
    return True

def TestMul():
    if mul([0,0,0,0])!=0:
        return False
    if mul([23,6,44,0])!=0:
        return False
    if mul([99,3,55,7])!=114345:
        return False
    if mul([1,5,2,2])!=20:
        return False

    return True

def TestGetHighestIndex():
    if GetHighestIndex([3,6,2,78])!=3:
        return False
    if GetHighestIndex([100,101,234,0,899,3,9,11,22]) != 4:
        return False
    if GetHighestIndex([4500,5500,6666,77,99,99887])!=5:
        return False
    if GetHighestIndex([3500,6600,700,200,4000,55,66])!=1:
        return False
    return True

##################################################main#######################################################
rows = someWierdInput.split("\n")
if len(rows) > MatrixSize:
    print("The number of rows is not equal to the fixed set-size: " + str(MatrixSize))

numMatrix = []

for row in rows:
    rowNums = row.split(" ")
    rowNums = [int(numeric_string) for numeric_string in rowNums]

    if len(rowNums) > MatrixSize:
        print("The following row has INCORRECT length: " + str(rowNums))

    numMatrix.append(rowNums)


#for row in numMatrix:
 #   print(row)

###############################################################################################################

#print(Testret())
#print(RunAllTests())

list= mulAll()
newList = max(list)
print(newList)
Cc= newList[2][0]
Rr= newList[2][1]
Dd= newList[1]

def direction(Dd):
    return {
        'right': PointRight(Cc,Rr),
        'left' : PointLeft(Cc,Rr),
        'up'   : PointUp(Cc,Rr),
        'down' : PointDown(Cc,Rr),
        'rightUp': PointDiagonalRightUP(Cc,Rr),
        'rightDown': PointDiagonalRightDown(Cc,Rr),
        'leftUp': PointDiagonalLeftUp(Cc,Rr),
        'leftDown': PointDiagonalLeftDown(Cc,Rr),
    }[Dd]

FourValues = direction(Dd)
index = list.index(newList)
print("\n" + "The highest value within the matrix is =" + str(newList[0]),"\n" + "The index in the matrix is :" + str(index), "\n" + "Column and Row in order" + str(newList[2]) ,"\n" + "The direction : " + str(newList[1]) ,"\n" + "The 4 values of the highest product is: " + str(FourValues) )


'''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

'''





