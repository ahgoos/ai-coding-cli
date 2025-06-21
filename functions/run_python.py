import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        cmds = ["python3", target_file]
        if args:
            cmds.extend(args)
        result = subprocess.run(
            cmds,
            timeout=30,
            capture_output=True,
            cwd=abs_working_dir,
            text=True,
        )
        out = []
        if result.stdout:
            out.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            out.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            out.append(f"Process exited with code {result.returncode}")
        return "\n".join(out) if out else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"
