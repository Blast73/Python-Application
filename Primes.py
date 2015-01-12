# I don't have enough experience to even really know where to start from a practical standpoint 
# But I will propose potential methods
#
## method 1
# To start I would want to inport some type of graph that's a list of prime numbers (like datetime possibly)
# I assume they couldn't all be imported because there are infinite primes
# after having the list for reference I would take find_next_prime(n) and use some ifs and thens
# to find the next biggist prime and return it 
#
## method 2
# I would take n from find_next_prime(n) 
# then if (n + 1) / (n + 1) == 1 I would return n + 1
# if that returned False I would have it run the same but n + 2
# Now I'm absolutely sure there's a way to simplify that but I don't know how
# Preferably a way of changing the 1 to a 2 then to a 3 until some True returns exist
