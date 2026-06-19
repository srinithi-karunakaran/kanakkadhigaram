# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-06-18

### Added

#### Core Modules
- **enn_arithal**: Fundamental arithmetic & number theory
  - `convert_peru_en()` - Magnitude scale conversions
  - `convert_saaram()` - Length scale conversions
  - `exponential_double()` - Geometric doubling system
  - `padiyadi_ilakkam_sum()` - Arithmetic sequence summation
  - `enn_perukkam()` - Large number expansion
  - Number unit discovery and conversion utilities

- **alaviyal**: Units of measurement & weight
  - `edai_alavai()` - Weight unit conversions
  - `neer_kanaku()` - Liquid volume calculations
  - `kozh_alavu()` - Grain measure conversions
  - Historical Tamil measurement standards
  - Geometric calculations for measurements

- **nilam**: Land area calculations
  - `square_area()` - Square field area
  - `circular_area()` - Circular field area
  - `triangular_area()` - Triangular field area
  - `rectangular_area()` - Rectangular field area
  - Land unit conversions
  - Agricultural field measurements

- **vivasaya_kanakku**: Agricultural mathematics
  - `arisi_calculation()` - Rice grain calculations
  - `nell_calculation()` - Millet grain calculations
  - `pala_sulai_kanakku()` - Fruit/crop calculations
  - `pusani_vidai_kanakku()` - Seeding rate calculations
  - Harvest & storage computations

- **vaniga_kanakku**: Commerce & trade mathematics
  - `ponn_calculation()` - Gold & precious metal calculations
  - `kall_kannaku()` - Currency & monetary conversions
  - Historical trade unit systems

- **porul_alavai**: Value & asset measurements
  - `porul_maa_maatruthal()` - Standard value calculations
  - `kadal_uppu_alavai()` - Salt & sea measures
  - Material valuations and property assessments

- **andaviyal**: Cosmology & astronomical calculations
  - `convert_yugam_to_kali()` - Yugam to Kali conversion
  - `convert_saka_to_kali()` - Saka to Kali conversion
  - `anda_adukugal()` - Universe age calculations
  - Astronomical time conversions
  - Celestial period calculations

#### Project Infrastructure
- Complete test suite with 7 test modules
- Modern `pyproject.toml` configuration (PEP 621)
- Comprehensive `README.md` with quick start guide
- `.gitignore` for Python development
- `MANIFEST.in` for source distribution
- `CONTRIBUTING.md` for contributor guidelines
- `LICENSE` (MIT)

#### Documentation
- Module-level docstrings referencing Kanakkadhigaram verses
- Function-level documentation with Tamil context
- Code examples in docstrings
- Historical references and explanations

#### Development Tools Configuration
- **Black** - Code formatter (88-char lines)
- **Ruff** - Fast linter with isort
- **Mypy** - Type checking
- **Pytest** - Test framework with coverage
- **Coverage** - Code coverage reporting

### Project Metadata
- Package version: 0.1.0
- Python support: 3.8+
- License: MIT
- Author: Srinithi Karunakaran

---

## Planned Features (Future Releases)

### [0.2.0] - Planned
- Extended cosmology calculations
- Additional trade mathematics functions
- Expanded documentation with usage examples
- CLI tool for unit conversions
- Web-based calculator interface

### [0.3.0] - Planned
- Performance optimizations
- Extended type hints
- Additional test coverage
- Integration tests
- Benchmarking suite

### [1.0.0] - Long-term Vision
- Complete feature parity with Kanakkadhigaram
- Official documentation site
- Community contributions
- Translation support
- Educational resources

---

## Release History

| Version | Date | Status |
|---------|------|--------|
| 0.1.0 | 2026-06-18 | Latest |

---

## Guidelines for Contributors

When contributing changes, please update this CHANGELOG with:
- **Added** for new features
- **Changed** for existing feature modifications
- **Deprecated** for soon-to-be removed features
- **Removed** for removed features
- **Fixed** for bug fixes
- **Security** for security improvements

### Format Example

```markdown
### [X.Y.Z] - YYYY-MM-DD

#### Added
- New feature description

#### Fixed
- Bug fix description

#### Changed
- Change description
```

---

## Versioning

This project follows [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

---

**Note**: This is the initial release of Kanakkadhigaram on PyPI. The codebase includes 40+ Python modules with implementations of ancient Tamil mathematical systems.

For more information, see [README.md](README.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
