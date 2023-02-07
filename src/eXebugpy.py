#! /usr/bin/python3 
 
import ctypes


# execute binnary in python in memory add



def __exek():
    libv1  = ctypes.CDLL("./file.bin")


    # objec memory addres in file load in memory


    address = ctypes.cast(lib.addr, ctypes.c_void_p)

    # exe exploting buff 

    libv1.execute(address)


    
if __name__ == "__main__":
    __exek()
