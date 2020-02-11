from MathOperations.addition import sum
from MathOperations.division import quotient

def mean(data):
    num_values = len(data)
    total = 0

    for num in num_values:
        total = sum(total, num)
    return quotient(total, num_values)