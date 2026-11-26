# SCD-Group-1-Refactoring (Gilded Rose Kata)

## Project Description
This repository contains the refactored Python implementation of the Gilded Rose Inventory Management System. The objective is to eliminate code smells (Long Method, Magic Numbers, Nested Conditionals) and apply Object-Oriented Design principles while preserving existing behavior.

## How to Run & Test
1. Ensure Python 3 is installed on your machine.
2. Run the unit tests from the root directory:
   ```bash
   python -m unittest discover
   ```

## Group 1 Members
* Alishba Siddique - swen241101074
* Aliya Irfan - swen241101083
* Ummay Rumman - swen241101081
* Benish Eman - swen241101102
* Laiba Kanwal - swen241101095
  
## Changelog
### [v1.0.0] - 2026-11-26
- **Magic Literals & Constants:** Replaced hardcoded numbers (`50`, `0`, `11`, `6`) and item strings with symbolic constants (`PR #1`).
- **Helper Methods & Decomposition:** Extracted `_increase_quality()`, `_decrease_quality()`, and item-specific update methods (`PR #2`).
- **Simplified Conditionals:** Replaced deeply nested `if-else` blocks with guard clauses (`PR #3`).
- **Polymorphic Design:** Implemented `ItemUpdater` class hierarchy (`NormalItemUpdater`, `AgedBrieUpdater`, `BackstagePassUpdater`, `SulfurasUpdater`) (`PR #4`).
- **Testing & Documentation:** Added baseline analysis (`docs/baseline-analysis.md`), target UML diagram (`docs/design-model.png`), and 10 characterization unit tests.

