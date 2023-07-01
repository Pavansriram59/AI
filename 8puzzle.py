import copy
def hf(board_initial,board_final):
    h=0
    for i in range(len(board_initial)):
        for j in range(len(board_final)):
            if(board_initial[i][j]!=board_final[i][j]):
                h+=1
    return h

def findij(state):
  i,j = 0,0
  for i in range(len(state)):
    for j in range(len(state[i])):
      if state[i][j] == 0:
        return i,j
      
    
def puzzle(board_initial,board_final):
    visited,path=[],[]
    g,cost=0,0
    h=hf(board_initial,board_final)
    print(h)
    current=copy.deepcopy(board_initial)
    while True:
        g+=1
        i,j=findij(current)
        temp = copy.deepcopy(current)
        children = []
       
        if j!=0:
            temp[i][j],temp[i][j-1] = temp[i][j-1],temp[i][j]
            children.append([hf(temp,board_final)+g,temp])
            temp = copy.deepcopy(current)

        if j!= len(board_initial)-1:
            temp[i][j],temp[i][j+1] = temp[i][j+1],temp[i][j]
            children.append([hf(temp,board_final)+g,temp])
            temp = copy.deepcopy(current)

        if i!=0:
            temp[i-1][j],temp[i][j] = temp[i][j],temp[i-1][j]
            children.append([hf(temp,board_final)+g,temp])
            temp = copy.deepcopy(current)

        if i!=len(board_initial)-1:
            temp[i+1][j],temp[i][j] = temp[i][j],temp[i+1][j]
            children.append([hf(temp,board_final)+g,temp])
            temp = copy.deepcopy(current)

        children.sort()
        if current == board_final:
            break
        cost += g
        current = children[0][-1]
        path.append(current)
    print(cost)
    print(path)

    

       
    





board_initial=[[2,8,3],[1,6,4],[7,0,5]]
board_final=[[1,2,3],[8,0,4],[7,6,5]]
puzzle(board_initial,board_final)