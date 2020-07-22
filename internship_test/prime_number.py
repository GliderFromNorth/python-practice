def prime_num_check(n):
    for i in range(2, n-1):
        if n % i == 0:
            return "false"
    return "true"
print(prime_num_check(int(input("Enter the number"))))
