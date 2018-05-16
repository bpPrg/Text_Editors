#!/Users/poudel/anaconda/bin/python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 22, 2017 Tue
# Last update :
# Est time    :

# Imports
import string
import numpy as np

# Global Variables
ofile = 'latex_colors.cson'
def latex_colors():
    """
    Latex colors used in beamer
    """
    infile = "colors.txt"
    col1,col2 = np.genfromtxt(infile, delimiter=None, usecols=(0,1),
                      dtype=str, unpack=True)
    # first column
    print("  # Beamer Colors".strip('\n'),file=open(ofile,'w'))
    for i,a in enumerate(col1):
        hdr = "  'Beamer Color {}':\n".format(a)
        pre = "    'prefix': 'c{}'".format(i+1)
        bdy = r"""
    'body': '''
    \\\\begin{tcolorbox}[colback=blue!5!white,colframe=%s]
    \  $1
    \\\\end{tcolorbox}
    '''
        """%(a)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

    # second column
    for i,a in enumerate(col2):
        hdr = "  'Beamer Color {}':\n".format(a)
        pre = "    'prefix': 'c{}'".format(i+1+34)
        bdy = r"""
    'body': '''
    \\\\begin{tcolorbox}[colback=blue!5!white,colframe=%s]
    \  $1
    \\\\end{tcolorbox}
    '''
        """%(a)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def main():
    """Run main function."""
    print('Creating: ', ofile)
    latex_colors()


if __name__ == "__main__":
    main()
