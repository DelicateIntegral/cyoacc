# cyoacc

`cyoacc` is a Python module designed to invert colors in JSON files, specifically produced by Interactive CYOA Creator (ICC) by MeanDelay. This tool is useful for creators who need to invert color schemes in their CYOAs without altering the point bar colors. I made this mainly for Lt. Ouroumov's Worm CYOA.

## Features

- Inverts colors in JSON files produced by ICC.
- Preserves the colors of the point bar.
- Processes all JSON files in a specified directory or the script's directory if none is provided.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/DelicateIntegral/cyoacc.git
    cd cyoacc
    ```

2. **Install the Module:**

    ```bash
    pip install .
    ```

## Usage

After installation, you can use the `cyoacc` command to process JSON files:

### Command Line Interface

```bash
cyoacc [directory_path] [boolean_value]
```

This will process all JSON files in [directory_path] which do not have "_light" in their name and output the modified files with _light appended to their names. It overwrites any previous outputs. [boolean_value] here decides whether the output is minified or not. True for minified and False is default.

### Integrating cyoacc into Your Python Code

To use cyoacc in your own Python code, follow these steps:

```python
import os
from cyoacc import process_json_file

def main(directory=None, minify=False):
    # Use current working directory if no argument provided
    if directory is None:
        directory = os.getcwd()  
    
    # Process all JSON files in the specified directory
    files = os.listdir(directory_path)
    for filename in files:
        if "_light" not in filename and filename.endswith(".json"):
            file_path = os.path.join(directory_path, filename)
            process_json_file(file_path, minify)

if __name__ == "__main__":
    # You can specify a directory here or leave it as None to use the current directory
    # You can specify True if you want minified outputs or leave blank for default False
    main('/path/to/json/files', True)
```