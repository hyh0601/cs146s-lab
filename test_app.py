import pytest

from app import apply_discount, discount_rate, invoice_total, line_total


def test_line_total():
    assert line_total(3, 4) == 12


def test_discount_rate():
    assert discount_rate(20) == 0.2


def test_no_discount():
    assert apply_discount(100, 0) == 100


def test_twenty_percent_off():
    assert apply_discount(100, 20) == 80


def test_discount_out_of_range():
    with pytest.raises(ValueError):
        apply_discount(100, 150)


def test_invoice_total_with_discount():
    assert invoice_total([(3, 4), (2, 5)], 10) == pytest.approx(19.8)


def test_empty_invoice():
    assert invoice_total([]) == 0
