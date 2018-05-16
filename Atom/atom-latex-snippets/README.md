# atom-latex-snippets
This is a comprehensive list of latex snippets for atom editor.
To use the autocompletion feature in atom, add the contents of `atom-latex-snippets.cson` to your `~/.Atom/snippets.cson` file.

**Package Recommendations:**
```bash
Recommended packages to use latex in Atom:
language-latex
latex
latexer

Similar Packages: latex-completions and autocomplete-plus
```

** Usage:**
```bash
Usage:
tba = \boldsymbol{a}
xxa = $a$
And so on.
```

**Snippets Description:**
```bash
Text            A               Bold            Dollar
-----------------------------------------------------------
Bold            tba             tba             tbax
Dollar          xxa             xxba            xxa
Script          say             say             sayx

tsb = tau script bold

Prefixes_y: Angle, Bold, Partial (a.y b.y p.y)
Suffixes  : Bar, Prime, Hat, Star, Tilde (b. p. h. s. t.)


Prefix/Suffix   A               Bold            Dollar         Bold Dollar
---------------------------------------------------------------------------
Angle           aay             aaby            aayx           aabyx
Bold            bay             bay             bayx           bayx    
Partial         pay             paby            payx           pabyx
----------------------------------------------------------------------------
Star            as              asb             asx            asbx
Bar             ab              abb             abx            abbx
dot             ad              adb             adx            adbx
Prime           ap              apb             apx            apbx
Hat             ah              ahb             ahx            ahbx
Tilde           at              atb             atx            atbx
Modulus         am              amb             amx            ambx
zero            a0              a0b             a0x            a0bx
one             a1              a1b             a1x            a1bx
two             a2              a2b             a2x            a2bx
three           a3              a3b             a3x            a3bx
```
