def re(n):
    if n > 1:
        return n * re(n-1)
    else:
        return 1


if __name__ == '__main__':
    print(re(999))
