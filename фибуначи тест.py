def fibonacci_matrix(n):
    def multiply_matrices(m1, m2):
        return [
            [m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0], m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]],
            [m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0], m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]]
        ]

    def matrix_power(matrix, power):
        result = [[1, 0], [0, 1]]  # Единична матрица
        while power:
            if power % 2:
                result = multiply_matrices(result, matrix)
            matrix = multiply_matrices(matrix, matrix)
            power //= 2
        return result

    if n <= 1:
        return n
    result_matrix = matrix_power([[1, 1], [1, 0]], n - 1)
    return result_matrix[0][0]


def run_fibonacci_program():
    try:
        user_input = input("Въведете положително цяло число за Фибоначи (или 'q' за изход): ")
        if user_input.lower() == 'q':
            print("Изход от програмата.")
            return
        n = int(user_input)
        if n < 0:
            print("Моля, въведете положително число.")
        else:
            result = fibonacci_matrix(n)
            print(f"{n} на Фибоначи: {result}")
    except ValueError:
        print("Моля, въведете валидно цяло число.")

    run_fibonacci_program()  # Рекурсивно извикване за повторно стартиране


# Стартиране на програмата
run_fibonacci_program()
