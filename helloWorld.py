

def my_method(a):
    a+=10
    print(a)
    return a/2



def main():
    print("Hello World!")
    a=3
    print(a)
    a="hello"
    print(a)
    a=6
    b=my_method(a)
    print(b)

if __name__ == '__main__':
    main()