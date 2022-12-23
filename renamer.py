#!/usr/bin/python

import os
import sys

code_extensions = [
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".html",
    ".css",
    ".scss",
    ".sass",
    ".less",
    ".json",
    ".md",
    ".txt",
    ".yml",
    ".yaml",
    ".xml",
    ".csv",
    ".sql",
    ".sh",
    ".bat",
    ".ini",
    ".conf",
    ".cfg",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".cs",
    ".java",
    ".go",
    ".rb",
    ".rs",
    ".swift",
    ".kt",
    ".dart",
    ".php",
    ".pl",
    ".pm",
    ".t",
    ".pod",
    ".podspec",
    ".rb",
    ".rake",
    ".gemspec",
    ".podspec",
    ".j2",
    ".jinja",
    ".jinja2",
    ".mustache",
    ".handlebars",
    ".hbs",
    ".html",
    ".htm",
    ".ejs",
    ".vue",
    ".svelte",
    ".elm",
    ".erl",
    ".ex",
    ".exs",
    ".leex",
    ".eex",
    ".slim",
    ".haml",
    ".pug",
    ".jade",
    ".twig",
    ".liquid",
    ".coffee",
    ".litcoffee",
    ".env",
    ".env.example",
    ".env.sample",
    ".env.development",
    ".env.development.local",
    ".env.test",
    ".env.test.local",
    ".env.production",
    ".env.production.local",
    ".env.staging",
    ".env.staging.local",
    ".env.local",
    ".envrc",
    ".env-cmdrc",
    ".dockerignore",
]


def rename_recursive(root_dir, replace_token, new_token):
    for path, subdirs, files in os.walk(root_dir):
        for name in files:
            if replace_token in name:
                os.rename(os.path.join(path, name), os.path.join(path, new_token))

            if not os.path.splitext(name)[1] in code_extensions:
                continue

            with open(os.path.join(path, name), "r") as file:
                filedata = file.read()

            filedata = filedata.replace(replace_token, new_token)
            with open(os.path.join(path, name), "w") as file:
                file.write(filedata)

    if replace_token in root_dir:
        os.rename(root_dir, root_dir.replace(replace_token, new_token))


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

    rename_recursive(path, word_to_replace, new_word)
