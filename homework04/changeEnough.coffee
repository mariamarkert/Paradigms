changeEnough = (changeInPocket, amount) -> 
	# Your
	# Function
	# implementation
	# here
	ret = false;
	totalChange = changeInPocket[0]*.25+changeInPocket[1]*.1+changeInPocket[2]*.05+changeInPocket[3]*.01;
	if totalChange>=amount
		 ret = true;
	return ret;


# Keep the line below so we can test your code!
module.exports = { changeEnough }
