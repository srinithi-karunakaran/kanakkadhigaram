# Kanakkadhigaram Use Cases: Practical Applications

## Overview

The Kanakkadhigaram library encodes ancient Tamil mathematical systems into modern Python functions. This document demonstrates 18 real-world use cases with **function implementations** drawn from actual library modules.

---

## Use Case 1: Archaeological & Epigraphical Decoding

### Problem
Historical Tamil inscriptions record land measurements in ancient units (வேலி, மா, குழி) that are unfamiliar to modern researchers.

**Historical Example:** A Chola-period inscription records "6½ வேலி of cultivable land" donated to a temple.

### Solution
Use the `nilam` (land) module to convert between traditional Tamil land units.

```python
from kanakkadhigaram.nilam import convert_land

# Convert 6.5 வேலி to மா
result = convert_land(6.5, "வேலி", "மா")
print(f"6.5 வேலி = {result} மா")  
# Output: 6.5 வேலி = 130.0 மா

# Further conversion to குழி
result = convert_land(6.5, "வேலி", "குழி")
print(f"6.5 வேலி = {result} குழி")
# Output: 6.5 வேலி = 13000.0 குழி
```

### Research Benefits
- Decode historical land grants from inscriptions
- Compare land donations across dynasties
- Build digital archives of temple endowments
- Support epigraphical research and digital humanities

---

## Use Case 2: Temple Donation Record Analysis

### Problem
Medieval temple inscriptions record commodity donations using traditional volume units (கலம், தூணி, நாழி) that need conversion for quantitative analysis.

**Historical Example:** "10 கலம் of paddy were endowed for temple lamps" (Brihadisvara Temple inscription)

### Solution
Use the `alaviyal` (measurements) module to convert volume units.

```python
from kanakkadhigaram.alaviyal import neer_kanaku

# The library can convert volume measurements between units
# Example: 10 கலம் in different units
# 1 கலம் = 3 தூணி = 12 குறுணி = 96 நாழி

# For rice/grain volume conversions
from kanakkadhigaram.vivasaya_kanakku import grain_volume_conversion

result = grain_volume_conversion(10)
print(result)
# Shows conversion hierarchy for 10 units of grain
```

### Research Benefits
- Interpret temple donation records accurately
- Compare commodity donations across temples
- Estimate historical agricultural production
- Build quantitative models of temple economies

---

## Use Case 3: Ancient Trade & Market Reconstruction

### Problem
Historical trade records use traditional weight units (கழஞ்சு, பலம், துலாம்) that are difficult to compare across documents.

**Historical Example:** "A merchant donated 25 கழஞ்சு of gold to the temple treasury."

### Solution
Use the `enn_arithal` (arithmetic) module to work with weight hierarchies.

```python
from kanakkadhigaram.enn_arithal import convert_peru_en

# Convert between traditional weight units
# The perl system (peru-en) represents increasingly large quantities
result = convert_peru_en(25, "கழஞ்சு", "பலம்")
print(f"25 கழஞ்சு = {result} பலம்")

# For commodity-specific weights
from kanakkadhigaram.porul_alavai import get_material_weight

# Access traditional weights for specific commodities
gold_weight = get_material_weight("சந்தனம்")  # Sandalwood
pepper_weight = get_material_weight("மிளகு")   # Pepper
```

### Research Benefits
- Interpret commercial measurements in inscriptions
- Compare trade volumes quantitatively
- Reconstruct historical market systems
- Study taxation and economic scales

---

## Use Case 4: Understanding Puranas & Cosmological Time

### Problem
Religious texts (Puranas, Itihasas) describe vast time units (யுகம், சதுர்யுகம், மன்வந்தரம், கற்பம்) whose relationships are difficult to understand.

**Historical Example:** Traditional texts describe "Seven மன்வந்தரங்கள் before the present age."

### Solution
Use the `andaviyal` (cosmology) module to convert between time epochs.

```python
from kanakkadhigaram.andaviyal import convert_prabhanja_kaala

# Convert between cosmological time units
# 1 கற்பம் = 1000 சதுர்யுகம் = 14 மன்வந்தரம்

result = convert_prabhanja_kaala(1, "கற்பம்", "சதுர்யுகம்")
print(f"1 கற்பம் = {result} சதுர்யுகம்")

# Convert உயர்ந்த யுகங்கள் (higher epochs)
result = convert_prabhanja_kaala(1, "கற்பம்", "மன்வந்தரம்")
print(f"1 கற்பம் = {result} மன்வந்தரம்")
```

### Research Benefits
- Interpret cosmological references in classical texts
- Compare timelines across Puranic literature
- Build knowledge graphs of traditional cosmology
- Preserve classical Tamil philosophical concepts

