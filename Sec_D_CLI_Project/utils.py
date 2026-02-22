"""
This module contains the helper utilitty functions
"""
from __future__ import annotations

def prompt_non_empty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Empty input is not allowed. Try again.")

def clean_name(raw_name: str) -> str:
    return raw_name.strip().title()

def prompt_int(prompt: str, min_val: int = 0, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if val < min_val:
            print(f"Value must be at least {min_val}. Try again.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be at most {max_val}. Try again.")
            continue
        return val
    
def prompt_float(prompt: str, min_val: float = 0.0, max_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if val < min_val:
            print(f"Value must be at least {min_val}. Try again.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be at most {max_val}. Try again.")
            continue
        return val