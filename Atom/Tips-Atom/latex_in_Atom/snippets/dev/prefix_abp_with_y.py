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
ofile = 'templates/prefix_abp_with_y.cson'


grk = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa',
       'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi',
       'chi', 'psi', 'omega', 'Gamma', 'Delta', 'Theta', 'Lambda', 'Xi', 'Pi', 'Sigma', 'Phi', 'Psi']

alph = list('abgdezhqiklmnxoprstufcywGDQLXPSFY')
cap_alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

comment = """ 
  #-----------------------------------------------------------------------------
"""


def greek():
  """
  Greek
  a = \alpha
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Greek".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(grk):
    hdr = "  '{}':\n".format(a)
    pre = "    'prefix': '{}'\n".format(alph[i])
    fmt = r'\\\\{}'.format(a)
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def angle():
  """
  Angle Alpha
  aay = \langle\alpha\rangle
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Angle Alpha".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(grk):
    hdr = "  'Angle {}':\n".format(a)
    pre = "    'prefix': 'a{}y'\n".format(alph[i])
    fmt = r'\\\\langle \\\\{} \\\\rangle\ $0'.format(a)
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def bold():
  """
  Bold Alpha
  bay = \boldsymbol{\alpha}
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Bold Alpha".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(grk):
    hdr = "  'Bold {}':\n".format(a)
    pre = "    'prefix': 'b{}y'\n".format(alph[i])
    fmt = r'\\\\boldsymbol{}\\\\{}{}\ $0'.format("{", a, "}")
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def partial():
  """ 
  Partial Alpha
  pay = \partial{\alpha}
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Partial Alpha".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(grk):
    hdr = "  'Partial {}':\n".format(a)
    pre = "    'prefix': 'p{}y'\n".format(alph[i])
    fmt = r'\\\\partial\\\\{}\ $0'.format(a)
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


# **************************** Bold ****************************
def angle_bold():
  """ 
  Angle Alpha Bold
  aaby = \langle\boldsymbol{\alpha}\rangle
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Angle Alpha Bold".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(grk):
    hdr = "  'Angle {} Bold':\n".format(a)
    pre = "    'prefix': 'a{}by'\n".format(alph[i])
    fmt = r'\\\\langle\\\\boldsymbol{}\\\\{}{}\\\\rangle\ $0'.format(
        "{", a, "}")
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def partial_bold():
  """ 
  Partial Alpha Bold
  paby = \partial\boldsymbol{\alpha}
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Partial Alpha Bold".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(grk):
    hdr = "  'Partial {} Bold':\n".format(a)
    pre = "    'prefix': 'p{}by'\n".format(alph[i])
    fmt = r'\\\\partial\\\\boldsymbol{}\\\\{}{}\ $0'.format("{", a, "}")
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))

# **************************** Dollar ****************************


def dollar_greek():
  """
  Alpha Dollar
  ax = $\alpha$
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Alpha Dollar".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(grk):
    hdr = "  '{} Dollar':\n".format(a)
    pre = "    'prefix': '{}x'\n".format(alph[i])
    fmt = r'\$\\\\{}\$\ $0'.format(a)
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def dollar_angle():
  """
  Angle Alpha Dollar
  aayx = $\langle \alpha \rangle$ 
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Angle Alpha Dollar".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(grk):
    hdr = "  'Angle {} Dollar':\n".format(a)
    pre = "    'prefix': 'a{}yx'\n".format(alph[i])
    fmt = r'\$\\\\langle \\\\{} \\\\rangle\$\ $0'.format(a)
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def dollar_bold():
  """
  Bold Alpha Dollar
  bayx = $\boldsymbol{\alpha}$
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Bold Alpha Dollar".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(grk):
    hdr = "  'Bold {} Dollar':\n".format(a)
    pre = "    'prefix': 'b{}yx'\n".format(alph[i])
    fmt = r'\$\\\\boldsymbol{}\\\\{}{}\$\ $0'.format("{", a, "}")
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def dollar_partial():
  """ 
  Partial Alpha Dollar
  payx = $\partial\boldsymbol{\alpha}$
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Partial Alpha Dollar".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(grk):
    hdr = "  'Partial {} Dollar':\n".format(a)
    pre = "    'prefix': 'p{}yx'\n".format(alph[i])
    fmt = r'\$\\\\partial{}\\\\{}{}\$\ $0'.format("{", a, "}")
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))

#------------------------- Dollar Bold --------------------


def dollar_bold_angle():
  """
  Angle Alpha Bold Dollar
  aabyx = $\langle \boldsymbol{\alpha} \rangle$ 
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Angle Alpha Bold Dollar".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(grk):
    hdr = "  'Angle {} Bold Dollar':\n".format(a)
    pre = "    'prefix': 'a{}byx'\n".format(alph[i])
    fmt = r'\$\\\\langle \\\\boldsymbol{}\\\\{}{} \\\\rangle\$\ $0'.format(
        "{", a, "}")
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def dollar_bold_partial():
  """ 
  Partial Alpha Bold Dollar
  pabyx = $\partial\boldsymbol{\alpha}$
  """
  print(comment.strip('\n'), file=open(ofile, 'a'))
  print("  # Partial Alpha  Bold Dollar".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(grk):
    hdr = "  'Partial {} Bold Dollar':\n".format(a)
    pre = "    'prefix': 'p{}byx'\n".format(alph[i])
    fmt = r'\$\\\\partial\\\\boldsymbol{}\\\\{}{}\$\ $0'.format("{", a, "}")
    bdy = "    'body': '{}'\n".format(fmt)
    snip = hdr + pre + bdy
    print(snip, file=open(ofile, 'a'))


def main():
  """Run main function."""
  greek()
  angle()
  bold()
  partial()

  # bold
  angle_bold()
  partial_bold()

  # Dollar
  dollar_greek()
  dollar_angle()
  dollar_bold()
  dollar_partial()

  # Bold Dollar
  dollar_bold_angle()
  dollar_bold_partial()


if __name__ == "__main__":
  main()
