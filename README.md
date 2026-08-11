# vCard to CSV Converter

A lightweight Python script designed to parse raw vCard (`.vcf`) text data and convert structured contact attributes into a clean CSV spreadsheet (`contacts.csv`).

## Overview

This tool parses raw `vCard v2.1` formatted strings, extracts essential contact fields, and exports them directly into a structured CSV file. It provides an efficient solution for migrating contacts or preparing data for analysis.

## Key Features

* **Multi-Field Extraction**: Captures Name (`N`), Formatted Name (`FN`), Multiple Telephone Numbers (`CELL`, `HOME`, `WORK`, `PREF`), and Organization (`ORG`).
* **Zero Dependencies**: Relies strictly on standard Python library modules (`csv`).
* **Customizable Parsing**: Simple string manipulation logic that can be adapted for custom or extended vCard tags.

## Output Schema

The resulting `contacts.csv` file uses the following headers:

| Field Header |     Description        |    Example             |
| ---          | ---                    | ---                    |
| `N`          | Structured Name        | `;Samsung Helpline;;;` |
| `FN`         | Formatted Name         | `Samsung Helpline`     |
| `TEL;CELL:`  | Mobile Phone Number    | `180012321`            |
| `TEL;HOME:`  | Home Phone Number      | `180012322`            |
| `TEL;WORK:`  | Work Phone Number      | `180012323`            |
| `TEL;PREF:`  | Preferred Phone Number | `180012324`            |
| `ORG`        | Organization / Company | `Samsung`              |

## Usage Guide

### Prerequisites

* Python 3.x installed on your system.

### Quick Start

1. **Clone or Download**: Copy the code script into a local directory as `main.py`.
2. **Add Your vCard Data**: Open `main.py` in your text editor and paste your raw vCard block inside the triple-quoted string (`vcard_data = """..."""`).
3. **Execute the Script**: Run the file using your terminal or Python interpreter:
```bash
python main.py

```


4. **Access the Output**: Locate the generated `contacts.csv` file in the same directory.

---

Would you like help extending this script to parse `.vcf` files dynamically from disk instead of using a hardcoded string?
