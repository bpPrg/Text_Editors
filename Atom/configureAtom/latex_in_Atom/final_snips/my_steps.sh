#!/bin/bash
#
# 1. copy snippets.cson to a.cson here
# 2. search 'tba with leading prime sign and get line number of comment line e.g. 1207
# 3. search beamer and get another line number e.g. 9716
# 4. use sed to delete lines (this deletes lines in a.cson, click that file.)
# 5. again search beamer in a.cson
# 6. Go to column number 1 and paste the contents of latex_snips.cson there.
# 7. copy the contents of a.cson to snippets.cson.
# 8. Check any tex file for the autocompletion.
# 9. Delete the end additional snippet it it is there in snippets.cson
# 10. backup snippets.

## Step 1
rm -r a.cson
cp ~/.Atom/snippets.cson a.cson
/Users/poudel/Applications/Atom.app/Contents/MacOS/Atom a.cson

# step 2
sed -e '1277,9786d' a.cson > b.cson # First check line number !!
/Users/poudel/Applications/Atom.app/Contents/MacOS/Atom b.cson

# Note that in b.cson there are no snippets for greek letters
# ctrl g 1277  should have no previous latex commands.

# search beamer in b.cson
# go to first column of line above this
# copy all from latex_snip.cson
# copy b.cson to snippets.cson
