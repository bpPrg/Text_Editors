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
ofile = 'templates/text_bold_dollar_script.cson'

alph_low = list('abcdefghijklmnopqrstuvwxyz')
alph_upp = [a.upper() for a in alph_low]
alph = alph_low + alph_upp

comment = """ 
  #-----------------------------------------------------------------------------
"""


def text_bold():
  """
  Text Bold a
  tba = \boldsymbol{a}
  """
  print(comment.strip('\n'), file=open(ofile, 'w'))
  print("  # Text Bold a".strip('\n'), file=open(ofile, 'a'))
  for i, a in enumerate(alph):
    hdr = "  'Text Bold {}':\n".format(a)
    pre = "    'prefix': 'tb{}'\n".format(alph[i])
    fmt = r'\\\\boldsymbol{}\\\\{}{}\ $0'.format("{", a, "}")
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
  text_bold()
  text_dollar()
  text_bold_dollar()
  text_dollar_bold()

  text_script()
  text_script_dollar()


if __name__ == "__main__":
  main()
