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
cyoacc [directory_path]
```

This will process all JSON files in /path/to/json/files starting with "project" and output the modified files with _light appended to their names.

### Integrating cyoacc into Your Python Code

To use cyoacc in your own Python code, follow these steps:

```python
import os
from cyoacc import process_json_file

def main(directory=None):
    # If no directory is provided, use the directory where the script exists
    if directory is None:
        directory = os.path.dirname(os.path.realpath(__file__))
    
    # Process all JSON files in the specified directory
    for filename in os.listdir(directory):
        if filename.startswith("project") and filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            process_json_file(file_path)

if __name__ == "__main__":
    # You can specify a directory here or leave it as None to use the current directory
    main('/path/to/json/files')
```