import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

# Use in-memory SQLite by patching the database engine before app import
import app.core.database as database
database.engine = create_engine("sqlite:///:memory:")
database.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=database.engine)
database.Base.metadata.create_all(bind=database.engine)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.parametrize(
    "url,expected",
    [
        ("/internal/v1/health/", {"status": "ok"}),
        ("/mcm/v1/products/", {"product": "Sample product"}),
        ("/scm/v1/orders/", {"orders": []}),
    ],
)
def test_endpoints(url, expected):
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == expected
