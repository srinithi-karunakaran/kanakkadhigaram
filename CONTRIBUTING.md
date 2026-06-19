# Contributing to Kanakkadhigaram

Thank you for your interest in contributing to Kanakkadhigaram! This document provides guidelines for contributing to the project.

## Code of Conduct

Be respectful and inclusive. We are committed to providing a welcoming environment for all contributors.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists
2. Provide a clear description of the problem
3. Include code examples or steps to reproduce
4. Specify your Python version and environment

### Making Changes

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/kanakkadhigaram.git
   cd kanakkadhigaram
   ```

3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Set up development environment**:
   ```bash
   pip install -e ".[dev]"
   ```

5. **Make your changes**:
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

6. **Run tests**:
   ```bash
   pytest tests/ -v
   ```

7. **Format code**:
   ```bash
   black kanakkadhigaram/
   ```

8. **Check linting**:
   ```bash
   ruff check kanakkadhigaram/
   ```

9. **Type checking**:
   ```bash
   mypy kanakkadhigaram/
   ```

### Pull Request Process

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** with:
   - Clear title describing the change
   - Description of what was changed and why
   - Reference to any related issues
   - Test results showing all tests pass

3. **Address review feedback** promptly

## Code Style

- Follow PEP 8 guidelines
- Use type hints where applicable
- Keep functions focused and well-documented
- Include docstrings for all public functions

### Example Function Style

```python
def convert_peru_en(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert between Peru En magnitude scales.
    
    பாடல் 79-81 (Verses 79-81)
    
    Parameters
    ----------
    value : float
        The value to convert
    from_unit : str
        Source unit (Tamil name)
    to_unit : str
        Target unit (Tamil name)
    
    Returns
    -------
    float
        Converted value
    
    Examples
    --------
    >>> convert_peru_en(1, "கற்பம்", "அணு")
    123456789
    """
```

## Testing

- Write tests for all new functionality
- Ensure all tests pass before submitting PR
- Aim for 80%+ code coverage
- Use descriptive test names

Example test:

```python
def test_convert_peru_en_basic():
    """Test basic unit conversion."""
    result = convert_peru_en(1, "கற்பம்", "అணు")
    assert result > 0
    assert isinstance(result, (int, float))
```

## Documentation

- Update README.md if adding new functionality
- Include docstrings for all public functions
- Add examples to docstrings
- Update CHANGELOG.md with your changes

## Commit Messages

Use clear, descriptive commit messages:

```
Add unit conversion for Peru En scale

- Implement convert_peru_en() function
- Add comprehensive test cases
- Update module documentation
```

Avoid:
- "Fix bug" (be specific)
- "Updates" (what was updated?)
- Very long first lines (keep under 50 chars)

## Module Development

Each module should:

1. **Have an `__init__.py`** exporting public functions
2. **Include type hints** for function signatures
3. **Have docstrings** referencing Kanakkadhigaram verses
4. **Be well-tested** with dedicated test file
5. **Use Tamil names** where culturally appropriate

### Module Structure

```
kanakkadhigaram/
└── my_module/
    ├── __init__.py
    ├── function1.py
    ├── function2.py
    └── test_my_module.py
```

## Questions?

- Check existing issues and discussions
- Review the README and documentation
- Open an issue with your question

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to preserving தமிழ் mathematical heritage!** 
