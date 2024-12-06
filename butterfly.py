def print_butterfly(n):
    #Print upper half of the butterfly
    for i in range(n):
        print(
            '*' * (i + 1) + ' ' * (n - i - 1) +
            ' ' * (n - i - 1) + '*' * (i + 1)
        )
    #Print lower half of the butterfly
    for i in range(n -2, -1, -1):
        print(
            '*' * (i + 1) + ' ' * (n - i - 1) +
            ' ' * (n - i - 1) + '*' * (i + 1)
        )
    #Call the function to print the butterfly
print_butterfly(5)

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

