numbers = [4, 7, 2, 9, 1, 5, 3]

def print_average(input_list):
    sum = 0

    for i in numbers:
        sum += abs(i)

    average = round((sum / len(numbers)), 2)

    print(average)

print_average(numbers)

# list reversed
numbers.reverse()
print(numbers)