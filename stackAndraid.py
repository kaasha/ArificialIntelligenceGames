from copy import deepcopy
#import pdb
import time
player_main=""
player2_opp=""
def output(move,move_type,board_state,n):
  fdw = open('output.txt','w')
  fdw.write('{} {}{}'.format(move,move_type,'\n'))
  for i in range(n):
    for j in range(n):
      fdw.write('{}'.format(board_state[i][j]))
    fdw.write('{}'.format('\n'))
  fdw.close()

def get_gamescore(inp_matrix,cur_state,n):
  sum_x=0
  sum_y=0
  for i in range(n):
    for j in range(n):
      if cur_state[i][j]=='X':
        sum_x=sum_x+inp_matrix[i][j]
      elif cur_state[i][j]=='O':
        sum_y=sum_y+inp_matrix[i][j]
  if player_main=='X':
    return sum_x-sum_y
  else:
    return sum_y-sum_x

  
def actions(player,inp_matrix,cur_state,n):
  if player == 'X':
    player2='O'
  else:
    player2='X'
  flag1=0
  flag2=0
  flag3=0
  flag4=0
  #print "Player"
  #print player
  list_of_actions=[]
  for i in range(n):
    for j in range(n):
      if cur_state[i][j]=='.':
        cur_state[i][j]= player
        #print cur_state
        
        list_of_actions.append((i,j,"Stake",deepcopy(cur_state)))
        #print list_of_actions
        cur_state[i][j]='.'
    
  for i in range(n):
    for j in range(n):
      if cur_state[i][j]=='.' and ((i>0 and cur_state[i-1][j]==player) or (i<n-1 and cur_state[i+1][j]==player) or (j<n-1 and cur_state[i][j+1]==player) or (j>0 and cur_state[i][j-1]==player)):
        cur_state[i][j]=player
        if j<n-1 and cur_state[i][j+1]==player2:
          flag1=1
          cur_state[i][j+1]=player
        if i<n-1 and cur_state[i+1][j]==player2:
          flag2=1
          cur_state[i+1][j]=player
        if i>0 and cur_state[i-1][j]==player2:
          flag3=1
          cur_state[i-1][j]=player
        if j>0 and cur_state[i][j-1]==player2:
          flag4=1
          cur_state[i][j-1]=player
        if flag1 or flag2 or flag3 or flag4:
          list_of_actions.append((i,j,"Raid",deepcopy(cur_state)))
        if flag1:
          cur_state[i][j+1]=player2
          flag1=0
        if flag2:
          cur_state[i+1][j]=player2
          flag2=0
        if flag3:
          cur_state[i-1][j]=player2
          flag3=0
        if flag4:
          cur_state[i][j-1]=player2
          flag4=0
          
        
        
        cur_state[i][j]='.'
        
     
      
  return list_of_actions
          

def findBestMovemm(depth,inp_matrix,cur_state,n):
  bestMove={}
  bestval= float('-inf')
  action_list=actions(player_main,inp_matrix,cur_state,n)
  for (i,j,move,ele) in action_list:
    #print action_list
    val = minimax(depth,inp_matrix,deepcopy(ele),0,n,1)
    if val>bestval:
      bestMove["row"]=i
      bestMove["col"]=j
      bestMove["move"]=move
      bestval=val
      bestMove["val"]=bestval
      bestMove["ele"]=ele
  return bestMove

def findBestMoveab(depth,inp_matrix,cur_state,n):
  bestMove={}
  bestval= float('-inf')
  action_list=actions(player_main,inp_matrix,cur_state,n)
  for (i,j,move,ele) in action_list:
    #print action_list
    val = alphabeta(depth,inp_matrix,deepcopy(ele),0,n,1,float('-inf'),float('inf'))
    if val>bestval:
      bestMove["row"]=i
      bestMove["col"]=j
      bestMove["move"]=move
      bestval=val
      bestMove["val"]=bestval
      bestMove["ele"]=ele
  return bestMove

def alphabeta(depth,inp_matrix,cur_state,maxPlayer,n,cur_depth,alpha,beta):
  #if player=='X':
  #  player2="O"
  #else:
  #  player2="X"
  #pdb.set_trace()
  if cur_depth == int(depth) or is_full(cur_state,n):
    return  get_gamescore(inp_matrix,deepcopy(cur_state),n)
  if maxPlayer:
    best = float('-inf')
    #print "In MAX"
    #print "Depth"
    #print cur_depth
    #print "Player Main"
    #print player_main
    action_list=actions(player_main,inp_matrix,deepcopy(cur_state),n)
    #print action_list
    for (i,j,move,ele) in action_list: 
      v = alphabeta(depth,inp_matrix,deepcopy(ele),0,n,cur_depth+1,alpha,beta)
      best = max(best,v)
      alpha = max(alpha, best)
      if beta<=alpha:
        break
    return best
  else:
    best = float('inf')
    #print "In MIN"
    #print "Depth"
    #print cur_depth
    #print "Player_opp"
    #print player2_opp
    action_list=actions(player2_opp,inp_matrix,deepcopy(cur_state),n)
    #print action_list
    for (i,j,move,ele) in action_list:
      v = alphabeta(depth,inp_matrix,deepcopy(ele),1,n,cur_depth+1,alpha,beta)
      best = min(best,v)
      beta = min(beta,best)
      if beta<=alpha:
        break
    return best

