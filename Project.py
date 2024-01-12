from threading import Timer
import time

def my_function():
    print("My function executed")

timer = Timer(13.0, my_function)

timer.start()

time.sleep(1.0)

timer.cancel()

def main():
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        print(a + b)


if __name__ == "__main__":
    main()