"""Test my garden functions."""
__author__ = "730395850"
from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


# add_by_kind function Unit tests
def test_add_by_kind_edge_case() -> None:
    """Add plant kind to empty dictionary."""
    plants_by_kind = {}
    add_by_kind(plants_by_kind, "flower", "daffodil")
    assert plants_by_kind == {"flower": ["daffodil"]}


def test_add_by_kind_use_case() -> None:
    """Add plant to existing plant kind."""
    plants_by_kind = {"flower": ["daffodil"]}
    add_by_kind(plants_by_kind, "flower", "chrysanthemum")
    assert plants_by_kind == {"flower": ["daffodil", "chrysanthemum"]}


# by_date function unit tests
def test_add_by_date_edge_case() -> None:
    """Test adding a plant to an empty month."""
    plants_by_date = {}
    
    add_by_date(plants_by_date, "August", "windflower")
    
    assert plants_by_date == {"August": ["windflower"]}


def test_add_by_date_use_case() -> None:
    """Test adding a plant to an existing month."""
    plants_by_date = {"August": ["windflower"]}
    
    add_by_date(plants_by_date, "August", "gardenia")
    
    assert plants_by_date == {"August": ["windflower", "gardenia"]}


# lookup_by_kind_and_date function unit tests
def test_lookup_by_kind_and_date_no_plants() -> None:
    """Look up non-existent plant kind and month."""
    plants_by_kind = {}
    plants_by_date = {}
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, "flower", "June")
    assert result == "No flower to plant in June."


def test_lookup_by_kind_and_date_use_case() -> None:
    """Look up existing plant kind and month."""
    plants_by_kind = {"flower": ["daffodil", "chrysanthemum"]}
    plants_by_date = {"August": ["windflower", "gardenia"]}
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, "flower", "August")
    assert result == "No flower to plant in August."