def surfaceArea(A):
    surface = 0
    
    for i in range(1, len(A)):
        for j in range(0, len(A[i])):
            surface += abs(A[i][j] - A[i - 1][j])
            
    print(surface)
            
    for i in range(0, len(A)):
        for j in range(1, len(A[i])):
            surface += abs(A[i][j] - A[i][j - 1])
            
    print(surface)
            
    surface += len(A) * len(A[0]) * 2
    surface += sum(A[0])
    surface += sum(A[-1])
    surface += sum([x[0] for x in A])
    surface += sum([x[-1] for x in A])
            
    return surface