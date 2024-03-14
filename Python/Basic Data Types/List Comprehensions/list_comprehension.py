# List Comprehensions

# we have to print all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.
# the conditions are:
# 0 <= i <= x
# 0 <= j <= y
# 0 <= k <= z

# Using list comprehensions, create lists of i,j,k of all possible coordinates. Then, print the list of coordinates that satisfy where sum of i+j+k is not equal to n.
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])