---

## Use Case 5: Panchanga (Astrological Calendar) Reconstruction

### Problem
Temple inscriptions record events using traditional time units (நாழிகை, விநாடி) that don't correspond to modern time.

**Historical Example:** "விழா நடத்தப்பட்டது 12 நாழிகை நேரத்தில்" (Festival held at 12 நாழிகை)

### Solution
Use the `andaviyal` module for time conversions.

```python
from kanakkadhigaram.andaviyal import nakshatra_to_nazhi, convert_prabhanja_kaala

# Convert traditional time units
# 1 நாழிகை (நாழி) = 24 minutes
# 60 நாழிகை = 1 நாள் (24 hours)

# If using constellation-based time:
nazhi_time = nakshatra_to_nazhi("அசுவதம்")
print(f"Ashvini nakshatra duration: {nazhi_time} நாழிகை")

# For time-of-day conversions
# 12 நாழிகை = 4 hours 48 minutes
hours_minutes = 12 * 24 / 60  # = 4.8 hours
```

### Research Benefits
- Reconstruct historical festival schedules
- Interpret temple records accurately
- Match traditional dates to modern calendar
- Study historical astronomy

---

## Use Case 6: Land Area Calculation & Geometric Scaling

### Problem
Historical land records describe fields by geometric shape and dimensions. Need to calculate areas using traditional Tamil methods.

**Historical Example:** "A square field measuring 100 கோல் on each side was granted to the temple."

### Solution
Use the `nilam` (land) module for geometric calculations.

```python
from kanakkadhigaram.nilam import calculate_land_parappu, ambuvil_nilam_kanakkugal

# Calculate area of a square field
# Side = 100 கோல்
side_length = 100
area = calculate_land_parappu(side_length, side_length)
print(f"Square field area: {area} square கோல்")
# Output: 10000 square கோல்

# Use ambuvil_nilam for water-adjacent (riverside) calculations
length, breadth = 100, 80
river_area = ambuvil_nilam_kanakkugal.vil_nilam(length, breadth)
print(f"Rectangular field area: {river_area}")

# Calculate triangular field areas
from kanakkadhigaram.nilam.ambuvil_nilam_kanakkugal import kalappu_nilam
# kalappu = triangle
triangle_area = kalappu_nilam(100, 80, 90)  # sides of triangle
print(f"Triangular field area: {triangle_area}")
```

### Research Benefits
- Interpret historical land surveys
- Calculate field areas from descriptions
- Validate inscriptional land grants
- Compare land sizes across records

---

## Use Case 7: Ancient Agricultural Terminology

### Problem
Historical agricultural texts reference specific methods and units (நெல், அரிசி, பலாச்சுளை segments) that need explanation.

**Historical Example:** "How many segments does a பலாச்சுளை (jackfruit) have?"

### Solution
Use the `vivasaya_kanakku` (agriculture) module.

```python
from kanakkadhigaram.vivasaya_kanakku import estimate_jackfruit_slices

# Estimate jackfruit segments from thorn count
# Kanakkadhigaram describes a mathematical relationship
thorn_count = 20
segments = estimate_jackfruit_slices(thorn_count)
print(f"Estimated segments from {thorn_count} thorns: {segments}")

# Explain the calculation
explanation = explain_jackfruit(thorn_count)
print(explanation)
```

### Research Benefits
- Understand traditional agricultural terminology
- Preserve indigenous farming knowledge
- Interpret classical agricultural texts
- Support ethnobotanical research

---

## Use Case 8: Agricultural Yield Calculations

### Problem
Historical records describe conversions between raw paddy (நெல்) and processed rice (அரிசி) using traditional ratios.

**Historical Example:** "14400 நெல் yields how much அரிசி?"

### Solution
Use the `vivasaya_kanakku` module for grain conversions.

```python
from kanakkadhigaram.vivasaya_kanakku import rice_from_paddy_197

# Convert paddy to rice using traditional ratios
paddy_amount = 14400
rice_result = rice_from_paddy_197(paddy_amount)
print(f"From {paddy_amount} நெல் (paddy): {rice_result}")

# Reverse conversion
from kanakkadhigaram.vivasaya_kanakku import paddy_from_rice_198
rice_amount = 7200
paddy_result = paddy_from_rice_198(rice_amount)
print(f"To produce {rice_amount} அரிசி (rice): {paddy_result} நெல்")
```

### Research Benefits
-  Study historical agricultural productivity
-  Compare yield ratios across texts
-  Preserve traditional farming knowledge
-  Build computational models of historical agriculture

---

