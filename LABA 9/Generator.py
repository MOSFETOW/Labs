


def pair_generator(filename):
    f = open(filename, "r", encoding="utf-8")

    for line in f:
        line = line.strip().lower()
        words = line.split()

        pairs = []

        # шукаємо пари тільки всередині одного слова
        for w in words:
            for i in range(len(w) - 1):
                pairs.append(w[i] + w[i + 1])

        # повертаємо тільки 3 пари
        yield pairs[:3]

    f.close()


# ======= приклад використання =========
def main():
    for p in pair_generator("text100.txt"):
        print(p)
if __name__ == "__main__":
    main()