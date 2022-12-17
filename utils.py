import os


def load_session_cookie():
    with open("session_cookie.txt") as file:
        return file.readline()


def load_input():
    files = []
    for file_name in [f for f in os.listdir() if f.startswith("input") and f.endswith(".txt")]:
        with open(file_name) as file:
            files.append(file.read())

    return files[0] if len(files) == 1 else files
