![ASCII art](https://sun9-30.userapi.com/c853628/v853628642/15d5ac/OLBRQhGJb00.jpg)

# dotflz
Utility to keep copies of dotfiles in one some place

### Requirements
Pyhton 3

### Installation
 1. Clone repository:
    ```shell script
    git clone https://github.com/ivanjermakov/dotflz.git
    cd dotflz
    ```
 2. Optionally add `dotflz` to PATH.

### Usage
````
Usage: dotflz [OPTIONS] COMMAND [ARGS]...

  Utility to keep copies of dotfiles in one place.

Options:
  --help  Show this message and exit.

Commands:
  backup   Backup original files into backup directory.
  copy     Copy files by specified configuration file
  paste    Replace original files with ones from configured directory.
  restore  Restore original files with specified backup directory.
  verify   Verify configuration file.
````
