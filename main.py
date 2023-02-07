#!/usr/bin/env python3 

from sys import stdin 
import os , sys
import subprocess
import io
import time



def __pressent():

    # help programming init 


    # call script 
    script_f =  "src/banner.sh"

    subprocess.run(["bash", script_f])
     
    _myfunc()



def  __core_db():
    pass
    




def _myfunc():
    _teler = 4 
    _Status_t = "[+]"
    print(f"{_Status_t} reading status ", end = "")
    for t in range(3):
        
        print(".", end="", flush=True)
        time.sleep(1)
    #print(["." for z in range(3)])   
    
    print("\n")

if __name__ == "__main__" : 
    __pressent()