## Use Case 9: Understanding Land Shares & Property Papers

### Problem
Historical documents describe property divisions and share allocations that are difficult to verify manually.

**Historical Example:** "A property was divided among 3 heirs; calculate each person's share."

### Solution
Use `enn_arithal` module for proportional reasoning.

```python
from kanakkadhigaram.enn_arithal import sum_of_natural_numbers, paribasha_decode

# For property division with specific ratios:
# Traditional methods for dividing shares proportionally

# Using paribasha (mathematical principles):
a, b, c = 100, 50, 25  # Share ratios
result = paribasha_decode(a, b, c)
print(f"Property division result: {result}")

explanation = explain_paribasha(a, b, c)
print(f"Breakdown: {explanation}")
```

### Research Benefits
- Verify historical property divisions
- Interpret traditional legal documents
- Analyze inheritance records
- Study historical economic practices

---

## Use Case 10: Tamil Mathematical Aptitude & Competitive Testing

### Problem
Educators want to use traditional Tamil arithmetic problems for mathematical training and aptitude assessment.

**Historical Example:** Complex proportion and distribution problems from Kanakkadhigaram can be adapted for modern education.

### Solution
Use library functions for interactive problem-solving.

```python
from kanakkadhigaram.enn_arithal import convert_peru_en, reverse_transform
from kanakkadhigaram.alaviyal import edai_alavai

# Problem: A merchant exchanges 50 units at ratio 3:2. How much does he receive?
# Using proportional reasoning from Kanakkadhigaram

# Convert between unit systems for problem-solving
result = convert_peru_en(50, "அணு", "கற்பம்")
print(f"50 அணு = {result} கற்பம்")

# Reverse engineering: Given final value, find starting value
final = 10000
initial = reverse_transform(final)
print(f"Starting from: {initial} to reach {final}")
```

### Educational Benefits
- Learn authentic Tamil mathematical methods
- Develop numerical reasoning skills
- Compare traditional and modern approaches
- Create interactive learning applications

---

## Use Case 11: Historical Entertainment & Puzzle Systems

### Problem
Traditional Tamil mathematical puzzles in Kanakkadhigaram are difficult to verify and understand without computational support.

**Historical Example:** Sequential operation problems where intermediate steps lead to hidden quantities.

### Solution
Use `enn_arithal` module puzzle functions.

```python
from kanakkadhigaram.enn_arithal import nenaitha_ilakkam_solludhal, reverse_transform

# Interactive puzzle game based on Kanakkadhigaram
game_state = play_game()
print(game_state)

# Or solve puzzles programmatically
final_value = 12000
initial = reverse_transform(final_value)
print(f"If the final value is {final_value}, the starting value was: {initial}")
```

### Research Benefits
- Study historical recreational mathematics
- Understand traditional logical thinking
- Create educational puzzle applications
- Preserve cultural mathematical heritage

---

## Use Case 12: Temple Donation Record Analysis (Extended)

### Problem
Comprehensive temple records often combine multiple measurement types: land, grain, and valuables.

**Historical Example:** "A donor granted 2 வேலி of land AND 5 கலம் of paddy AND 10 பலம் of gold."

### Solution
Combine multiple module functions.

```python
from kanakkadhigaram.nilam import convert_land
from kanakkadhigaram.vivasaya_kanakku import grain_volume_conversion
from kanakkadhigaram.enn_arithal import convert_peru_en

# Multi-unit temple donation analysis
print("=== Temple Donation Analysis ===")

# Land component
land_veli = 2
land_ma = convert_land(land_veli, "வேலி", "மா")
print(f"Land: {land_veli} வேலி = {land_ma} மா")

# Grain component  
grain_kalam = 5
grain_conv = grain_volume_conversion(grain_kalam)
print(f"Grain: {grain_kalam} கலம் = {grain_conv}")

# Precious metal component
gold_palam = 10
gold_kazhansu = convert_peru_en(gold_palam, "பலம்", "கழஞ்சு")
print(f"Gold: {gold_palam} பலம் = {gold_kazhansu} கழஞ்சு")
```

### Research Benefits
- Comprehensive temple record analysis
- Multi-dimensional historical data interpretation
- Comparative temple studies
- Economic history research

---

## Use Case 13: Ancient Trade & Market Reconstruction (Extended)

### Problem
Historical commerce involved multiple commodities, each with specific measurement conventions.

**Historical Example:** "Pepper merchant supplied 600 பலம் at rate X, while sandalwood merchant supplied different quantity at different rate."

### Solution
Use commodity-specific functions from `porul_alavai` and `vaniga_kanakku` modules.

