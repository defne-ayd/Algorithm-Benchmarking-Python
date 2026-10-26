from timeit import default_timer as timer
def is_prime(n):
    n = int(n)
    if n == 1:
        return False
    else:
        for i in range(n - 1,0,-1):
            if i > 1:
                rest = n % i
                if rest == 0:
                    return False
                    break
            elif i == 1:
                return True
def accuracy_test_is_prime(test_case,prime):
    if prime == is_prime(test_case):
        print("Test for", test_case, "passed.")
    else:
        print("Test for", test_case, "failed.")
def speed_test_is_prime(n):
    start_time = timer()
    is_prime(n)
    end_time = timer()
    total_time = end_time - start_time
    print("Time for", n, total_time)
accuracy_test_is_prime(43177,True)
accuracy_test_is_prime(23909,True)
accuracy_test_is_prime(31091,True)
accuracy_test_is_prime(44532,False)
accuracy_test_is_prime(38243,False)
accuracy_test_is_prime(13860,False)
speed_test_is_prime(43177)
speed_test_is_prime(784687)
speed_test_is_prime(12009367)
speed_test_is_prime(231002771)
speed_test_is_prime(3484798799)
