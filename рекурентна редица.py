def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

while True:
    user_input = input("Въведете положително цяло число (или 'q' за изход): ")

    if user_input.lower() == 'q':
        print("Изход от програмата.")
        break

    try:
        n = int(user_input)
        if n < 0:
            print("Моля, въведете положително число.")
        else:
            result = fibonacci_recursive(n)
            print(f"{n} на Фибоначи: {result}")
    except ValueError:
        print("Моля, въведете валидно цяло число.")
