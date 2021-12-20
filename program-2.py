import math 
  
def isPerfectSquare(num): 
  
    n = int(math.sqrt(num)) 
    return (n * n == num) 
  
   
def checkFib(array, n): 
  
    count = 0
    for i in range(n): 
      
        if (isPerfectSquare(5 * array[i] * array[i] + 4) or 
            isPerfectSquare(5 * array[i] * array[i] - 4)): 
          
            print(array[i], " ", end =""); 
            count = count + 1
          
      
    if (count == 0): 
        print("None present"); 
  
  
array = [1, 7, 11, 18, 29, 47, 0, 8, -1, 0, 1, 1, 2, 3, 5, 8, 13, -10, 4, 10]
n = len(array) 
   
checkFib(array, n) 