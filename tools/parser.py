def _parse_parts(text, allowed_parts):
    """Split a dotted numeric string into a tuple of ints.

    Raises ValueError if the segment count is not in ``allowed_parts``
    or any segment is not a valid integer.
    """
    parts = text.split(".")
    if len(parts) not in allowed_parts:
        expected = " or ".join(str(n) for n in sorted(allowed_parts))
        raise ValueError(f"expected {expected} version parts, got {len(parts)}")
    return tuple(int(part) for part in parts)


def parse_version(text):
    version = text.replace("python", "", 1)
    return _parse_parts(version, {2})


def parse_release(text):
    if not text.startswith("v"):
        raise ValueError("release version must start with 'v'")
    core = text[1:]
    if "+" in core:
        core, build = core.split("+", 1)
        if not build:
            raise ValueError("release version must have non-empty build suffix")
    if "-" in core:
        core, prerelease = core.split("-", 1)
        if not prerelease:
            raise ValueError("release version must have non-empty prerelease suffix")
    return _parse_parts(core, {2, 3})
