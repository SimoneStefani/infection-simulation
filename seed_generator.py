from sympy import sieve

prime_numbers = list(sieve.primerange(800, 10000)) # Generates 1090 prime numbers
print(len(prime_numbers))

# Take approx. 100 of those prime numbers as our seeds (every 10th prime number from the list)
prime_seeds = [prime_numbers[i*10] for i in range(int(len(prime_numbers)/10))]
print(len(prime_seeds))
print(prime_seeds)

