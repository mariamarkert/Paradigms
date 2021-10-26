
n = ARGV

i0 = 0
i1 = 1
i = 1

def fib(n)

	f0, f1 = 0, 1
	print "%d " % [f0]

	print "%d " % [f1]

	
	for a in 1...n.to_i do
	
		f0, f1 = f1, f0 + f1
		print "%d " % [f1]

	end
	print "\n"
end

if ARGV.length != 1
	STDERR.puts 'Error'
	exit 1
end
fib(ARGV[0])
