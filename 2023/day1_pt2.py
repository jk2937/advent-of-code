 #  day1_pt2.py

debug_enabled = True
debug_pause = False
def debug_print(*args):
    global debug_enabled
    if debug_enabled == False:
        return
    print("DEBUG -", *args)

    global debug_pause
    if debug_pause == True:
        input("DEBUG - Press enter to continue")

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
    debug_print("Begin loop")
    left_digit = None
    right_digit = None
    two_digit_number = None

    debug_print("Printing arr[i] -", arr[i])

    line = arr[i]
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    arr[i] = line

    debug_print("Printing arr[i] -", arr[i])

    #  Loop over each character from left
    for j in range(len(arr[i])):
        debug_print("Loop over each character from left")
        debug_print("Print arr[i][j] -", arr[i][j])

        #  If the character is a number 
        if arr[i][j] in [str(num) for num in range(10)]:
            debug_print( "Assign left_digit to int(arr[i][j]) -", int(arr[i][j]) )
            left_digit = int(arr[i][j])
            break

    #  Loop over each character from right
    for j in range( len(arr[i]) - 1 , -1, -1): 
        debug_print("Loop over each character from right")
        # If the character is a number
        if arr[i][j] in [str(num) for num in range(10)]:
            debug_print( "Assign right_digit to int(arr[i][j]) -", int(arr[i][j]) )
            right_digit = int(arr[i][j])
            break

     #  Concatenate left_digit and right_digit
    two_digit_number = int( str(left_digit) + str(right_digit) )
    debug_print("Print two_digit_number -", two_digit_number)

     #  Add the two digit number to the total
    calibration_values_sum = calibration_values_sum + two_digit_number

debug_print("Print calibration_values_sum -", calibration_values_sum)
