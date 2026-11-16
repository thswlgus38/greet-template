"""{{ cookiecutter.package_description }}."""


def greet(name: str) -> str:
    """Return a greeting for name, or for world if name is blank."""
    return f"Hello, {name.strip() or 'world'}!"
