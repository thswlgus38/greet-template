# Contributing to {{ cookiecutter.package_distribution_name }}

## Set up for development

Create a virtual environment, activate it, and install the package in editable mode:

```console
python -m pip install -e .
```

## Run the tests

Check that the greeting works:

```console
python -c "from {{ cookiecutter.package_import_name }} import greet; print(greet('Hee'))"
```

Expected output: Hello, Hee!

## Send a change

1. Create a branch from main for your change.
2. Commit your change and push the branch to GitHub.
3. Open a pull request from the branch to main.
