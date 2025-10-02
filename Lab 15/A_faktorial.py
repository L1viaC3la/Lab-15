def faktorial(n: int) -> int:
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

if __name__ == "__main__":
    n = int(input("n: "))
    rezultati = faktorial(n)
    if rezultati == -1:
        print("Gabim")
    else:
        print(rezultati)
