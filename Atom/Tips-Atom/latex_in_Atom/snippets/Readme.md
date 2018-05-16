Latex Snippets
===================
- `\mathscr    \usepackage{mathrsfs}`
- `\boldsymbol \usepackage{amsmath}`

# Convension
- a = angle
- s = star or asterisk

# Plain text bold and italic
- `tbf = \textbf{}`
- `tit = \textit{}`

# Greek Letters
- `a = alpha h=eta f=phi q=theta y=psi w=omega`
- `ax = $\alpha$`

# Prefixes_y: Angle, Bold, Partial, Script 
** Prefix **                |  ** Bold **                                   | ** Dollar ** 
----------------------------|-----------------------------------------------|--------------------------------
aay = $\langle\alpha\rangle$|  aaby = $\langle\boldsymbol{\alpha}\rangle$ | XXX
bay = $\boldsymbol{\alpha}$ |  XXX                                        | bayx = $\boldsymbol{\alpha}$
pay = $\partial\alpha$      |  paby = $\partial\boldsymbol{\alpha}$       | XXX
say = $\mathscr{A}$         |  XXX                                        | sayx = $\mathscr{A}$

# Suffixes: Bar, Prime, Hat, Star, Tilde
** Suffix **         |  ** Bold **                       | ** Dollar ** 
---------------------|-----------------------------------|--------------------------------
ab = $\bar\alpha$    |abb = $\boldsymbol{\bar{\alpha}}$   |abx & abbx
ap = $\alpha\prime$  |apb = $\boldsymbol{\alpha\prime}$  |bap = $\boldsymbol{\alpha\prime}$
ah = $\hat\alpha$    |ahb = $\hat{\boldsymbol{\alpha}}$  |ah  = $\hat\alpha$ & xbah = $\hat{\boldsymbol{\alpha}}$
as = $\alpha^*$      |asb = $\boldsymbol{\alpha}^*$     |XXX
at = $\tilde\alpha$  |atb = $\boldsymbol{\tilde{\alpha}}$  |XXX


# Caveats
```bash
# prefixes: a b h p s
# suffices: b p s t      b and s are both prefix and suffix
#
# bb = \mathbold{}
#
# ab ap as at
# bb bp bs bt
# hb hp hs ht
# pb pp ps pt
# sb sp ss st

Solution:
ab = a_bar & yab = angle_b

***** Snippets not made *******
alpha prime bar
alpha prime hat
alpha prime tilde
```
