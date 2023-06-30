# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/python

# DESCRIPTION:
# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

# input
# customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.

def queue_time(customers, n):
    counter = 0
    while not customers:
        return counter
    if n >= len(customers):
        counter = max(customers)
    else:
        cashiers = [0] * n
        for _cust in customers:
            cashiers.sort()
            cashiers[0] += _cust
        counter = max(cashiers)
    return counter