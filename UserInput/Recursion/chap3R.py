def x(n):
    if n <= 0:
        print("kiss me again!")
        return
    else:
        print(f"You kissed me {n} times")
        x( n - 1)
x(5)
