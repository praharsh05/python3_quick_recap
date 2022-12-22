
def my_method():
    a=5
    b=6
    return a,b



def main():
    my_tuple=(1,'hello', 3.4)
    print(my_tuple)
    print(my_tuple[0])
    print(my_tuple[2])
    print(my_tuple[-2])
    print(len(my_tuple))
    print(my_tuple[1:3])
    q=my_method()
    print(q)
    d,e=q
    print(d)


if __name__ == '__main__':
    main()