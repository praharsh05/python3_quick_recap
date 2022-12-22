def main():
    a=0
    while(a<10):
        print(a)
        a+=1
    

    my_tuple=(1,2,3,4,5,'hi', 6)
    for items in my_tuple:
        print(items)

    my_list=[1,2,4,7,'hello']
    for items in my_list:
        print(items)
    
    for i in range(10):
        print(i)

    print(type(range(10)))
    a=list(range(10))
    print(a)


if __name__=='__main__':
    main()