#!python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel
# Date        : Mar 11, 2018
#
# Imports
from __future__ import print_function, with_statement, division, unicode_literals, absolute_import
import string

# Global Variables
ofile = 'atom-latex-snippets.cson'

alph_low = list('abcdefghijklmnopqrstuvwxyz')
alph_upp = [a.upper() for a in alph_low]
alph = alph_low + alph_upp

comment = """ 
  #--------------------------------------------------
"""

atom_latex = """##===================================================
##  Latex Snippets
## h=eta q=theta f=phi c=chi y=psi w=omega t=tau x=xi
##===================================================
'.text.tex.latex':
"""

grk = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa',
       'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi',
       'chi', 'psi', 'omega', 'Gamma', 'Delta', 'Theta', 'Lambda', 'Xi', 'Pi', 'Sigma', 'Phi', 'Psi']
grk_alph = list('abgdezhqiklmnxoprstufcywGDQLXPSFY')

greek_data = [  # greek
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


def greek_snippets(h0, h1, p0, p1, b0, b1):
  cmt = comment + "\n" + '  # ' + h0 + ' ' + h1 + '\n'
  print(cmt, file=open(ofile, 'a'))
  for i in range(len(grk)):
    hdr = h0 + ' ' + grk[i] + ' ' + h1
    hdr = "  '{}':\n".format(hdr.strip())
    pre = "    'prefix': '{}{}{}'\n".format(p0, grk_alph[i], p1)
    bdy = "    'body': '{}{}{}'\n".format(b0, grk[i], b1)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def text_bold():
  """
  Text Bold a
  tba = \boldsymbol{a}
  """
  print("  # Text Bold a".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(alph):
    hdr = "  'Text Bold {}':\n".format(a)
    pre = "    'prefix': 'tb{}'\n".format(alph[i])
    fmt = r'\\\\boldsymbol{}{}{}\ $0'.format("{", a, "}")
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def text_dollar():
  """
  Text Dollar a
  xxa = $a$
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Text Dollar a".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(alph):
    hdr = "  'Text Dollar {}':\n".format(a)
    pre = "    'prefix': 'xx{}'\n".format(alph[i])
    fmt = r'\${}\$\ $0'.format(a)
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def text_bold_dollar():
  """
  Text Bold a Dollar
  tbax = $\boldsymbol{a}$
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Text Bold a Dollar".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(alph):
    hdr = "  'Text Bold {} Dollar':\n".format(a)
    pre = "    'prefix': 'tb{}x'\n".format(alph[i])
    fmt = r'\$\\\\boldsymbol{}{}{}\$\ $0'.format("{", a, "}")
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def text_dollar_bold():
  """
  Text Dollar Bold a
  xxba = $\boldsymbol{a}$
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Text Dollar Bold".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(alph):
    hdr = "  'Text Dollar Bold {} ':\n".format(a)
    pre = "    'prefix': 'xxb{}'\n".format(alph[i])
    fmt = r'\$\\\\boldsymbol{}{}{}\$\ $0'.format("{", a, "}")
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def text_script():
  """
  Text Script A
  say = \mathscr{A}

  Note: \mathscr needs   usepackage{mathrsfs}
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Text Script A".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(alph_upp):
    hdr = "  'Text Script {}':\n".format(a)
    pre = "    'prefix': 's{}y'\n".format(alph[i])
    fmt = r'\\\\mathscr{}{}{}\ $0'.format("{", a, "}")
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def text_script_dollar():
  """
  Text Script A Dollar
  sayx = $\mathscr{A}$

  Note: \mathscr needs   usepackage{mathrsfs}
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Text Script A Dollar".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(alph_upp):
    hdr = "  'Text Script {} Dollar':\n".format(a)
    pre = "    'prefix': 's{}yx'\n".format(alph[i])
    fmt = r'\$\\\\mathscr{}{}{}\$\ $0'.format("{", a, "}")
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def main():
  """Run main function."""
  # Snippets for english alphabet
  print(atom_latex.rstrip('\n'), file=open(ofile, 'w'))
  text_bold()
  text_dollar()
  text_bold_dollar()
  text_dollar_bold()

  text_script()
  text_script_dollar()

  # Snippets for greek letters
  for d in greek_data:
    h0, h1, p0, p1, b0, b1 = d
    greek_snippets(h0, h1, p0, p1, b0, b1)


if __name__ == "__main__":
  main()
