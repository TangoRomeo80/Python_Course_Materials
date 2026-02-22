"""
File for utility functions that are used across the project.
"""

from __future__ import annotations

def prompt_non_empty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        else:
            print("Empty input is not allowed. Try again.")

# Function to input name and 
def clean_name(raw_name: str) -> str:
    return raw_name.strip().title()

# Function to input integer
def prompt_int(prompt: str, min_val: int | None = None, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Please enter a valid integer")
            continue

        if min_val is not None and val < min_val:
            print(f"Value must be >= {min_val}")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be <= {max_val}")
            continue

        return val
    
def prompt_float(prompt: str, min_val: float | None = None, max_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Please enter a valid number")
            continue

        if min_val is not None and val < min_val:
            print(f"Value must be >= {min_val}")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be <= {max_val}")
            continue

        return val
