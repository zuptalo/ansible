import base64
import fnmatch
import json
import os


def parse_gitignore(gitignore_path):
    if not os.path.exists(gitignore_path):
        return []

    with open(gitignore_path, 'r') as f:
        patterns = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return patterns


def should_ignore(path, ignore_patterns):
    path_str = str(path)
    for pattern in ignore_patterns:
        if pattern.endswith('/'):
            if fnmatch.fnmatch(path_str + '/', pattern):
                return True
        if fnmatch.fnmatch(path_str, pattern):
            return True
    return False


def get_file_structure(start_path, ignore_patterns):
    structure = {"type": "dir", "name": os.path.basename(start_path), "children": []}

    try:
        items = os.listdir(start_path)
    except PermissionError:
        return None

    for item in sorted(items):
        full_path = os.path.join(start_path, item)
        rel_path = os.path.relpath(full_path, start_path)

        if should_ignore(rel_path, ignore_patterns):
            continue

        if os.path.isdir(full_path):
            subdir = get_file_structure(full_path, ignore_patterns)
            if subdir:
                structure["children"].append(subdir)
        else:
            try:
                with open(full_path, 'rb') as f:
                    content = base64.b64encode(f.read()).decode('utf-8')
                structure["children"].append({
                    "type": "file",
                    "name": item,
                    "content": content
                })
            except (PermissionError, IsADirectoryError):
                continue

    return structure


def gather_context(directory="."):
    gitignore_path = os.path.join(directory, '.gitignore')
    ignore_patterns = parse_gitignore(gitignore_path)

    # Add default git ignore patterns
    ignore_patterns.extend(
        ['.git/', '.gitignore', '__pycache__/', 'README.md', 'LICENSE', 'project_context.json', 'ai.py', '*.pyc', '*.pyo'])

    structure = get_file_structure(directory, ignore_patterns)

    return {
        "directory_structure": structure,
        "ignore_patterns": ignore_patterns
    }


def save_context(output_file="project_context.json"):
    context = gather_context()
    with open(output_file, 'w') as f:
        json.dump(context, f, indent=2)


if __name__ == "__main__":
    save_context()
    print(f"Context has been saved to project_context.json")
