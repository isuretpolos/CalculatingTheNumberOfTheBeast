#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Number of the Beast — Arithmetic Demonstration (Terminal Edition)

This script displays the biblical arithmetic that leads to 666 in a clear,
stepwise manner with colored terminal output.

Framework:
  1) Start from perfection: 144,000 (Rev 7:4; 14:1) = 12 × 12,000
  2) Subtract the deficiency (Eccl 1:15; 2 Pet 3:8): 1/1000 of 144,000 → 144
  3) Divide by 6 (human imperfection) three times: → 666 (Rev 13:18)

Usage:
  python calculate_the_number_of_the_wild_beast_colored.py
  python calculate_the_number_of_the_wild_beast_colored.py --no-color
  python calculate_the_number_of_the_wild_beast_colored.py --brief
"""

from __future__ import annotations
import argparse
import sys

# --- ANSI color palette (disabled with --no-color or when stdout is not a TTY) ---
class Palette:
    def __init__(self, enabled: bool) -> None:
        def c(code: str) -> str:
            return code if enabled else ""
        self.reset   = c("\033[0m")
        self.dim     = c("\033[2m")
        self.bold    = c("\033[1m")
        self.italic  = c("\033[3m")
        self.uline   = c("\033[4m")

        self.cyan    = c("\033[36m")
        self.blue    = c("\033[34m")
        self.green   = c("\033[32m")
        self.yellow  = c("\033[33m")
        self.red     = c("\033[31m")
        self.magenta = c("\033[35m")
        self.gray    = c("\033[90m")

# --- Core arithmetic ---
def compute():
    perfection = 144_000
    lack = perfection // 1000            # 1/1000 → 144
    imperfect = perfection - lack        # 143,856

    d1 = imperfect // 6                  # 23,976
    d2 = d1 // 6                         # 3,996
    beast = d2 // 6                      # 666

    return {
        "perfection": perfection,
        "lack": lack,
        "imperfect": imperfect,
        "d1": d1,
        "d2": d2,
        "beast": beast,
    }

def shortage(n: int, thousand_block: int) -> int:
    """Return how much n is short of the next exact 'thousand_block' multiple.
       Example: shortage(23976, 1000) -> 24 (short of 24,000)."""
    remainder = n % thousand_block
    return (thousand_block - remainder) if remainder != 0 else 0

# --- Pretty printing ---
def hr(ch: str = "─", width: int = 64) -> str:
    return ch * width

def title(c: Palette, text: str) -> None:
    print(f"{c.bold}{c.cyan}{text}{c.reset}")

def subtitle(c: Palette, text: str) -> None:
    print(f"{c.bold}{c.blue}{text}{c.reset}")

def kv(c: Palette, label: str, value: str) -> None:
    print(f"{c.dim}{label:<22}{c.reset} {value}")

def formula(c: Palette, left: str, right: str) -> None:
    print(f"{c.bold}{left}{c.reset} {c.dim}→{c.reset} {right}")

def bullet(c: Palette, text: str, color: str | None = None) -> None:
    col = getattr(c, color) if (color and hasattr(c, color)) else ""
    print(f"  • {col}{text}{c.reset}")

def render(args) -> int:
    use_color = (sys.stdout.isatty() and not args.no_color)
    c = Palette(use_color)

    data = compute()

    # Header
    title(c, "The Number of the Beast — A Biblical Calculation")
    print(hr())
    bullet(c, 'Revelation 13:18 calls us to "calculate" (Greek: psephizō).', "magenta")
    bullet(c, "Numbers in Revelation carry consistent symbolism, not letter puzzles.", "magenta")
    print(hr())

    # Step 1
    subtitle(c, "Step 1 — Begin with Perfection (Rev 7:4; 14:1)")
    kv(c, "Perfection:", f"{c.green}{data['perfection']:,}{c.reset}")
    formula(c, "12 × 12,000", f"{c.green}144,000{c.reset}")
    print()

    # Step 2
    subtitle(c, "Step 2 — Subtract the Deficiency (Eccl 1:15; 2 Pet 3:8)")
    kv(c, "One-thousandth (lack):", f"{c.yellow}{data['lack']:,}{c.reset}")
    kv(c, "After subtraction:", f"{c.yellow}{data['imperfect']:,}{c.reset}  "
                                f"{c.dim}(144,000 − 144){c.reset}")
    print()

    # Step 3
    subtitle(c, "Step 3 — Divide by Six, Three Times (Human Imperfection)")
    kv(c, "First division (÷6):", f"{c.red}{data['d1']:,}{c.reset}"
                                  f"  {c.gray}(short of 24,000 by {shortage(data['d1'],1000)}){c.reset}")
    kv(c, "Second division (÷6):", f"{c.red}{data['d2']:,}{c.reset}"
                                   f"  {c.gray}(short of 4,000 by {shortage(data['d2'],1000)}){c.reset}")
    kv(c, "Third division (÷6):", f"{c.red}{data['beast']:,}{c.reset}")
    print()

    # Meaning
    subtitle(c, "Meaning — From Perfection to Absolute Imperfection")
    bullet(c, f"{c.green}144,000{c.reset}: divine completeness and perfection.")
    bullet(c, f"Subtract {c.yellow}144{c.reset}: the marked shortfall of one divine day.")
    bullet(c, f"Three divisions by {c.red}6{c.reset}: intensified human imperfection → "
              f"{c.bold}{c.red}{data['beast']}{c.reset}.")
    print(hr())
    print(f"{c.bold}Result:{c.reset} {c.red}{data['beast']}{c.reset}")
    print(hr())

    if args.proof:
        print(f"Proof: 666*216 + 144 = {666*216 + 144} (should be 144000)")

    if not args.brief:
        subtitle(c, "Notes")
        bullet(c, "The arithmetic mirrors the symbolism; the method and result carry the same meaning.")
        bullet(c, "This approach stays within Scripture’s arithmetic rather than importing Gematria.")
        bullet(c, "You can toggle colors with --no-color and shorten output with --brief.")
        print(hr())

    return 0

def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description="Display the biblical arithmetic that yields 666, step by step."
    )
    p.add_argument("--no-color", action="store_true", help="Disable ANSI colors.")
    p.add_argument("--brief", action="store_true", help="Show a compact output.")
    p.add_argument("--proof", action="store_true", help="Reverse calculation.")
    args = p.parse_args(argv)
    return render(args)

if __name__ == "__main__":
    raise SystemExit(main())
