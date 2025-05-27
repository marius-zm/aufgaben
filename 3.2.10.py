def count_up(number):
    sum = 0
    for i in range(1, number):
        if i % 2 == 0:
            sum += i
    print(sum)

count_up(20)
count_up(100)