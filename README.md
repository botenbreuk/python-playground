# python-playground

A simple project to quickly test python functionality.

## Requirements

- Python >= 3.14
- [Poetry](https://python-poetry.org/) for dependency management

## Setting up the project

Install dependencies with Poetry, which creates and manages a virtual
environment for you:

```bash
poetry install
```

## Running the application

Run the entry point via the `start` script:

```bash
poetry run start
```

This scans the project (including subfolders) for `.py` files and runs every
function decorated with `@example`. Files/folders starting with `.` or `_`,
and `__pycache__`, are skipped.

## Adding your own example

Create a `.py` file anywhere in the project, import the decorator from
`main`, and mark your function:

```python
from main import example

@example
def my_example():
    print("hello")
```

The next time you run `poetry run start`, it will be picked up and executed
automatically.

Options:
- `@example(disable=True)` — keep the function marked but skip it during the scan.
- `@example(name="...")` — give the example a display name in the logs.
