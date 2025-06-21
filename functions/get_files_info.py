import os


def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        out_str = ""
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            out_str += f"- {filename}: file_size={os.path.getsize(filepath)} bytes, is_dir={os.path.isdir(filepath)}\n"
        return out_str
    except Exception as e:
        return f"Error: {e}"

