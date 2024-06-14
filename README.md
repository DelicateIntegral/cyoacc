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