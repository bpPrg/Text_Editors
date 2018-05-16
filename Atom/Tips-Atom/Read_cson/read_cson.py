#!python
# -*- coding: utf-8 -*-#
"""
Read cson files
    
@author: Bhishan Poudel
    
@date:  Mar 23, 2018
    
"""
# Imports
import cson


def read_cson(ifile):
    with open(ifile,'rb') as fi:
        snippets = cson.load(fi)



    text = snippets['.text.plain']
    diary = text['diary']
    prefix = diary['prefix']
    body = diary['body']
    # print(body)


    for k in text.keys():
        print(text[k]['prefix'])

def main():
    """Run main function."""
    read_cson('a.cson')
    
if __name__ == "__main__":
    main()
