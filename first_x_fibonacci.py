def first_x_fibonacci(x):
	prev_number = 0 
	curr_number = 1
	count = 2 
	print(prev_number)
	print(curr_number)

	while count <= x:
		next_num = curr_number + prev_number
		print(next_num)
		prev_number=curr_number
		curr_number=next_num
		count +=1
		

a = 17
print('First %d Fibonacci numbers' %a)
first_x_fibonacci(a)
