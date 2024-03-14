# Loops Solution
# Sample Input
# 3
# Sample Output
# 0
# 1
# 4
# Thought Process:
# Use the range(n) function to create a list of integers from 0 to n-1. On the new line, print each element of the list squared.

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)