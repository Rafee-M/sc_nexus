"""A-120: with API_TOKEN set, every route but `/` and /health needs the bearer token."""

from __future__ import annotations

import pytest
from cportal_api.main import create_app
from fastapi.testclient import TestClient


def test_api_token_gate(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("API_TOKEN", "s3cret-token")
    c = TestClient(create_app())
    assert c.get("/health").status_code == 200
    assert c.get("/api/v1/meta").status_code == 401
    bad = c.get("/api/v1/meta", headers={"Authorization": "Bearer nope"})
    assert bad.status_code == 401 and bad.json()["title"] == "Unauthorized"
    ok = c.get("/api/v1/meta", headers={"Authorization": "Bearer s3cret-token"})
    assert ok.status_code == 200


def test_public_root_only_exact_paths(monkeypatch: pytest.MonkeyPatch) -> None:
    """`/` (landing JSON) is public too, but only as an exact path: docs and data stay gated."""
    monkeypatch.setenv("API_TOKEN", "s3cret-token")
    c = TestClient(create_app())
    root = c.get("/")
    assert root.status_code == 200
    assert set(root.json()) == {"name", "status", "version", "health", "docs", "api"}
    assert "s3cret-token" not in root.text
    for path in ("/docs", "/openapi.json", "/api/v1/meta", "/healthz"):
        assert c.get(path).status_code == 401, path
