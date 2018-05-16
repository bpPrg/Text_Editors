#!python
# -*- coding: utf-8 -*-#
"""
Python script with arguments.

@author: Bhishan Poudel

@date:  Oct 18, 2017

@email: bhishanpdl@gmail.com

To run: python my_args.py a 3 4

Using atom:
First create a profile with predefined arguments:
cmd shf i   or package>configure script
cmd: python
prg arg: 2 3
save: arg_2_3

Then, run the program
cmd shf k  or, package> script> run with profile
hit enter.




"""
# Imports
import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))


a = sys.argv[1]
b = sys.argv[2]
print("a+b = {}".format(a+b))

aa = int(sys.argv[1])
bb = int(sys.argv[2])
print("aa+bb = {}".format(aa+bb))
