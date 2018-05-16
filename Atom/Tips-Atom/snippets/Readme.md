Adding custom snippets in atom editor
======================================

To add custom snippts in atom editor create a file `~/.atom/snippets.cson` and write your snippets.
To find the name `.text.plain` and so on go to the File manager (ctrl, or cmd; ) then go to Packages 
and type `language` and click `Settings` of that language. Then we can see the `scope`.

```
##==============================================================================
## Plain text Snippets
##=============================================================================
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
      'prefix': 'h'
      'body': '''
      Author: Bhishan Poudel, Physics PhD student Ohio University
      Date  : $1

      Topic: $2
      ====================================
      $0
      '''
      
      
##==============================================================================
##          Python SNIPPETS
##==============================================================================
'.source.python':
    'function':
        'prefix': 'def'
        'body': 'def $1($2):\n    $3\n$0'

```
