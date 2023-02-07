#!/usr/bin/python3 



from sys import stdin




def __buff_bin():
    """funcction read process .. binary ... """

    # read binary
    with open("binary.bin", "rb") as readby:
        buff = io.BytesIO(readby.read())


    # utily buff 

    # status view 

    print(" buff content :", buff.getvalue()) # muestra el binario cargado ... 
    #contador en  0 
    buff.seek(0)

    print("read byte : ", buff.read(1))



    buff.close()




if __name__ == "__main__":
    __buff_bin()
