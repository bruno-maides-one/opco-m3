# tests/test_pdt_client.py
import pytest
from models.pydanticModels import pdtClient

def test_valid_client():
    """Test with valid data"""
    data = {
        "id": 1,
        "nom": "Dupont",
        "prenom": "Jean",
        "sexe": "M",
        "nationalite_francaise": "Oui"
    }
    client = pdtClient(**data)
    assert client.id == 1
    assert client.nom == "Dupont"
    assert client.prenom == "Jean"
    assert client.sexe == "M"
    assert client.nationalite_francaise == "Oui"

def test_missing_field():
    """Test missing required field"""
    with pytest.raises(ValueError):
        pdtClient(id=1, nom="Dupont", prenom="Jean", sexe="M")

def test_invalid_type():
    """Test invalid type for id field"""
    with pytest.raises(ValueError):
        pdtClient(id="123", nom="Dupont", prenom="Jean", sexe="M", nationalite_francaise="Oui")

def test_invalid_enum_value():
    """Test invalid value for nationalite_francaise field"""
    with pytest.raises(ValueError):
        pdtClient(id=1, nom="Dupont", prenom="Jean", sexe="M", nationalite_francaise="Non")

def test_valid_client_with_optional_fields():
    """Test with all required fields"""
    data = {
        "id": 2,
        "nom": "Martin",
        "prenom": "Luc",
        "sexe": "F",
        "nationalite_francaise": "Oui"
    }
    client = pdtClient(**data)
    assert client.id == 2
    assert client.nom == "Martin"
    assert client.prenom == "Luc"
    assert client.sexe == "F"
    assert client.nationalite_francaise == "Oui"