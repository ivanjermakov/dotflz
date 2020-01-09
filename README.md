![ASCII art](https://sun9-19.userapi.com/c857732/v857732190/13b709/A7LNzw5wGQA.jpg)

[![Travis (.com)](https://img.shields.io/travis/com/ivanjermakov/dotflz)](https://travis-ci.com/ivanjermakov/dotflz)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/ivanjermakov/dotflz)](https://github.com/ivanjermakov/dotflz/releases)
[![codecov](https://img.shields.io/codecov/c/gh/ivanjermakov/dotflz)](https://codecov.io/gh/ivanjermakov/dotflz)

# dotflz
Utility to keep copies of dotfiles in one place

## Requirements
Pyhton 3

## Installation

### With PIP
```shell script
pip install dotflz
```

### From source
 1. Clone repository:
    ```shell script
    git clone https://github.com/ivanjermakov/dotflz.git
    cd dotflz
    ```
 2. Mark `bin/dotflz` as executable:
    ```shell script
    chmod +x bin/dotflz
    ```

Optionally add `bin/dotflz` to PATH.

## Usage
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

Example configurations can be found [here](https://github.com/ivanjermakov/dotflz/tree/master/example).
