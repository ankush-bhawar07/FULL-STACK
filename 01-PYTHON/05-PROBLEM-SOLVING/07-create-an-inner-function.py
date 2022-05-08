# Create an inner function

# Create an outer function that will accept two strings, x and y. (x= 'Code' and y = 'Compete'.
# Create an inner function inside an outer function that will concatenate x and y.
# At last, an outer function will join the word 'developer' to it.

def manipulate(x, y):
    # concatenate two strings
    def inner_fun(x, y):
        return x + y

    z = inner_fun(x, y)
    return z + 'Developers'

result = manipulate('Code', 'Compete')
print(result)
