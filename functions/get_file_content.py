import os

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is an irregular file: "{file_path}"'
    try:
        with open(target_file, "r") as f:
            out_str = f.read(MAX_CHARS)
        return (
            out_str
            if len(out_str) < MAX_CHARS
            else f'{out_str}[...File "{file_path}" truncated at 10000 characters]'
        )
    except Exception as e:
        return f"Error: {e}"
