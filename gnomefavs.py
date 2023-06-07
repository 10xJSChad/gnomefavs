import os
import json
import subprocess
import sys

HOME_DIR                     = os.getenv("HOME")
CONFIG_DIR                   = f"{HOME_DIR}/.config"
GNOMEFAVS_PRESETS_DIRNAME    = "gnomefavs"
GNOMEFAVS_PRESETS_FILENAME   = "gnomefavs.json"
GNOMEFAVS_PRESETS_DIR_PATH   = f"{CONFIG_DIR}/{GNOMEFAVS_PRESETS_DIRNAME}"
GNOMEFAVS_PRESETS_FILE_PATH  = f"{GNOMEFAVS_PRESETS_DIR_PATH}/{GNOMEFAVS_PRESETS_FILENAME}"

PATH_TYPE_NONEXISTENT   = 0
PATH_TYPE_FILE          = 1
PATH_TYPE_DIR           = 2


def run_bash_command(command: str | list) -> str:
    result = subprocess.run(command, stdout=subprocess.PIPE, check=True)
    return result.stdout.decode("utf-8")


def get_path_type(path: str) -> int:
    if path is None:
        raise TypeError("Path is None")

    if os.path.isdir(path):
        return PATH_TYPE_DIR

    if os.path.isfile(path):
        return PATH_TYPE_FILE

    #path does not exist
    return PATH_TYPE_NONEXISTENT


def path_is_dir(path: str) -> bool:
    return get_path_type(path) == PATH_TYPE_DIR


def path_is_file(path: str) -> bool:
    return get_path_type(path) == PATH_TYPE_FILE


def path_is_nonexistent(path: str) -> bool:
    return get_path_type(path) == PATH_TYPE_NONEXISTENT


def create_gnomefavs_dir_and_presets_file() -> None:
    if path_is_nonexistent(GNOMEFAVS_PRESETS_DIR_PATH):
        os.mkdir(GNOMEFAVS_PRESETS_DIR_PATH)

    if path_is_nonexistent(GNOMEFAVS_PRESETS_FILE_PATH):
        create_presets_file()


def validate_paths() -> None:
    if not path_is_dir(HOME_DIR):
        raise FileNotFoundError(f"Could not find home directory at {HOME_DIR}")

    if not path_is_dir(CONFIG_DIR):
        raise FileNotFoundError(f"Could not find config directory at {CONFIG_DIR}")

    # this function performs its own checks
    create_gnomefavs_dir_and_presets_file()


def create_presets_file() -> None:
    with open(GNOMEFAVS_PRESETS_FILE_PATH, "w+") as f:
        f.write("{}")


def read_presets_to_dict() -> dict[str, list[str]]:
    with open(GNOMEFAVS_PRESETS_FILE_PATH) as presets_json:
        return json.load(presets_json)


def write_presets(presets: dict) -> None:
    with open(GNOMEFAVS_PRESETS_FILE_PATH, "w+") as f:
        json.dump(presets, f)


def write_preset(preset_key: str, preset_data: str) -> None:
    presets = read_presets_to_dict()
    presets[preset_key] = preset_data

    with open(GNOMEFAVS_PRESETS_FILE_PATH, "w+") as f:
        json.dump(presets, f)

def get_gnome_favorites() -> str:
    command = ["gsettings", "get", "org.gnome.shell", "favorite-apps"]
    return run_bash_command(command).strip()


def set_gnome_favorites(favorites: list) -> None:
    command = ["gsettings", "set", "org.gnome.shell", "favorite-apps", str(favorites)]
    run_bash_command(command)


def save_preset(preset_key: str) -> None:
    validate_paths()
    write_preset(preset_key, get_gnome_favorites())
    print(f"Saved preset: {preset_key}")


def load_preset(preset_key: str) -> None:
    validate_paths()
    presets = read_presets_to_dict()

    if preset_key in presets:
        set_gnome_favorites(presets[preset_key])
        print(f"Loaded preset: {preset_key}")
    else:
        raise KeyError(f"{preset_key} not found in saved presets")


def remove_preset(preset_key: str) -> None:
    validate_paths()
    presets = read_presets_to_dict()
    presets.pop(preset_key)
    write_presets(presets)
    print(f"Removed preset: {preset_key}")


def list_presets()-> None:
    presets = read_presets_to_dict()
    for key in presets.keys():
        print(key)


def print_help() -> None:
    help_text = """
    Usage: myscript [OPTIONS] [NAME]
    
    This script is used for managing GNOME favorites presets.

    OPTIONS:
        --list             List all the available presets.
        -s, --save NAME    Save the current GNOME favorites as a preset with the given name.
        -l, --load NAME    Load the preset with the given name.
        -r, --remove NAME  Remove the preset with the given name.
        
    If no options are provided, this help message will be printed.
    """

    print(help_text)


# omega lazy arg handling
def main(argv: list) -> None:
    args_count = len(argv)

    if args_count < 1:
        print_help()
        return
    
    if argv[0] == "--list":
        list_presets()
        return

    if args_count < 2:
        print_help()
        return

    if argv[0] == "-s" or argv[0] == "--save":
        save_preset(argv[1])
        return

    if argv[0] == "-l" or argv[0] == "--load":
        load_preset(argv[1])
        return

    if argv[0] == "-r" or argv[0] == "--remove":
        remove_preset(argv[1])
        return


if __name__ == "__main__":
   main(sys.argv[1:])