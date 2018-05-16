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
ofile = 'templates/all_latex_snippets.cson'


def main():
  """Run main function."""
  headers = 'templates/latex_headers.cson'
  text = 'templates/text_bold_dollar_script.cson'
  greek = 'templates/greek_snippets.cson'
  footers = 'templates/latex_footers.cson'

  filenames = [headers, text, greek, footers]
  with open(ofile, 'w') as fo:
    for fname in filenames:
      with open(fname) as fi:
        for line in fi:
          fo.write(line)

  filenames = ['templates/snippets_without_latex.cson',
               'templates/all_latex_snippets.cson']
  with open('bhishan_snippets.cson', 'w') as fo:
    for fname in filenames:
      with open(fname) as fi:
        for line in fi:
          fo.write(line)


if __name__ == "__main__":
  main()
