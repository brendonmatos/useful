#!/usr/bin/python3
import shutil
import sys
import renamer


ignore = shutil.ignore_patterns(
    "*.pyc",
    "__pycache__",
    ".git",
    ".gitignore",
    ".DS_Store",
    "node_modules",
    "dist",
    "build",
    "venv",
)


if __name__ == "__main__":
    # Get arguments from command line
    path = sys.argv[1]
    word_to_replace = sys.argv[2]
    new_word = sys.argv[3]

    target_path = path.replace(word_to_replace, new_word)
    shutil.copytree(path, target_path, ignore=ignore)
    renamer.rename_recursive(target_path, word_to_replace, new_word)
