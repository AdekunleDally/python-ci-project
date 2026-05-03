# My Calculator App
A Sample Python package used to demonstrate GithubActions Pipelines

## Features
- Add numbers
- Subtract numbers
- Multiply numbers
- Divide numbers

# Development
Install locally
* CD to  the root of the project directory
* Ensure you have the correct pyproject.toml file
* Run the commands below

```bash
python -m venv .venv
source .venv/Scripts/activate  (for gitbash)
python -m pip install --upgrade pip
python -m pip install .[dev]
ruff check . --fix
ruff check .
pytest
python -m build
