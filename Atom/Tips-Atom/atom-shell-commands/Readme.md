# Run bash commands in Atom

```bash
# File: ~/.Atom/custom_entries.json
  {
  "type": "button",
  "tooltip": "MPI execute",
  "callback": "atom-shell-commands:mpiexec",
  "icon": "at",
  "iconset": "ion"
  },
```
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
