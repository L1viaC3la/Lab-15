def shuma_shifrave(n: int) -> int:
    if n < 0:
        return -1
    if n < 10:
        return n
    return (n % 10) + shuma_shifrave(n // 10)

if __name__ == "__main__":
    n = int(input("n: "))
    rezultati = shuma_shifrave(n)
    if rezultati == -1:
        print("Gabim")
    else:
        print(rezultati)
