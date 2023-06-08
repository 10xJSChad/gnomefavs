# gnomefavs

gnomefavs is a command-line utility that helps manage GNOME favorite applications presets. It allows users to swiftly save, load, list, and remove configurations, providing a flexible way to customize and switch between app layouts in a GNOME environment.

I'm pretty new to this Linux thing, so I can't guarantee that this works on every system, but it should work as long as ~/.config exists and the user has write permissions for it.

## Preview
https://github.com/10xJSChad/gnomefavs/assets/48174610/e05ef270-69c9-4b28-a502-664861265ae1


## Installation

Clone this repository and run the script.

```bash
git clone https://github.com/10xJSChad/gnomefavs.git
cd gnomefavs
python3 gnomefavs.py
```

## Usage

The command line options are as follows:

- `--list` - List all the available presets.
- `-s` or `--save [NAME]` - Save the current GNOME favorites as a preset with the given name.
- `-l` or `--load [NAME]` - Load the preset with the given name.
- `-r` or `--remove [NAME]` - Remove the preset with the given name.

If no options are provided, a help message will be printed.

## Contributing

Anyone is welcome to make a pull request, all contributions are welcome.
