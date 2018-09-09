def callback(i):
    if i % 16 == 0:
        if i % 10 == 0:
            print(i)


def main(callback):
    for i in range(1000):
        callback(i)
    print("0-999 is checked!")


if __name__ == '__main__':
    main(callback=callback)