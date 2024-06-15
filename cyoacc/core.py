import os
import json
import sys

def invert_color(color):
    """
    Inverts the color represented in hexadecimal format (with or without alpha channel).

    Args:
    - color (str): Color in hexadecimal format (#RRGGBB or #RRGGBBAA).

    Returns:
    - str: Inverted color in the same format as input.
    
    Raises:
    - ValueError: If the color format is invalid.
    """
    if color.startswith("#"):
        color = color.lstrip('#')
        if len(color) == 6:
            # RGB format without alpha
            r, g, b = color[:2], color[2:4], color[4:]
            r = format(255 - int(r, 16), '02x')
            g = format(255 - int(g, 16), '02x')
            b = format(255 - int(b, 16), '02x')
            return f"#{r}{g}{b}"
        elif len(color) == 8:
            # RGBA format with alpha
            r, g, b, a = color[:2], color[2:4], color[4:6], color[6:]
            r = format(255 - int(r, 16), '02x')
            g = format(255 - int(g, 16), '02x')
            b = format(255 - int(b, 16), '02x')
            return f"#{r}{g}{b}{a}"
        else:
            raise ValueError(f"Invalid color format: {color}")
    else:
        return color

def invert_style_recursive(data):
    """
    Recursively inverts styles in a JSON-like data structure.

    Args:
    - data (dict or list): JSON-like data structure to be processed.

    Returns:
    - dict or list: Processed data with inverted styles.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "styling" and isinstance(value, dict):
                data[key] = invert_style_values(value)
            else:
                data[key] = invert_style_recursive(value)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            data[i] = invert_style_recursive(item)
    return data

def invert_style_values(style):
    """
    Inverts specific style attributes in a dictionary.

    Args:
    - style (dict): Dictionary containing style attributes.

    Returns:
    - dict: Processed dictionary with inverted style attributes.
    """
    inverted_style = {}
    for key, value in style.items():
        if key.startswith("bar"):
            inverted_style[key] = value  # Preserve "bar" keys unchanged
        elif isinstance(value, str) and (key.endswith("Color") or key.endswith("BgColor")):
            inverted_style[key] = invert_color(value)
        elif isinstance(value, int):
            inverted_style[key] = value  # Handle integer values if needed
        else:
            inverted_style[key] = value
    return inverted_style

def process_json_file(file_path, minify=False):
    """
    Processes a JSON file, applies style inversion, and saves the result to a new file.

    Args:
    - file_path (str): Path to the input JSON file.
    - minify (bool): Boolean value to determine if output should be generated minified
    """
    # Generate output file name
    filename = os.path.basename(file_path)
    base_name, ext = os.path.splitext(filename)
    output_filename = f"{base_name}_light.json"
    output_file_path = os.path.join(os.path.dirname(file_path), output_filename)

    # Remove old outputs
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    # Invert Data
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    inverted_data = invert_style_recursive(data)

    # Write inverted data to the output file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        if minify:
            json.dump(inverted_data, f, indent=None, separators=(',', ':'))
        else:
            json.dump(inverted_data, f, indent=2)
    
    print(f"Processed {file_path} -> {output_file_path}")


def main():
    """
    Main function to process all JSON files in the specified directory whose names start with "project".
    If no directory is specified, it processes files in the current working directory directory.
    """
    # Check for directory path argument
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
        minify = sys.argv[2]
    else:
        directory_path = os.getcwd()  # Use current working directory if no argument provided

    files = os.listdir(directory_path)
    for filename in files:
        if "_light" not in filename and filename.endswith(".json"):
            file_path = os.path.join(directory_path, filename)
            process_json_file(file_path, minify)

# Entry point of the script
if __name__ == "__main__":
    main()
