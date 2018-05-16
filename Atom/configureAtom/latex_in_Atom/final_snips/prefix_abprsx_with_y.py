#!/Users/poudel/anaconda/bin/python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 22, 2017 Tue
# a     b     p      r      s     xx
# angle bold partial paren script dollar_or_dollarbold

# Imports
import string

# Global Variables
ofile = 'latex_snips.cson'

grk=['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa',
'lambda','mu','nu','xi','omicron','pi','rho','sigma','tau','upsilon','phi',
'chi','psi','omega','Gamma','Delta','Theta','Lambda','Xi','Pi','Sigma','Phi','Psi']

alph=list('abgdezhqiklmnxoprstufcywGDQLXPSFY')
alphabet=list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
CAPS=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

comment=r"""
  #-----------------------------------------------------------------------------
"""

##=======================================================================
## Alphabet Bold, Dollars and Bold Dollars
##=======================================================================
def bold_alphabet():
    """
    Text Bold A
    tba = \boldsymbol{A}
    tb is tau bar.
    tax is tau asterisk dollar.
    """
    print(comment.strip('\n'),file=open(ofile,'w'))
    print("  # Text Bold A".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(alphabet):
        hdr = "  'Text Bold {}':\n".format(a)
        pre = "    'prefix': 'tb{}'\n".format(alphabet[i])
        fmt = r'\\\\boldsymbol{}{}{}\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def dollar_alphabet():
    """
    A Dollar
    xxa = $a$
    tax is tau astrisk dollar.
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Text A Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(alphabet):
        hdr = "  '{} Dollar':\n".format(a)
        pre = "    'prefix': 'xx{}'\n".format(alphabet[i])
        fmt = r'\${}\$\ $0'.format( a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def dollar_bold_alphabet():
    """
    Text Bold A Dollar
    xxba = $\boldsymbol{A}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Text Bold A Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(alphabet):
        hdr = "  'Text Bold {} Dollar':\n".format(a)
        pre = "    'prefix': 'xxb{}'\n".format(alphabet[i])
        fmt = r'\$\\\\boldsymbol{}{}{}\$\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def script_CAPS():
    r"""
    Script A
    say = \mathscr{A}

    Note: \mathscr needs   \usepackage{mathrsfs}
    Only Capital Letters have math script environment.
    For simplicity I use lowercase in autocompletion.
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Script A".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(CAPS):
        hdr = "  'Script {}':\n".format(a)
        pre = "    'prefix': 's{}y'\n".format(CAPS[i].lower())
        fmt = r'\\\\mathscr{}{}{}'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

##=======================================================================
## Greek Letters
##=======================================================================

def greek():
    """
    Greek
    a = \alpha
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Greek".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{}':\n".format(a)
        pre = "    'prefix': '{}'\n".format(alph[i])
        fmt = r'\\\\{}'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def angle():
    """
    Angle Alpha
    aay = \langle\alpha\rangle
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Angle Alpha".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Angle {}':\n".format(a)
        pre = "    'prefix': 'a{}y'\n".format(alph[i])
        fmt = r'\\\\langle \\\\{} \\\\rangle\ $0'.format( a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))



def bold():
    """
    Bold Alpha
    bay = \boldsymbol{\alpha}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Bold Alpha".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Bold {}':\n".format(a)
        pre = "    'prefix': 'b{}y'\n".format(alph[i])
        fmt = r'\\\\boldsymbol{}\\\\{}{}\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def partial():
    r"""
    Partial Alpha
    pay = \partial{\alpha}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Partial Alpha".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Partial {}':\n".format(a)
        pre = "    'prefix': 'p{}y'\n".format(alph[i])
        fmt = r'\\\\partial\\\\{}\ $0'.format( a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def parenthesis():
    r"""
    Parenthesis Alpha
    ray = (\alpha)
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Parenthesis Alpha".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Parenthesis {}':\n".format(a)
        pre = "    'prefix': 'r{}y'\n".format(alph[i])
        fmt = r'(\\\\{})\ $0'.format( a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))



