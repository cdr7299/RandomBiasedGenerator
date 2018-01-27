# RandomBiasedGenerator
A random number generator with a bias towards the higher of the numbers

We need a random number generator which is biased towards higher end of our range. 
We can simply do this by getting a random number and wrapping it according to our required scenario(Using a uniformly distributed random generator we get a 73% skewed results towards higher range)

As customrandrange(X,Y) has uniform distribution we can then simply get higher numbers when this function returns less than 73(which is our preffered percentage).

For generating the random number, System time is used as the seed. It then uses previous value to generate a new random number. 
But if large amount of random numbers are required at a time this converges pretty fast. So after every 15 random numbers a new seed is provideed(lastest time). This ensures better distribution but in turn makes the program slow because of use of sleep.
