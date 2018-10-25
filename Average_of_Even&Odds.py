def average(funct):

    def wrapper(numbers):
        total_even_sum = 0
        even_numbers = 0
        total_odd_sum = 0
        odd_numbers = 0
        for Number in numbers:
            if (Number % 2 == 0 ):
                even_numbers +=1
                total_even_sum += Number
            else:
                odd_numbers += 1
                total_odd_sum += Number
        print("Average of Evens:", total_even_sum/even_numbers)
        funct(numbers)
        print("Average of Odds:", total_odd_sum / odd_numbers)
    return wrapper

@average
def mean(numbers):
    total = 0

    for i in numbers:

        total += i

    print("Mean:",total/len(numbers))

mean([55,	26,	28,	84,	89, 94,	81,	82,	92,	72, 10,	98,	8,	28,	53, 82,	85,	64,	29,	41, 24,
      93,	71,	96, 21])
