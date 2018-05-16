# Read cson files in python

We can use `cson` package to read cson files in python.

For example a simple script to read a cson file is given below:

```python
import cson

with open('a.cson','rb') as fi:
    snippets = cson.load(fi)



text = snippets['.text.plain']
diary = text['diary']
prefix = diary['prefix']
body = diary['body']
# print(body)


for k in text.keys():
    print(text[k]['prefix'])
```

Where, the file `a.cson` is given below:

```
##==============================================================================
## Plain text Snippets
##==============================================================================
'.text.plain':
    'diary':
        'prefix': 'hdr'
        'body': """
        ********************************************************************************
        # ==============================================================================
        # Author : Bhishan Poudel; PhD Student Ohio University
        # Email  : bhishanpdl@gmail.com
        # Date   : $1
        # Summary: $2
        # ==============================================================================
        $0
        """
    'header':
        'prefix': 'h2'
        'body': 'Author: Bhishan Poudel\nDate  : $1\n\n$0'

    'header2':
        'prefix': 'h'
        'body': 'Author: Bhishan Poudel\nDate  : $1\n\nTopic : $2\n====================================\n\n$0'

    'topic':
        'prefix': 't'
        'body': '\n\n# =============================================================================\n# Date   : $1\n# Summary: $2\n# =============================================================================\n\n$0'

    'single comment line':
        'prefix': 'line'
        'body': '# =============================================================================\n$0'

    'single comment line typo':
        'prefix': 'lien'
        'body': '# =============================================================================\n$0'

    'lines':
        'prefix': 'lines'
        'body': '##=======================================================================\n## $1\n\##=======================================================================$0'

```
