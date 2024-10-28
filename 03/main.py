import sys
from pathlib import Path
from colorama import Fore


class NoPathProvided(Exception):
    pass


class NoDirectoryOrFileExists(Exception):
    pass


def print_directory_structure(directory: Path, space_num: int) -> Path:
    space = " " * space_num
    for path in directory.iterdir():
        if path.exists():
            if path.is_dir():
                print(f"{space}{Fore.BLUE}{path.name}/")
                print_directory_structure(path, space_num + 4)
            else:
                print(f"{space}{Fore.GREEN}{path.name}")


def main():
    if len(sys.argv) > 1:
        absolute_path = sys.argv[1]
        directory = Path(absolute_path)

        if directory.exists():
            print_directory_structure(directory, 1)
        else:
            raise NoDirectoryOrFileExists("Directory doesn't exist!")

    else:
        raise NoPathProvided(
            "Absolute path to file is required! Please provide it as a parameter."
        )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
