"""Tiny invoice helper built on top of the arithmetic helpers in calc.py."""

from calc import add, divide, multiply, subtract


def line_total(unit_price, quantity):
    """Total for a single invoice line."""
    return multiply(unit_price, quantity)


def discount_rate(percent):
    """Convert a percentage into a fraction, e.g. 20 -> 0.2."""
    return divide(percent, 100)


def apply_discount(amount, percent):
    """Apply a percentage discount to amount."""
    if not 0 <= percent <= 100:
        raise ValueError(f"discount must be between 0 and 100, got {percent}")
    return subtract(amount, multiply(amount, discount_rate(percent)))


def invoice_total(items, discount_percent=0):
    """Total of (unit_price, quantity) pairs after an optional discount."""
    subtotal = add(*[line_total(price, qty) for price, qty in items]) if items else 0
    return apply_discount(subtotal, discount_percent)
