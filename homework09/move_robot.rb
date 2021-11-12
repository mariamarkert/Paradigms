def fibonacci_array( array, n )

	array[0] = 1
	if n == 1 
		return
	end	
	array[1] = 1
	i = 2

	while i < n
		array[i] = array[i-1] + array[i-2]
		i+=1
	end

	return array
end

def move_robot(array)
	x = 0
	y = 0
	i = 0
	
	for item in array
		case i 
		when 0
			y = y + item
			i+=1
		when 1
			x = x + item
			i+=1
		when 2
			y = y - item
			i+=1
		when 3
			x = x - item
			i = 0
		end
		
	end
	return [x,y]
end



n = ARGV[0]
array = []

array = fibonacci_array( array, n.to_i )

x,y = move_robot(array)
puts("( "+x.to_s+" , "+y.to_s+" )")
