import numpy as np
def transpose(matrix):
    
    matrix_rows = len(matrix)
    
    matrix_cols = len(matrix[0])
    
    matrix_transpose = [[0] * matrix_rows for _ in range(matrix_cols)]
    
    for i in range(len(matrix_transpose)):
        
        for j in range(len(matrix_transpose[0])):
            
            matrix_transpose[i][j]= matrix[j][i]
            
    return matrix_transpose

def powers(lst,lower_pow,upper_pow):
    
    power_lst = [[0] * (upper_pow-lower_pow+1) for _ in range(len(lst))]
    
    for i in range(len(lst)):
        
        for j in range(lower_pow , upper_pow+1):
            
            power_lst[i][j-lower_pow] = lst[i] ** j
            
    return power_lst

def main():
    
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]]
    
    np_matrix = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])
    
    power_lst = [1,2,3,4]
    
    print(powers(power_lst,2,4))
    
    
main()
    