import subprocess


def main() -> None:
    print("Hello from sussexmews!")


def format() -> None:
    subprocess.run("uv run ruff format .", shell=True)


def lint() -> None:
    subprocess.run("uv run ruff check .", shell=True)


def lintfix() -> None:
    subprocess.run("uv run ruff check --fix .", shell=True)
