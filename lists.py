def main():
    my_list=[1,3,'hello', 4.5]
    print(my_list)
    print(my_list[2])
    print(my_list[-2])
    print(my_list[1:3])
    my_list[2]='a new thing'
    print(my_list)
    my_list.append(56)
    print(my_list)
    del my_list[2]
    print(my_list)





if __name__=='__main__':
    main()