```python
from kanakkadhigaram.porul_alavai import get_material_weight, list_world_items

# Check standard weights for commodities
sandalwood_weight = get_material_weight("சந்தனம்")
pepper_weight = get_material_weight("மிளகு")

print(f"Standard sandalwood weight: {sandalwood_weight}")
print(f"Standard pepper weight: {pepper_weight}")

# List all known commodities
commodities = list_world_items()
for item in commodities:
    weight = get_material_weight(item)
    print(f"{item}: {weight}")
```

### Research Benefits
- Interpret historical commodity records
- Reconstruct market price structures
- Compare trade volumes across regions
- Model historical economic systems

---

## Use Case 14: Historical Land Survey Reconstruction

### Problem
Detailed land surveys require converting between units and validating geometric descriptions.

**Historical Example:** Inscriptions describe: "A square field of 50 கோல் = X குழி total area"

### Solution
Use `nilam` module for comprehensive conversions.

```python
from kanakkadhigaram.nilam import convert_land, calculate_land_parappu

# Step 1: Calculate area in original units
side_length = 50  # கோல்
area_gol = calculate_land_parappu(side_length, side_length)
print(f"Field area: {side_length}² = {area_gol} square கோல்")

# Step 2: Convert to other land units for comparison
# Note: Area conversions vary by region and period
# Use proportional conversion based on linear unit ratios

# If 1 கோல் = 1/100 மா (example ratio)
# Then 2500 square கோல் ≈ 0.25 மா (approximate)

# For precise historical records, check local abbreviations
print("\nFor inscriptional verification:")
print(f"Record describes: {side_length} கோல் square field")
print(f"Computed area: {area_gol} square units")
print("Compare with inscription to validate")
```

### Research Benefits
- Validate historical land grants
- Reconstruct traditional survey systems
- Analyze agricultural holdings
- Study taxation and revenue administration

---

## Use Case 15: Ancient Cosmology & Knowledge Representation

### Problem
Understanding large-number hierarchies (கற்பம், புற்புதம், சங்கம், மத்தியம், பரார்த்தம்) for cosmological knowledge representation.

**Historical Example:** "The universe exists for one பரார்த்தம் = ? years"

### Solution
Use `enn_arithal` module for large-number conversions.

```python
from kanakkadhigaram.enn_arithal import convert_large_number, list_large_number_units

# Access the traditional Tamil large-number system
units = list_large_number_units()
print("Traditional Tamil Large-Number Hierarchy:")
print(units)

# Convert between extremely large units
kalpam = 1
brahma_day = convert_large_number(kalpam, "கற்பம்", "புணரி")
print(f"\n1 கற்பம் = {brahma_day} புணரி")

# Continue up the hierarchy
ultimate = convert_large_number(1, "கற்பம்", "பரார்த்தம்")
print(f"1 கற்பம் = {ultimate} பரார்த்தம்")
```

### Research Benefits
- Study traditional Tamil number systems
- Analyze hierarchical knowledge organization
- Preserve cosmological concepts digitally
- Compare with other ancient number systems

---

## Use Case 16: Nakshatra (Star) System & Celestial Calculations

### Problem
Historical records describe celestial events using traditional star-time relationships that need conversion to modern understanding.

**Historical Example:** "Event occurred during அசுவதம் நாக்ஷத்ரம்" (Ashvini nakshatra period)

### Solution
Use `andaviyal` module for nakshatra-time mappings.

```python
from kanakkadhigaram.andaviyal import nakshatra_to_nazhi, get_symbol

# Map nakshatra to duration
ashvini_duration = nakshatra_to_nazhi("அசுவதம்")
print(f"Ashvini nakshatra duration: {ashvini_duration} நாழிகை")

# Get symbolic representation
symbol = get_symbol("அசுவதம்")
print(f"Ashvini symbol: {symbol}")

# Calculate total night duration for multiple nakshatras
nakshatras = ["அசுவதம்", "பரணி", "கார்த்திகை"]
total_duration = total_night_nazhi(nakshatras)
print(f"Total duration for {len(nakshatras)} nakshatras: {total_duration} நாழிகை")
```

### Research Benefits
- Interpret astronomical references in texts
- Reconstruct historical observation practices
- Model traditional astronomy
- Study historical calendrics

---

## Use Case 17: Calendar System Conversion & Date Correlation

### Problem
Correlating events described in traditional calendars (Saka year, Kali year) with modern Gregorian dates.

**Historical Example:** "Event recorded in Saka year 1500 corresponds to modern year ?"

### Solution
Use `andaviyal` module for calendar conversions.

