
def main():
    rows = 20
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))

if __name__ == '__main__':
    main()