#!/usr/bin/python
import shutil
import sys
import renamer

print("useful duplicator script")

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


def main():
    path = sys.argv[1]
    word_to_replace = sys.argv[2]
    new_word = sys.argv[3]

    if not path:
        raise Exception("Please provide a path to the directory to duplicate")

    if not word_to_replace:
        raise Exception("Please provide a word to replace")

    if not new_word:
        raise Exception("Please provide a new word")

    target_path = path.replace(word_to_replace, new_word)
    shutil.copytree(path, target_path, ignore=ignore)
    renamer.rename_recursive(target_path, word_to_replace, new_word)
