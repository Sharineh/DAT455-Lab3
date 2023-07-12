from  numpy import *

# Tanspose a given matirx
def transpose(matrix):
    
    if matrix == [] :
        
        return []
    matrix_rows = len(matrix)
    
    matrix_cols = len(matrix[0])
    
    matrix_transpose = [[0] * matrix_rows for _ in range(matrix_cols)]
    
    for i in range(len(matrix_transpose)):
        
        for j in range(len(matrix_transpose[0])):
            
            matrix_transpose[i][j]= matrix[j][i]
            
    return matrix_transpose

# Compute the powers of a given lst from lower_pow to upper_pow included
def powers(lst,lower_pow,upper_pow):
    
    pow_matrix = []
    
    for enetery in lst :
        
        pow_row = [] 
        
        for j in range(lower_pow , upper_pow+1):
            
            pow_row.append(enetery**j)
            
        pow_matrix.append(pow_row)
        
    return pow_matrix

# Return the result of multiplying two matrices given that the dimenssions are correct
def matmul(m1,m2):
    
    if m1 == [] or m2 == []:
        return []
    
    m1_rows = len(m1)
    
    m2_cols = len(m2[0])
    
    m2_rows = len(m2)
    
    
    result = [[0] * m2_cols for _ in range(m1_rows)]
    
    for i in range(m1_rows):
        
        for j in range(m2_cols):
            
            for k in range(m2_rows):
                
                result[i][j] += m1[i][k] * m2[k][j]
                
    return result

# Invert a 2x2 matrix
def invert(M):
    
        det_m = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        
        inverted_M = [[M[1][1]/det_m, -M[0][1]/det_m],
                      [-M[1][0]/det_m, M[0][0]/det_m]]
        
        return inverted_M

# Load txt from file_name and return it as a matrix

def loadtxt(file_name):
    
    result = []
    
    with open(file_name) as file:
        
        for line in file:
            
            row = []
            
            row.append(line .split())
            
            row = [float(element) for element in row[0]]
            
            result.append(row)
            
    return result

    