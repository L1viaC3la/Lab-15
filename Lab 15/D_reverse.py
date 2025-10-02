def kthim_teksti(s: str) -> str:
    if len(s) <= 1:
        return s
    return s[-1] + kthim_teksti(s[:-1])

if __name__ == "__main__":
    teksti = input("Teksti: ")
    print(kthim_teksti(teksti))
