def first_x_fibonocci_for(x):
    prev_number = 0 
    curr_number = 1
    print(prev_number)
    print(curr_number)

    for count in range(2, x + 1):
        next_num = curr_number + prev_number
        print(next_num)

        prev_number = curr_number
        curr_number = next_num

first_x_fibonocci_for(17)