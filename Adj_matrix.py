

def adj_matrix(matrix, start, end):
  if matrix == []:
  	return False	
  	
  if len(matrix) != len(matrix[0]):
  	return "error not valid matrix"	

  for i in matrix:
  	if len(i) != len(matrix[0]):
  		return "error not valid matrix"	

  for i in matrix:
  	for j in i:
  		if j != 1 and j != 0:
  			return "Not valid input(matrix values must be 0 or 1)"		
  seen = set()
  q = []
  q.append(start)
  while q:
    a = q.pop(0)
    
    for i in range(len(matrix[a])):

      if matrix[a][i] == 1 and i == end:
        return True

      elif matrix[a][i] == 1 and (a,i) not in seen:
        seen.add((a,i))
        
        q.append(i)
  return False


# Once you get the answer you can fill it in then run this file in terminal.
# you should also rename the funciton adj_matrix to something that better describes the function. 
# I can rename after I run it. Don't want it to bug out.
# name your functions better in the future.

#matrix of two with no path from start to end but nodes are connected to themselves
if __name__ == "__main__":
  test_one = {
    "matrix": [
    [1, 0],
    [0, 1]
  ], 
    "start" : 0,
  	"end" : 1,
  	"answer" : False }
  #matrix of two with a path from start to end
  test_two = {
    "matrix": [
    [1, 1],
    [1, 1]
  ], 
    "start" : 0,
  	"end" : 1,
  	"answer" : True}
  #standard undirected graph with a path from start to end	
  test_three = {
    "matrix": [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
  ], 
    "start" : 0,
  	"end" : 3,
  	"answer" : True}
  #standard directed graph with a path from start to end	
  test_four = {
    "matrix": [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
  ], 
    "start" : 0,
  	"end" : 3,
  	"answer" : True}
  #standard directed graph - no path from 0,1,2,3 but has a path from 3,2	
  test_five = {
    "matrix": [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
  ], 
    "start" : 0,
  	"end" : 3,
  	"answer" : False}
  # Non Valid Matrix because it is not n*n	
  test_six = {
    "matrix": [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
  ], 
    "start" : 0,
  	"end" : 3,
  	"answer" : "error not valid matrix"}
  # Matrix of 1	- you can test if the single node is connected to itself or not
  test_seven = {
    "matrix": [
    [1]
  ], 
    "start" : 0,
  	"end" : 0,
  	"answer" : True}
  # Empty matrix - no paths availble	
  test_eight = {
    "matrix": [
    
  ], 
    "start" : 0,
  	"end" : 30,
  	"answer" : False}
  
  # Graph with cycles - seen stops it from infinite looping	
  test_nine = {
    "matrix": [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
  ], 
    "start" : 0,
  	"end" : 3,
  	"answer" : True}
  # Comnpletely disjointed graph - no paths available	
  test_ten = {
    "matrix": [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
  ], 
    "start" : 0,
  	"end" : 2,
  	"answer" : False}  

  # Invalid matrix - not n*n								
  test_eleven = {
    "matrix": [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1]
  ], 
    "start" : 0,
  	"end" : 3,
  	"answer" : "error not valid matrix"}
  # Invalid matrix - not valid input because not 0 or 1	
  test_twelve = {
    "matrix": [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 20],
  ], 
    "start" : 0,
  	"end" : 2,
  	"answer" : "Not valid input(matrix values must be 0 or 1)"}	
		
  answer_one = adj_matrix(test_one['matrix'], test_one['start'], test_one['end'])
  answer_two = adj_matrix(test_two['matrix'], test_two['start'], test_two['end'])
  answer_three = adj_matrix(test_three['matrix'], test_three['start'], test_three['end'])
  answer_four = adj_matrix(test_four['matrix'], test_four['start'], test_four['end'])
  answer_five = adj_matrix(test_five['matrix'], test_five['start'], test_five['end'])
  answer_six = adj_matrix(test_six['matrix'], test_six['start'], test_six['end'])
  answer_seven = adj_matrix(test_seven['matrix'], test_seven['start'], test_seven['end'])
  answer_eight = adj_matrix(test_eight['matrix'], test_eight['start'], test_eight['end'])
  answer_nine = adj_matrix(test_nine['matrix'], test_nine['start'], test_nine['end'])
  answer_ten = adj_matrix(test_ten['matrix'], test_ten['start'], test_ten['end'])
  answer_eleven = adj_matrix(test_eleven['matrix'], test_eleven['start'], test_eleven['end'])
  answer_twelve = adj_matrix(test_twelve['matrix'], test_twelve['start'], test_twelve['end'])
  if answer_one == test_one['answer']:
    print("Passed test one")
  else:
    print("Failed test one")

  if answer_two == test_two['answer']:
    print("Passed test two")
  else:
    print("Failed test two")  
    
  
  if answer_three == test_three['answer']:
    print("Passed test three")
  else:
    print("Failed test three")

  if answer_four == test_four['answer']:
    print("Passed test four")
  else:
    print("Failed test four") 

  if answer_five == test_five['answer']:
    print("Passed test five")
  else:
    print("Failed test five") 
  if answer_six == test_six['answer']:
    print("Passed test six")
  else:
    print("Failed test six")

  if answer_seven == test_seven['answer']:
    print("Passed test seven")
  else:
    print("Failed test seven")

  if answer_eight == test_eight['answer']:
    print("Passed test eight")
  else:
    print("Failed test eight")

  if answer_nine == test_nine['answer']:
    print("Passed test nine")
  else:
    print("Failed test nine") 

  if answer_ten == test_ten['answer']:
    print("Passed test ten")
  else:
    print("Failed test ten")  

  if answer_eleven == test_eleven['answer']:
    print("Passed test eleven")
  else:
    print("Failed test eleven")

  if answer_twelve == test_twelve['answer']:
    print("Passed test twelve")
  else:
    print("Failed test twelve")                         