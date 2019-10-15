#The hardest sudoku board
board=[[8,0,0,0,0,0,0,0,0],
       [0,0,3,6,0,0,0,0,0],
       [0,7,0,0,9,0,2,0,0],
       [0,5,0,0,0,7,0,0,0],
       [0,0,0,0,4,5,7,0,0],
       [0,0,0,1,0,0,0,3,0],
       [0,0,1,0,0,0,0,6,8],
       [0,0,8,5,0,0,0,1,0],
       [0,9,0,0,0,0,4,0,0]]

#Backtracking Algorithm implementer
def solve(mat):
    if find_empty(mat):
        row, col = find_empty(mat)
    else:
        return True


    for i in range(1,10):
        if IsValid(mat, i, (row,col)):
            mat[row][col]=i

            if solve(mat):
                return True

            mat[row][col]=0

    return False

def IsValid(mat,num,pos):

    #check row validity
    for i in range(0,9):
        if mat[pos[0]][i] == num and pos[1]!=i:
            return False
    #check column validity
    for i in range(0,9):
        if mat[i][pos[1]]== num and pos[0]!=i:
            return False

    #box position
    box_x=pos[1]//3
    box_y=pos[0]//3

    #check box validity
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if mat[i][j] == num and (i,j) != pos:
                return False

    return True


#prints the current version of board
def show_board(mat):

    for i in range(9):
        if i%3==0 and i!=0:
            print('----------------------')
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('|', end=" ")
            print(mat[i][j], end=" ")
        print()


#finds empty positions in the board
def find_empty(mat):
    for i in range(0,9):
        for j in range(0,9):
            if mat[i][j]==0:
                return (i,j)
    return None


#function call
show_board(board)
print('_____________________')
print()
solve(board)
show_board(board)

