def cubes_under1000():    
    num = 1
    while num*num*num <= 1000:
        print(num*num*num)
        num += 1

cubes_under1000()

def age_type():
    age_input = int(input('What is your age?'))
    if age_input < 18:
        print("kids")
    elif age_input > 65:
        print("seniors")
    else:
        print("adults")

age_type()

    
def primenumbersunder100():     #takes a list of prime numbers, already populated with 1 and 2. check to see if the numbers in range are divisible by the numbers in the prime list
    prime_nums = [1,2]
    is_prime = True
    for i in range (3,101,2):
        is_prime = True
        for nums in prime_nums:
            if i in prime_nums:
                is_prime = False
                break
            if i % nums == 0 and nums != 1:
                is_prime = False
        if is_prime == True:
            prime_nums.append(i)
    print(prime_nums)

primenumbersunder100()