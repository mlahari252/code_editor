
def sum(a, b):
    return a + b

# take two integers on a single line separated by space
a, b = map(int, input("Enter two numbers: ").split())

print(f'Sum of {a} and {b} is {sum(a, b)}')
