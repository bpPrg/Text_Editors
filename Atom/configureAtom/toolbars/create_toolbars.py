#!python
# -*- coding: utf-8 -*-#
"""
@author: Bhishan Poudel

@date: Oct 4, 2017

@email: bhishanpdl@gmail.com

:Topic: Create toolbar entries for atom package almighty toolbar

"""
# Imports
import numpy as np

icons = np.genfromtxt('ion_variables.less',dtype=str)

# icons = ['android-folder-open']

with open ('a.cson','w') as fo:
    for icon in icons:
        toolbar = '''
{
"type": "button",
"tooltip": "%s",
"callback": "advanced-open-file:toggle",
"icon": "%s",
"iconset": "ion"
},
{
"type": "spacer"
},
'''%(icon,icon)
        fo.write(toolbar.lstrip())
