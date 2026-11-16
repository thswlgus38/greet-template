# {{ cookiecutter.package_distribution_name }}

{{ cookiecutter.package_description }}

## Install

```console
python -m pip install -e .
```

## Use

```console
python -c "from {{ cookiecutter.package_import_name }} import greet; print(greet('Hee'))"
```
