from logger import log_call, log_data

@log_call
def add(a, b):
    return a + b


def main():
    print(add(3, 5))



if __name__ == '__main__':
    main()

