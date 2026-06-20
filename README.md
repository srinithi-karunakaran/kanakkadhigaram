# Kanakkadhigaram

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Package Version](https://img.shields.io/badge/version-0.1.0-orange)](https://pypi.org/project/kanakkadhigaram/)

A Python library encoding ancient Tamil mathematical systems from the classical text **Kanakkadhigaram** (கணக்காதிகாரம்). This package preserves and makes accessible the mathematical knowledge of medieval Tamil scholars, transforming centuries-old computational methods into modern, usable Python code.

## About Kanakkadhigaram

The **Kanakkadhigaram** is a classical Tamil mathematical text covering practical arithmetic, measurement, agriculture, trade, astronomy, and cosmology. This library systematically implements the mathematical operations, unit conversions, and calculation methods described in this classical work, enabling both cultural preservation and practical computation.

## Features

**7 Domain-Specific Modules:**

- **`enn_arithal`** - Fundamental arithmetic & number theory
  - Number scales (Peruen, Saaram systems)
  - Exponential and geometric progressions
  - Arithmetic sequences and summations
  
- **`alaviyal`** - Units of measurement & weight
  - Length, weight, volume conversions
  - Historical Tamil measurement standards
  - Geometric calculations for measurements

- **`nilam`** - Land area calculations
  - Field area computations (square, circular, triangular)
  - Agricultural land measurements
  - Historical Tamil land units

- **`vivasaya_kanakku`** - Agricultural mathematics
  - Grain calculations (rice, millet)
  - Crop yield estimates
  - Harvest & storage computations

- **`vaniga_kanakku`** - Commerce & trade mathematics
  - Monetary calculations
  - Gold & precious metal quantifications
  - Historical trade unit conversions

- **`porul_alavai`** - Value & asset measurements
  - Material valuations
  - Property assessments
  - Economic unit conversions

- **`andaviyal`** - Cosmology & astronomical calculations
  - Universe age calculations (Kali, Saka, Yugam)
  - Astronomical time conversions
  - Celestial period calculations

## Installation

Install from PyPI:

```bash
pip install kanakkadhigaram
```

Or install from source:

```bash
git clone https://github.com/srinithi-karunakaran/kanakkadhigaram.git
cd kanakkadhigaram
pip install -e .
```

## Quick Start

### Basic Usage

```python
from kanakkadhigaram import enn_arithal, nilam, vivasaya_kanakku

# Number scale conversions
units = enn_arithal.list_peru_en_units()
result = enn_arithal.convert_peru_en(1, "கற்பம்", "அணு")

# Land area calculations
area = nilam.square_area(10)  # 10 x 10 field
circular_area = nilam.circular_area(radius=5)

# Agricultural computations
rice_yield = vivasaya_kanakku.arisi_calculation(quantity=100, unit="மணி")
```

### Working with Modules

```python
# Arithmetic sequences
from kanakkadhigaram.enn_arithal import padiyadi_sum
total = padiyadi_sum(first_term=1, common_diff=2, num_terms=10)

# Measurement conversions
from kanakkadhigaram.alaviyal import edai_alavai
weight_in_grams = edai_alavai.convert_weight(5, "வராகம்", "அணு")

# Astronomical calculations
from kanakkadhigaram.andaviyal import yugam_saka_kali
kali_year = yugam_saka_kali.convert_yugam_to_kali(year=1000)
```

## Module Documentation

### `enn_arithal` - Arithmetic & Number Systems

| Function | Purpose |
|----------|---------|
| `convert_peru_en()` | Convert between magnitude scales |
| `convert_saaram()` | Convert between length scales |
| `list_peru_en_units()` | List available units in Peru scale |
| `exponential_double()` | Compute geometric doubling |
| `padiyadi_ilakkam_sum()` | Sum arithmetic sequences |
| `enn_perukkam()` | Large number expansion |

### `nilam` - Land & Area

| Function | Purpose |
|----------|---------|
| `square_area()` | Calculate square field area |
| `circular_area()` | Calculate circular field area |
| `triangular_area()` | Calculate triangular field area |
| `rectangular_area()` | Calculate rectangular field area |
| `convert_nilam()` | Convert between land units |

### `vivasaya_kanakku` - Agriculture

| Function | Purpose |
|----------|---------|
| `arisi_calculation()` | Rice grain calculations |
| `nell_calculation()` | Millet grain calculations |
| `pala_sulai_kanakku()` | Fruit/crop calculations |
| `pusani_vidai_kanakku()` | Seeding rate calculations |

### `alaviyal` - Measurements

| Function | Purpose |
|----------|---------|
| `edai_alavai()` | Weight conversions |
| `neer_kanaku()` | Liquid volume calculations |
| `kozh_alavu()` | Grain measure conversions |

### `vaniga_kanakku` - Commerce

| Function | Purpose |
|----------|---------|
| `ponn_calculation()` | Gold & precious metal calculations |
| `kall_kannaku()` | Currency & monetary conversions |

### `andaviyal` - Cosmology

| Function | Purpose |
|----------|---------|
| `convert_yugam_to_kali()` | Yugam to Kali conversion |
| `convert_saka_to_kali()` | Saka to Kali conversion |
| `yukam_age_calculation()` | Universe age calculations |
| `nakshatra_time_mapping()` | Constellation & time mappings |

### `porul_alavai` - Values & Measures

| Function | Purpose |
|----------|---------|
| `porul_maa_maatruthal()` | Standard value calculations |
| `kadal_uppu_alavai()` | Salt & sea measures |

##  Testing

Run the test suite:

```bash
pytest tests/
```

Run tests with coverage:

```bash
pytest --cov=kanakkadhigaram tests/
```

Specific module tests:

```bash
pytest tests/test_enn_arithal.py -v
pytest tests/test_nilam.py -v
pytest tests/test_vivasaya_kanakku.py -v
```

##  Historical Context

The Kanakkadhigaram encodes computational wisdom from 10th-century Tamil scholars. Each module maps to a section of the original text relating to

- ** Basic arithmetic (`enn_arithal`)
- ** Measurements (`alaviyal`)
- ** Land calculations (`nilam`)
- ** Agricultural methods (`vivasaya_kanakku`)
- ** Trade calculations (`vaniga_kanakku`)
- ** Valuations (`porul_alavai`)
- ** Cosmological time (`andaviyal`)

## Unit Conversions

### Example: Converting Units

```python
from kanakkadhigaram.enn_arithal import convert_peru_en

# Convert 1 Kalpam to Anu (smallest unit)
result = convert_peru_en(1, "கற்பம்", "அணு")
print(f"1 Kalpam = {result} Anu")

# Check available units
units = list_peru_en_units()
print(f"Available units: {units}")
```

## Use Cases

- **Historical Mathematics Education**: Learn authentic Tamil mathematical traditions
- **Cultural Heritage Preservation**: Access classical Tamil knowledge in modern form
- **Computational History**: Understand ancient computational methods
- **Academic Research**: Reference implementations for historical mathematics papers
- **Educational Projects**: Teach programming using cultural context

## Package Structure

```
kanakkadhigaram/
├── kanakkadhigaram/
│   ├── __init__.py
│   ├── enn_arithal/          # Arithmetic & numbers
│   ├── alaviyal/             # Measurements
│   ├── nilam/                # Land calculations
│   ├── vivasaya_kanakku/     # Agriculture
│   ├── vaniga_kanakku/       # Commerce
│   ├── porul_alavai/         # Values
│   └── andaviyal/            # Cosmology
├── tests/
│   ├── test_enn_arithal.py
│   ├── test_alaviyal.py
│   ├── test_nilam.py
│   ├── test_vivasaya_kanakku.py
│   ├── test_vaniga_kanakku.py
│   ├── test_porul_alavai.py
│   └── test_andaviyal.py
├── README.md
├── LICENSE
└── pyproject.toml
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Add tests for new functionality
4. Commit changes (`git commit -m 'Add amazing feature'`)
5. Push to branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Srinithi Karunakaran

## Acknowledgments

- The Kanakkadhigaram scholars for preserving mathematical knowledge
- The Tamil language community for maintaining classical texts
- Contributors and users who help expand and improve this library

## Support & Contact

For issues, questions, or suggestions:

- Open an issue on [GitHub](https://github.com/srinithi-karunakaran/kanakkadhigaram)
- Refer to test files for usage examples
- Check module docstrings for detailed function documentation

## References

- Saraswathi Mahal Library, Kanakkadhigaram (Thoguppu Nool). Thanjavur: Saraswathi Mahal Library, 1998. [Online]. Available: https://tamildigitallibrary.in/Articles/நூல்-8346-கணக்கதிகாரம்-%28தொகுப்பு%20நூல்%29

---

**Kanakkadhigaram**: Bridging ancient Tamil mathematical wisdom with modern computation.
