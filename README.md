### What?
This is a python script to invert colors in the JSON files produced by ICC (Interactive CYOA Creator by MeanDelay) without inverting the colors for the point bar. I made this mainly for Lt. Ouroumov's Worm CYOA.

### Explanation of Code and Comments

#### Imports
- **Imports**: `import os`, `import json`, and `import sys` are used for operating system interaction, JSON manipulation, and handling command-line arguments, respectively.

#### Functions
- **`invert_color(color)`**: Handles inversion of color values in hexadecimal format (`#RRGGBB` or `#RRGGBBAA`).
  - **Purpose**: Inverts the provided color value.
  - **Parameters**: `color` (str) - Hexadecimal color code.
  - **Returns**: Inverted color in the same format as input.
  - **Raises**: `ValueError` if the color format is invalid.

- **`invert_style_recursive(data)`**: Recursively traverses a JSON-like data structure (`dict` or `list`) and applies style inversion.
  - **Purpose**: Processes nested dictionaries or lists to invert style attributes.
  - **Parameters**: `data` (dict or list) - Input JSON-like data structure.
  - **Returns**: Processed data with inverted styles.

- **`invert_style_values(style)`**: Processes a dictionary (`style`) to invert specific style attributes such as color values (`Color` or `BgColor`).
  - **Purpose**: Modifies style attributes based on predefined conditions.
  - **Parameters**: `style` (dict) - Dictionary containing style attributes.
  - **Returns**: Processed dictionary (`inverted_style`) with inverted style attributes.

- **`process_json_file(file_path)`**: Reads a JSON file, processes its contents by applying style inversion, and saves the modified data to a new JSON file.
  - **Purpose**: Handles file I/O and style inversion for JSON data.
  - **Parameters**: `file_path` (str) - Path to the input JSON file.
  - **Output**: Generates a new file (`<input_filename>_light.json`) with inverted style attributes.

- **`main()`**: Entry point of the script. Processes all JSON files in the specified directory whose names start with "project". If no directory is specified, it processes files in the script's directory.
  - **Purpose**: Orchestrates the processing of JSON files within the specified directory.
  - **Parameters**: `directory_path` (str) - Path to the directory containing JSON files. Defaults to the script's directory if not provided.
  - **Workflow**: Iterates through files and invokes `process_json_file` for each qualifying file.

#### Comments
- Each function is documented with a description of its purpose, parameters, return values, and potential exceptions (`Raises` section).
- Inline comments within functions clarify specific sections of code, such as handling different color formats (`#RRGGBB` or `#RRGGBBAA`) or preserving specific keys (`bar keys`).
- The script now accepts an optional directory path argument for processing JSON files. If no path is provided, it defaults to the script's directory.
