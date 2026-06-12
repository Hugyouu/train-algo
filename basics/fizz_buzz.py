def fizz_buzz(value: int) -> None:
    print(*("FizzBuzz" if (x % 3 == 0 and x % 5 == 0) else "Buzz" if x % 5 == 0 else "Fizz" if x % 3 == 0 else x for x in range(1, value + 1)), sep="\n")


if __name__ == "__main__":
    fizz_buzz(100)
