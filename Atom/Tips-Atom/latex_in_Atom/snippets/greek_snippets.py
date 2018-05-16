#!python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 22, 2017 Tue
# Last update :
# Est time    :

# Imports
from __future__ import print_function, with_statement, division, unicode_literals, absolute_import
import string

# Global Variables
ofile = 'templates/greek_snippets.cson'
grk = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa',
       'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi',
       'chi', 'psi', 'omega', 'Gamma', 'Delta', 'Theta', 'Lambda', 'Xi', 'Pi', 'Sigma', 'Phi', 'Psi']
alph = list('abgdezhqiklmnxoprstufcywGDQLXPSFY')
comment = r"  #------------------------------------------"

data = [  # greek
    # greek
    ['', '', '', '', '\\\\\\\\', ''],
    # Prefixes: Angle bold partial
    ['Angle', '', 'a', 'y', '\\\\\\\\langle \\\\\\\\', ' \\\\\\\\rangle\ $0'],
    ['Bold', '', 'b', 'y',
     '\\\\\\\\boldsymbol{\\\\\\\\', '}\ $0'],
    ['Partial', '', 'p', 'y',
     '\\\\\\\\partial\\\\\\\\', '}\ $0'],
    # Bold
    ['Angle', 'Bold', 'a', 'by',
     '\\\\\\\\langle\\\\\\\\boldsymbol{\\\\\\\\', '}\\\\\\\\rangle\ $0'],
    ['Partial', 'Bold', 'p', 'by',
     '\\\\\\\\partial\\\\\\\\boldsymbol{\\\\\\\\', '}\ $0'],
    # Dollar
    ['', 'Dollar', '', 'x', '\$\\\\\\\\', '\$\ $0'],
    ['Angle', 'Dollar', 'a', 'yx', '\$\\\\\\\\langle \\\\\\\\', ' \\\\\\\\rangle\$\ $0'],
    ['Bold', 'Dollar', 'b', 'yx',
     '\$\\\\\\\\boldsymbol{\\\\\\\\', '}\$\ $0'],
    ['Partial', 'Dollar', 'p', 'yx',
     '\$\\\\\\\\partial{\\\\\\\\', '}\$\ $0'],
    # Attribute and Dollar
    ['Angle', 'Bold Dollar', 'a', 'byx',
     '\$\\\\\\\\langle \\\\\\\\boldsymbol{\\\\\\\\', '} \\\\\\\\rangle\$\ $0'],
    ['Partial', 'Bold Dollar', 'p', 'byx',
     '\$\\\\\\\\partial\\\\\\\\boldsymbol{\\\\\\\\', '}\$\ $0'],
    # Suffix: star prime bar dot hat tilde modulus zero one two three
    ['', 'star', '', 's', '\\\\\\\\', '^*\ $0'],
    ['', 'prime', '', 'p', '\\\\\\\\', '\\\\\\\\prime\ $0'],
    ['', 'bar', '', 'b', '\\\\\\\\bar{\\\\\\\\', '}\ $0'],
    ['', 'dot', '', 'd', '\\\\\\\\dot{\\\\\\\\', '}\ $0'],
    ['', 'hat', '', 'h', '\\\\\\\\hat{\\\\\\\\', '}\ $0'],
    ['', 'tilde', '', 't', '\\\\\\\\tilde{\\\\\\\\', '}\ $0'],
    ['', 'modulus', '', 'm', '\\\\\\\\lvert\\\\\\\\', '\\\\\\\\rvert\ $0'],
    ['', 'zero', '', '0', '\\\\\\\\', '_0\ $0'],
    ['', 'one', '', '1', '\\\\\\\\', '_1\ $0'],
    ['', 'two', '', '2', '\\\\\\\\', '_2\ $0'],
    ['', 'three', '', '3', '\\\\\\\\', '_3\ $0'],
    # Bold: star prime bar dot hat tilde modulus
    ['', 'star bold', '', 'sb', '\\\\\\\\boldsymbol{\\\\\\\\', '^*\ $0'],
    ['', 'prime bold', '', 'pb',
     '\\\\\\\\boldsymbol{\\\\\\\\', '}\\\\\\\\prime\ $0'],
    ['', 'bar bold', '', 'bb',
     '\\\\\\\\boldsymbol{\\\\\\\\bar{\\\\\\\\', '}}\ $0'],
    ['', 'dot bold', '', 'db',
     '\\\\\\\\boldsymbol{\\\\\\\\dot{\\\\\\\\', '}}\ $0'],
    ['', 'hat bold', '', 'hb',
     '\\\\\\\\boldsymbol{\\\\\\\\hat{\\\\\\\\', '}}\ $0'],
    ['', 'tilde bold', '', 'tb',
     '\\\\\\\\boldsymbol{\\\\\\\\tilde{\\\\\\\\', '}}\ $0'],
    ['', 'modulus bold', '', 'mb',
     '\\\\\\\\lvert\\\\\\\\boldsymbol{\\\\\\\\', '}\\\\\\\\rvert\ $0'],
    ['', 'zero bold', '', '0b', '\\\\\\\\boldsymbol{\\\\\\\\', '_0}\ $0'],
    ['', 'one bold', '', '1b', '\\\\\\\\boldsymbol{\\\\\\\\', '_1}\ $0'],
    ['', 'two bold', '', '2b', '\\\\\\\\boldsymbol{\\\\\\\\', '_2}\ $0'],
    ['', 'three bold', '', '3b', '\\\\\\\\boldsymbol{\\\\\\\\', '_3}\ $0'],
    # Attribute Dollar: star prime bar dot hat tilde modulus 0 1 2 3
    ['', 'star dollar', '', 'sx', '\$\\\\\\\\', '^*\$\ $0'],
    ['', 'prime dollar', '', 'px', '\$\\\\\\\\', '\\\\\\\\prime\$\ $0'],
    ['', 'bar dollar', '', 'bx', '\$\\\\\\\\bar{\\\\\\\\', '}\$\ $0'],
    ['', 'dot dollar', '', 'dx', '\$\\\\\\\\dot{\\\\\\\\', '}\$\ $0'],
    ['', 'hat dollar', '', 'hx', '\$\\\\\\\\hat{\\\\\\\\', '}\$\ $0'],
    ['', 'tilde dollar', '', 'tx', '\$\\\\\\\\tilde{\\\\\\\\', '}\$\ $0'],
    ['', 'modulus dollar', '', 'mx', '\$\\\\\\\\lvert\\\\\\\\', '\\\\\\\\rvert\$\ $0'],
    ['', 'zero dollar', '', '0x', '\$\\\\\\\\', '_0\$\ $0'],
    ['', 'one dollar', '', '1x', '\$\\\\\\\\', '_1\$\ $0'],
    ['', 'two dollar', '', '2x', '\$\\\\\\\\', '_2\$\ $0'],
    ['', 'three dollar', '', '3x', '\$\\\\\\\\', '_3\$\ $0'],
    #
    # Attribute Bold Dollar: star prime bar dot hat tilde modulus 0 1 2 3
    #
    ['', 'star bold dollar', '', 'sbx',
     '\$\\\\\\\\boldsymbol{\\\\\\\\', '^*\$\ $0'],
    ['', 'prime bold dollar', '', 'pbx',
     '\$\\\\\\\\boldsymbol{\\\\\\\\', '}\\\\\\\\prime\$\ $0'],
    ['', 'bar bold dollar', '', 'bbx',
     '\$\\\\\\\\boldsymbol{\\\\\\\\bar{\\\\\\\\', '}}\$\ $0'],
    ['', 'dot bold dollar', '', 'dbx',
     '\$\\\\\\\\boldsymbol{\\\\\\\\dot{\\\\\\\\', '}}\$\ $0'],
    ['', 'hat bold dollar', '', 'hbx',
     '\$\\\\\\\\boldsymbol{\\\\\\\\hat{\\\\\\\\', '}}\$\ $0'],
    ['', 'tilde bold dollar', '', 'tbx',
     '\$\\\\\\\\boldsymbol{\\\\\\\\tilde{\\\\\\\\', '}}\$\ $0'],
    ['', 'modulus bold dollar', '', 'mbx',
     '\$\\\\\\\\lvert\\\\\\\\boldsymbol{\\\\\\\\', '}\\\\\\\\rvert\$\ $0'],
    ['', 'zero bold dollar', '', '0bx',
     '\$\\\\\\\\boldsymbol{\\\\\\\\', '_0}\$\ $0'],
    ['', 'one bold dollar', '', '1bx',
     '\$\\\\\\\\boldsymbol{\\\\\\\\', '_1}\$\ $0'],
    ['', 'two bold dollar', '', '2bx',
     '\$\\\\\\\\boldsymbol{\\\\\\\\', '_2}\$\ $0'],
    ['', 'three bold dollar', '', '3bx',
     '\$\\\\\\\\boldsymbol{\\\\\\\\', '_3}\$\ $0']

]


def snippet(h0, h1, p0, p1, b0, b1):
  cmt = comment + "\n" + '  # ' + h0 + ' ' + h1 + '\n'
  print(cmt, file=open(ofile, 'a'))
  for i in range(len(grk)):
    hdr = h0 + ' ' + grk[i] + ' ' + h1
    hdr = "  '{}':\n".format(hdr.strip())
    pre = "    'prefix': '{}{}{}'\n".format(p0, alph[i], p1)
    bdy = "    'body': '{}{}{}'\n".format(b0, grk[i], b1)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def main():
  print("", file=open(ofile, 'w'))
  for d in data:
    h0, h1, p0, p1, b0, b1 = d
    snippet(h0, h1, p0, p1, b0, b1)


if __name__ == "__main__":
  main()
