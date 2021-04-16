two_D_matrix = [[-4, -3, -1, 1], [-2, -2,1, 2], [-1, 1, 2, 3], [1,2,4,5]]
count = 0 
for row in two_D_matrix:
    print('\n')  
    for element in row:
        print(element, end=" ")
        if element < 0:
            count  = count + 1
            
               
print('\n')    
print('The number of negative numbers is' , count)
