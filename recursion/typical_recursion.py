# Go through an array and print out all of the elements
def print_list_recursively(arr, index=0):
    if index == len(arr):
        return

    print(arr[index])

    print_list_recursively(arr, index + 1)

# Determine whether or not a string is a palindrome
def check_palindrome(text, length, index):
    if index == length // 2:
        return True

    if text[index] != text[length - 1 - index]:
        return False

    return check_palindrome(text, length, index + 1)

# Calculate a raised to the power of b
def power_calculation(number, power):
    if power == 0:
        return 1

    return number * power_calculation(number, power - 1)
# Extra credit: Try implementing the map function (the one that transforms arrays) without using loops

def generate_pascals_triangle(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    l = []
    for i in range(1, numRows+1):
        l.append([0]*i)
    
    generate_triange_recursively(l, 0, 0, numRows)
    
    return l
    
def generate_triange_recursively(l, i, j, numRows):
    if j == numRows:
        return
    if i== 0 or i == j:
        print("i={} j={}".format(i, j))
        l[j][i] = 1
    else:
        if j >= 2:
            l[j][i] = l[j-1][i-1]+l[j-1][i]
    
    generate_triange_recursively(l, i, j+1, numRows)
    generate_triange_recursively(l, i+1, j+1, numRows)