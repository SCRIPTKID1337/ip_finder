p = int (input ("type to the power : "))
def square_list(l):
    square = []
    for i in l:
        square.append(i**p)
    return square
first_number = int(input ("please type your first number : "))
second_number = int(input ("please type your second number : "))
numbers = list (range(first_number, second_number + 1))
print (square_list(numbers))
input ()
