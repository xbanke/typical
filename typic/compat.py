# flake8: noqa
try:
    from typing import Final, TypedDict  # type: ignore
except ImportError:  # pragma: nocover
    from typing_extensions import Final, TypedDict  # type: ignore
