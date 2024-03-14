# Print Function Solution
# Sample Input
# 3
# Sample Output
# 123

# Though process:
# define a variable a and assign it an empty string
# iterate through the range of 1 to n+1 and concatenate the string representation of each number to a
if __name__ == '__main__':
    n = int(input())
    a = "" 
    for i in range(1,n+1):
        a += str(i)
        
    print(a)