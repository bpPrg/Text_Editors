# Files to edit inside `~/.Atom/`  ( or `.atom` in linux)
- init.coffee # eg. to open bashrc, to write date
- keymap.cson # my custom keyboard shortcuts
- snippets.cson # snippets for programming languages (disable built-in autocomplete-plus)
- Copy the file `custom_entries.json` from `atom_important.zip` (also change toolbar-almighty settings).

# Packages to install
Go to Atom > Shell Commands # it will install `atom` and `apm` Atom Package Manager commands.
```
apm install advanced-open-file atom-shell-commands change-case clipboard-plus \
column-select date expand-selection-to-quotes file-icons git-plus highlight-column \
minimap open-terminal-here open-this plain-simple \
restart-atom language-fortran language-markdown language-restructuredtext \
tool-bar tool-bar-almighty markdown-toc markdown-writer markdown-preview-enhanced \
script sequential-number sort-lines toggle-quotes
```
- advanced-open-file
- atom-shell-commands
- change-case
- clipboard-plus
- column-select
- date # change setting
- expand-selection-to-quotes
- file-icons # logo-file-icons
- git-plus
- highlight-column
- language-fortran, language-latex,language-markdown,language-restructuredtext  # also disable unused ones
- markdown-toc, markdown-writer,markdown-preview-enhanced 
- minimap
- open-terminal-here
- open-this
- plain-simple # highlight text files
- restart-atom
- script # settings set executable path for current script location
- sequential-number 
- sort-lines 
- toggle-quotes
- tool-bar
- tool-bar-almighty # also create `~/.Atom/custom_entries.json` (NOT cson) and use this in settings.


# Further packages
- pigments # to see colors highlighted eg. #FF0000
- latex, latexer # I use overleaf, not atom for latex
- preview-inline # inline preview of latex snippet
- wakatime # keep history how much you worked on a project
- zotero-citations
- atom-beautify
- atom-transpose
- break
- click-link
- color-picker # unused
- delete-whitelines
- pandoc-convert
- platform-ide-terminal # cons: opens new terminals each time
- rst-preview-pandoc
- scroll-through-time # for macpro, use touchbar to undo stuffs
- sublime-style-column-selection
- wordcount
- *autocomplete-plus # (NEVER autocomplete-path, too slow) I got too many variable wrong names, decided to use it again!!
- *autocomplete-snippets # I had enabled autocomplete-plus and this on macpro, but it hangs frequently, so disable them.