```python
from kanakkadhigaram.andaviyal import kali_yuga_year, saka_year

# Convert Saka year to Kali year
saka = 1500
kali_equivalent = kali_yuga_year(saka)
print(f"Saka year {saka} = Kali year {kali_equivalent}")

# Reverse conversion: Kali to Saka
kali = 4722
saka_equivalent = saka_year(1, kali)  # Using Prabhava index
print(f"Kali year {kali} ≈ Saka year {saka_equivalent}")

# For modern correlation:
# Saka era begins at 78 CE in Gregorian calendar
# Kali era begins at 3102 BCE in Gregorian calendar
gregorian = 1500 + 78
print(f"Saka {saka} ≈ Gregorian year {gregorian}")
```

### Research Benefits
- Accurately correlate historical dates
- Compare texts using different calendars
- Validate inscriptional dates
- Create chronological frameworks

---

## Use Case 18: Water Clock & Traditional Timekeeping

### Problem
Understanding traditional time measurement using water clocks and natural time units (நாழிகை, விநாடி).

**Historical Example:** "Water clock fills and empties in 12 நாழிகை - what is the modern duration?"

### Solution
Use time conversion concepts from `andaviyal` module.

```python
from kanakkadhigaram.andaviyal import convert_prabhanja_kaala

# Traditional time unit conversions
# 60 நாழிகை = 1 day = 24 hours
# 1 நாழிகை = 24 minutes

# Water clock problem: 12 நாழிகை duration
nazhi = 12
minutes = nazhi * 24
hours = minutes / 60

print(f"{nazhi} நாழிகை = {minutes} minutes = {hours} hours")
# Output: 12 நாழிகை = 288 minutes = 4.8 hours

# For smaller time units
# 60 விநாடி = 1 நாழிகை
vinadi = 720  # 12 நாழிகை in விநாடி
print(f"12 நாழிகை = {vinadi} விநாடி")

# Water-clock rate problems
# "If clock fills in 12 நாழிகை, rate = ?"
# "If 3/4 filled in 9 நாழிகை, full fill time = ?"
full_time = (9 * 4) / 3  # = 12 நாழிகை
print(f"Calculated fill time: {full_time} நாழிகை")
```

### Research Benefits
- Understand traditional timekeeping mechanisms
- Model historical water-clock systems
- Correlate traditional and modern time
- Preserve horological knowledge digitally

---

## Integration Example: Complete Workflow

### Comprehensive Research Task
"Analyze a temple inscription describing a donation of 3 வேலி of land, 10 கலம் of paddy, and 25 பலம் of gold. Calculate total value and compare with other documented donations."

```python
from kanakkadhigaram.nilam import convert_land
from kanakkadhigaram.vivasaya_kanakku import grain_volume_conversion
from kanakkadhigaram.enn_arithal import convert_peru_en

print("="*60)
print("TEMPLE DONATION ANALYSIS - Complete Workflow")
print("="*60)

# Donation 1: Land
land_veli = 3
land_ma = convert_land(land_veli, "வேலி", "மா")
land_kuzhi = convert_land(land_veli, "வேலி", "குழி")

print(f"\n1. LAND COMPONENT:")
print(f"   {land_veli} வேலி = {land_ma} மா = {land_kuzhi} குழி")

# Donation 2: Grain
grain_kalam = 10
grain_data = grain_volume_conversion(grain_kalam)

print(f"\n2. GRAIN COMPONENT:")
print(f"   {grain_kalam} கலம் of paddy")
print(f"   Conversion data: {grain_data}")

# Donation 3: Precious metal
gold_palam = 25
gold_units = convert_peru_en(gold_palam, "பலம்", "கழஞ்சு")

print(f"\n3. PRECIOUS METAL COMPONENT:")
print(f"   {gold_palam} பலம் of gold")
print(f"   = {gold_units} கழஞ்சு")

print("\n" + "="*60)
print("Ready for comparative analysis with other donations")
print("="*60)
```


## Best Practices for Using Kanakkadhigaram

1. **Always import from specific modules** - Not just from main package
2. **Check return types** - Functions return various formats (dicts, floats, strings)
3. **Verify historical contexts** - Use appropriate functions for your period/region
4. **Combine modules** - Complex problems often need multiple modules
5. **Document assumptions** - Note which conversion ratios you used

---

## References

- Saraswathi Mahal Library, Kanakkadhigaram (Thoguppu Nool). Thanjavur: Saraswathi Mahal Library, 1998. [Online]. Available: https://tamildigitallibrary.in/Articles/நூல்-8346-கணக்கதிகாரம்-%28தொகுப்பு%20நூல்%29

---

**Last Updated:** June 2026
**Author:** Srinithi Karunakaran
