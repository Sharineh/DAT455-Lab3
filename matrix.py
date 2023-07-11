from  numpy import *
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

def powers(lst,lower_pow,upper_pow):
    
    power_lst = [[0] * (upper_pow-lower_pow+1) for _ in range(len(lst))]
    
    for i in range(len(lst)):
        
        for j in range(lower_pow , upper_pow+1):
            
            power_lst[i][j-lower_pow] = lst[i] ** (j-lower_pow)
            
    return power_lst

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

def invert(M):
    
    if len(M) != 2 and len(M[0]) != 2:
        
        return "The input should be a 2x2 matrix.\n"
    
    else:
        det_m = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        
        inverted_M = [[M[1][1]/det_m, -M[0][1]/det_m],
                      [-M[1][0]/det_m, M[0][0]/det_m]]
        
        return inverted_M
        
def loadtxt(file_name):
    
    result = []
    
    with open(file_name) as file:
        
        for line in file:
            
            row = []
            
            row.append(line .split())
            
            row = [float(element) for element in row[0]]
            
            result.append(row)
            
    return result

            
        
                
                
    

def main():
    
    power_lst = [2,3,4]
    
    print(powers(power_lst,2,4))
    
    #print(matmul(power_lst,matrix))
    
    I3 =[[1,0,0],
         [0,1,0],
         [0,0,1]]
    
    #print(matmul(power_lst,I3))
    
    A = [[1,2],
         [3,4]]
    
    A_inv = invert(A) 
    
    #print(matmul(A,A_inv))
    
    file_name = "chirps.txt"
    
    file_matrix = loadtxt(file_name)
    
    print(file_matrix)
    
if __name__== "__main__":
        
    main()
    