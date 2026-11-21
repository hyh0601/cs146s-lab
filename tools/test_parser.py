import pytest
from tools.parser import parse_version, parse_release


def test_parse_simple():
    assert parse_version("python3.12") == (3, 12)


def test_parse_release_three_parts():
    assert parse_release("v1.2.3") == (1, 2, 3)


def test_parse_release_two_parts():
    assert parse_release("v10.4") == (10, 4)


def test_parse_release_missing_v_prefix_raises():
    with pytest.raises(ValueError):
        parse_release("1.2.3")


def test_parse_release_empty_string_raises():
    with pytest.raises(ValueError):
        parse_release("")


def test_parse_release_wrong_part_count_raises():
    with pytest.raises(ValueError):
        parse_release("v1")
    with pytest.raises(ValueError):
        parse_release("v1.2.3.4")


def test_parse_release_ignores_prerelease_suffix():
    assert parse_release("v1.2.3-rc1") == (1, 2, 3)


def test_parse_release_ignores_build_suffix():
    assert parse_release("v2.0+build7") == (2, 0)


def test_parse_release_prerelease_and_build():
    assert parse_release("v1.2.3-rc1+build7") == (1, 2, 3)


def test_parse_release_suffix_with_dots_and_numbers():
    assert parse_release("v1.2.3-rc.1.2") == (1, 2, 3)


def test_parse_release_empty_prerelease_suffix_raises():
    with pytest.raises(ValueError):
        parse_release("v1.2.3-")


def test_parse_release_empty_build_suffix_raises():
    with pytest.raises(ValueError):
        parse_release("v1.2.3+")


def test_parse_release_suffix_does_not_mask_wrong_part_count():
    with pytest.raises(ValueError):
        parse_release("v1.2.3.4-rc1")
