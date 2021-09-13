# Write a function to compute 5/0 and use try/except to catch the exceptions

def compute(num, denom):
    try:
        return int(num/denom)
    except ZeroDivisionError:
        return 'Denminator value should be greater than zero!'


print(compute(5, 0))
