function parityAnalysis(n){
	
	// Your solution here
	let check = n%2;
	let i = 0;
	let ne = 0;
	while(n>0){
		ne = ne + n%10 
		n = (n-n%10)/10;
		
		i++;
	}
	
	
	let response = false;
	if(check == (ne%2))	{response = true}
	return response /* ... true or false */;
}
module.exports = {parityAnalysis}
