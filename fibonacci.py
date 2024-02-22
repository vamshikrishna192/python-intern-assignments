def Fibonacci(n):
    if n < 0:
        print("Invalid value entered")
    elif n == 0:
        return "0"
    elif n == 1:
        return "0 1"
    else:
        fib_sequence = [0, 1]
        sequence_str = "0 1"
        for i in range(2, n):
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
            sequence_str += " " + str(next_number)
        return sequence_str

a = int(input("Enter the number of terms for the Fibonacci sequence: "))
result = Fibonacci(a)
print("Required Fibonacci sequence is:", result)