# **************************** Bold ****************************
def angle_bold():
    r"""
    Angle Alpha Bold
    abay = \langle\boldsymbol{\alpha}\rangle
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Angle Bold Alpha".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Angle Bold {}':\n".format(a)
        pre = "    'prefix': 'ab{}y'\n".format(alph[i])
        fmt = r'\\\\langle\\\\boldsymbol{}\\\\{}{}\\\\rangle\ $0'.format( "{", a, "}" )
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def partial_bold():
    r"""
    Partial Bold Alpha
    pbay = \partial\boldsymbol{\alpha}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Partial Alpha Bold".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Partial Bold {}':\n".format(a)
        pre = "    'prefix': 'pb{}y'\n".format(alph[i])
        fmt = r'\\\\partial\\\\boldsymbol{}\\\\{}{}\ $0'.format( "{", a, "}" )
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def parenthesis_bold():
    r"""
    Parenthesis Bold Alpha
    rbay = (\boldsymbol{\alpha})
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Parenthesis Bold Alpha".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Parenthesis Bold {}':\n".format(a)
        pre = "    'prefix': 'rb{}y'\n".format(alph[i])
        fmt = r'(\\\\boldsymbol{}\\\\{}{})\ $0'.format( "{", a, "}" )
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

# **************************** Dollar ****************************

def dollar_greek():
    """
    Alpha Dollar
    ax = $\alpha$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Alpha Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  '{} Dollar':\n".format(a)
        pre = "    'prefix': '{}x'\n".format(alph[i])
        fmt = r'\$\\\\{}\$\ $0'.format(a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def dollar_angle():
    """
    Angle Alpha Dollar
    aayx = $\langle\alpha\rangle$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Angle Alpha Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Angle {} Dollar':\n".format(a)
        pre = "    'prefix': 'a{}yx'\n".format(alph[i])
        fmt = r'\$\\\\langle \\\\{} \\\\rangle\$\ $0'.format( a)
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def dollar_bold():
    """
    Bold Alpha Dollar
    bayx = $\boldsymbol{\alpha}$
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Bold Alpha Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Bold {} Dollar':\n".format(a)
        pre = "    'prefix': 'b{}yx'\n".format(alph[i])
        fmt = r'\$\\\\boldsymbol{}\\\\{}{}\$\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))

def dollar_script():
    r"""
    Script Alpha Dollar
    sayx = $\mathscr{\alpha}$

    Note: \mathscr needs   \usepackage{mathrsfs}
    """
    print(comment.strip('\n'),file=open(ofile,'a'))
    print("  # Script Alpha Dollar".strip('\n'),file=open(ofile,'a'))
    for i,a in enumerate(grk):
        hdr = "  'Script {} Dollar':\n".format(a)
        pre = "    'prefix': 's{}yx'\n".format(alph[i])
        fmt = r'\$\\\\mathscr{}\\\\{}{}\$\ $0'.format("{", a,"}")
        bdy = "    'body': '{}'\n".format(fmt)
        snip = hdr + pre + bdy
        print(snip,file=open(ofile,'a'))


def main():
    """Run main function."""
    print('Creating: ', ofile)

    # Alphabet ==> bold, dollar, and boldDollar
    bold_alphabet()        # tba  = \boldsymbol{A}
    dollar_alphabet()      # xxa  = $a$
    dollar_bold_alphabet() # xxba = $\boldsymbol{a}$
    script_CAPS()          # say  = \mathscr{A}

    # Greek Letters
    greek()              # a = \alpha
    angle()              # aay = \langle\alpha\rangle
    bold()               # bay = \boldsymbol{\alpha}
    partial()            # pay = \partial{\alpha}
    parenthesis()        # ray = (\alpha)

    # Bold Greek Letters
    angle_bold()         # abay = \langle\boldsymbol{\alpha}\rangle
    partial_bold()       # pbay = \partial\boldsymbol{\alpha}
    parenthesis_bold()   # rbay = (\boldsymbol{\alpha})

    # Dollar Greek
    dollar_greek()       # ax = $\alpha$
    dollar_angle()       # aayx = $\langle\alpha\rangle$
    dollar_bold()        # bayx = $\boldsymbol{\alpha}$
    dollar_script()      # sayx = $\mathscr{\alpha}$


if __name__ == "__main__":
    main()
