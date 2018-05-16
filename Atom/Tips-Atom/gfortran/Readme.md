# Compile and run fortran files with flags
We can simply run a fortran file using `script` package, but we need to create profile each time if we 
have to run with flags. There is one alternative to this. 
We can install [atom-shell-commands](https://atom.io/packages/atom-shell-commands) and create a config for any shell commands.

For example, I have added following in my `~/.Atom/config.cson` file:
```
  "atom-shell-commands":
    commands: [
      {
        name: "backup"
        command: "cp"
        arguments: [
          "{FileName}"
          "/Users/poudel/Dropbox/FileBackups/macpro_{FileNameNoExt}{FileExt}"
        ]
        options:
          cwd: "{FileDir}"
          keymap: "ctrl-s ctrl-b"
      }
      {
        name: "gcc"
        command: "gcc"
        arguments: [
          "-Wall"
          "{FileName}"
          "-o"
          "{FileNameNoExt}"
        ]
        options:
          cwd: "{FileDir}"
          keymap: "ctrl-s ctrl-g"
      }
      {
        name: "gfortran"
        command: "gfortran"
        arguments: [
          "-Wall"
          "-L/System/Library/Frameworks/vecLib.framework"
          "-framework"
          "Accelerate"
          "{FileName}"
          "-o"
          "{FileNameNoExt}"
        ]
        options:
          cwd: "{FileDir}"
          keymap: "ctrl-s ctrl-f"
      }
      {
        name: "execute"
        command: "{FileNameNoExt}"
        options:
          cwd: "{FileDir}"
          keymap: "ctrl-s ctrl-e"
      }
      {
        name: "rm"
        command: "rm"
        arguments: [
          "-rf"
          "{FileNameNoExt}"
        ]
        options:
          cwd: "{FileDir}"
          keymap: "ctrl-s ctrl-d"
      }
    ]
```
