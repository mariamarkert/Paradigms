
n = ARGV

i0 = 0
i1 = 1
i = 1

def fib(f1, f0, n)
	
	if n < 0 
		print "\n"
		return
	end
	print "%d " % [f0]
	n  = n-1;
	fib( f1 + f0, f1, n)

end

if ARGV.length != 1
	STDERR.puts 'Error'
	exit 1
end
fib(1, 0, ARGV[0].to_i)
