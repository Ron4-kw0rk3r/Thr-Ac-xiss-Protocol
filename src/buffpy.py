#!/usr/bin/python3 



from sys import stdin


#module io from buffer


import io 



def __create_speel():

    with open('testingfile.txt', "r") as readl:
        buffer = io.StringIO(readl.read())



    # read file archive in line x line in bucle with 
    # puntero del buffer en cero ... 


    buffer.seek(0)


    print("_creation finish \n")
    for l in buffer:
        print(l)



    buffer.close


if __name__ == "__main__":
    __create_speel()
