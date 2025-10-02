def gcd(a: int, b: int) -> int:
    if a < 0 or b < 0 or (a == 0 and b == 0):
        return -1
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    rezultati = gcd(a, b)
    if rezultati == -1:
        print("Gabim")
    else:
        print(rezultati)
