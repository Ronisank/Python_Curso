def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

num = int(input("Digite um número: "))

if num <= 0:
    print("Por favor, digite um número positivo")
else:
    print("Sequência de Fibonacci:")
    for i in range(num):
        print(fibonacci(i))

    if num in [fibonacci(i) for i in range(num)]:
        print(f"\nO número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"\nO número {num} não pertence à sequência de Fibonacci.")
