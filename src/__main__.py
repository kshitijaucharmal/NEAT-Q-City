import threading
import random

val = 0


def sayHello():
    global val
    nos = []
    for i in range(10000):
        nos.append(random.random())
        print(nos[i])
    val = nos[random.randint(0, 10000)]


# Basic threading code
def main():
    threads = []
    for _ in range(50):
        thread = threading.Thread(target=sayHello)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
    # for i in range(50):
    #     sayHello()
    pass