def is_full(cur_state,n):
  for i in range(n):
    for j in range(n):
      if cur_state[i][j]=='.':
        return 0
  return 1
      

def minimax(depth,inp_matrix,cur_state,maxPlayer,n,cur_depth):
  #if player=='X':
  #  player2="O"
  #else:
  #  player2="X"
  #pdb.set_trace()
  if cur_depth == int(depth) or is_full(cur_state,n):
    return  get_gamescore(inp_matrix,deepcopy(cur_state),n)
  if maxPlayer:
    best = float('-inf')
    #print "In MAX"
    #print "Depth"
    #print cur_depth
    #print "Player Main"
    #print player_main
    action_list=actions(player_main,inp_matrix,deepcopy(cur_state),n)
    #print action_list
    for (i,j,move,ele) in action_list: 
      v = minimax(depth,inp_matrix,deepcopy(ele),0,n,cur_depth+1)
      best = max(best,v)
      #print "Best,v"
      #print best,v
    return best
  else:
    best = float('inf')
    #print "In MIN"
    #print "Depth"
    #print cur_depth
    #print "Player_opp"
    #print player2_opp
    action_list=actions(player2_opp,inp_matrix,deepcopy(cur_state),n)
    #print action_list
    for (i,j,move,ele) in action_list:
      v = minimax(depth,inp_matrix,deepcopy(ele),1,n,cur_depth+1)
      best = min(best,v) 
      #print "Best,v"
      #print best,v
    return best
  
    
if __name__=='__main__':
  start=time.time()
  fd= open('input.txt','r')
  input_list= fd.readlines()
  n=int(input_list[0].strip('\n'))
  algo=input_list[1].strip('\n')
  #global player_main
  player_main=input_list[2].strip('\n')
  #global player2_opp
  if player_main=="X":
    player2_opp="O"
  else:
    player2_opp="X"
  depth=input_list[3].strip('\n')
  inp_matrix=[]
  
  for i in range(n):
    #print i
    #inp_matrix[i]=[]
    row =[]
    values=(input_list[4+i].strip('\n')).split(' ')
    for ele in values:
      row.append(int(ele))
    inp_matrix.append(row)
 
      
      
    #for j in range(n):
      #inp_matrix[i][j]=values[j]
  cur_state=[]
  for i in range(n):
    row=[]
    values=list(input_list[4+i+n].strip('\n'))
    for ele in values:
      row.append(ele)
    cur_state.append(row)
      
  #print input
  #print "INPUT"
  #for i in range(n):
  #  for j in range(n):
  #    print inp_matrix[i][j],
  #  print ""
    
  #for i in range(n):
  #  for j in range(n):
  #    print cur_state[i][j],
  #  print ""
  
  #print Trial  
  #output("F22","stake",cur_state,n)
  #i,j,maxi=get_max_unoccupied(inp_matrix,cur_state,n)
  #print i,j,maxi
  #print get_gamescore('X',inp_matrix,cur_state,n)
  
  #print is_full(cur_state,n)
  #print actions(player_main,inp_matrix,cur_state,n)
  
  if algo=="MINIMAX":
    #print depth
    #row,col,move_type=minimaxDecision(player,inp_matrix,cur_state,n)
    #best,row,col,move_type=minimax(player,int(depth),inp_matrix,cur_state,1,n)
    #for (i,j,move,ele) in actions(player,inp_matrix,cur_state,n):
    bestMove=findBestMovemm(depth,inp_matrix,cur_state,n) 
    row=bestMove['row']
    col=bestMove['col']
    row= row+1
    move_type=bestMove['move']
    new_state=deepcopy(bestMove['ele'])
    #print bestMove['val']
    #print row,col
    col=chr(col + ord('A'))
    move=col+str(row)
    #print move
    output(move,str(move_type),new_state,n)
  elif algo=="ALPHABETA":
    bestMove=findBestMoveab(depth,inp_matrix,cur_state,n) 
    row=bestMove['row']
    col=bestMove['col']
    row= row+1
    move_type=bestMove['move']
    new_state=deepcopy(bestMove['ele'])
    #print bestMove['val']
    #print row,col
    col=chr(col + ord('A'))
    move=col+str(row)
    #print move
    output(move,str(move_type),new_state,n)
  else:
    print "ERROR!"
  end=time.time()
  print end-start
    #print get_gamescore('O',inp_matrix,new_state,n)
