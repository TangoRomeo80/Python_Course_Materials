"""
This module contains all the helper functionalities
"""
from __future__ import annotations 

def prompt_non_empty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s != "":
            return s
        print("Empty input not allowed, please try again.")

def format_name(name: str) -> str:
    return name.title()

def prompt_int(prompt: str, min_value: int = 0, max_value: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if val < min_value:
            print(f"Value must be at least {min_value}. Please try again.")
            continue
        if max_value is not None and val > max_value:
            print(f"Value must be at most {max_value}. Please try again.")
            continue
        return val

def prompt_float(prompt: str, min_value: float = 0.0, max_value: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if val < min_value:
            print(f"Value must be at least {min_value}. Please try again.")
            continue
        if max_value is not None and val > max_value:
            print(f"Value must be at most {max_value}. Please try again.")
            continue
        return val