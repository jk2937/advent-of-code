 #  Open the puzzle input
_str = open("puzzle_input_1.txt", "r").read()
arr = _str.split("\n")

 #  Remove empty list items
arr2 = []
for i in range(len(arr)):
    if arr[i] != "":
        arr2.append(arr[i])

arr = arr2
arr2 = None

calibration_values_sum = 0

#  Loop over each line 
for i in range(len(arr)): 
    left_digit = None
    right_digit = None
    two_digit_number = None

    #  Loop over each character from left
    for j in range(len(arr[i])): 

        #  If the character is a number 
        if arr[i][j] in [str(num) for num in range(10)]:
            left_digit = int(arr[i][j])
            break

    #  Loop over each character from right
    for j in range( len(arr[i]) - 1 , -1, -1): 

        # If the character is a number
        if arr[i][j] in [str(num) for num in range(10)]:
            right_digit = int(arr[i][j])
            break

     #  Concatenate left_digit and right_digit
    two_digit_number = int( str(left_digit) + str(right_digit) )

     #  Add the two digit number to the total
    calibration_values_sum = calibration_values_sum + two_digit_number

print(calibration_values_sum)
