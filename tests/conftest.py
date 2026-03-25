"""pytest configuration for evidencell tests."""

import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "integration: tests that hit external services or large local databases (OAK, network)",
    )
