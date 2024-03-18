if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newList = [] # Create a new list to store the values
    
    for i in arr:
        newList.append(i)
        
    newList.sort()
    newList = list(dict.fromkeys(newList)) # Remove duplicates
    print(newList[-2]) # Print the second last element