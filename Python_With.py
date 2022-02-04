#!/usr/bin/python

# Open a file
import time

def main():
 with open("foo.txt", "r") as fo:

      print("Name of the file: ", fo.name)
      print("Closed or not : ", fo.closed)
      print ("Opening mode : ", fo.mode)
      print ("Softspace flag : ", fo.read(1))

 while(1):
      time.sleep(1)

if __name__ == '__main__':
    main()