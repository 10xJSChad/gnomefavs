# gnomefavs

gnomefavs is a command-line utility that helps manage GNOME favorite applications presets. It allows users to swiftly save, load, list, and remove configurations, providing a flexible way to customize and switch between app layouts in a GNOME environment.

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

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
