"""Some functions for my garden plan."""
__author__ = "730395850"


def add_by_kind(plants_by_kind: dict[str, list[str]], plant_kind: str, plant: str) -> None: 
    """Add a plant to the dictionary of plants grouped by kind."""
    if plant_kind in plants_by_kind:  # Check if the key "plant_kind" is in "plants_by_kind"
        plants_by_kind[plant_kind].append(plant)
    else:  # If key plant_kind is NOT in "plants_by_kind"
        plants_by_kind[plant_kind] = [plant]


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add a plant to the dictionary of plants grouped by month."""
    if month in plants_by_date:
        plants_by_date[month].append(plant)
    else:
        plants_by_date[month] = [plant]


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], plant_kind: str, month: str) -> str:
    """Look up plants of a specific kind to be planted in a given month."""
    if plant_kind not in plants_by_kind:
        return f"No {plant_kind} to plant in {month}."

    assert month in plants_by_date
    list_of_plants_by_kind = plants_by_kind[plant_kind]
    combined = []
    list_of_plants_by_date = plants_by_date[month]

    for plant in list_of_plants_by_kind:
        if plant in list_of_plants_by_date:
            combined.append(plant)

    if len(combined) > 0:
        return f"{plant_kind}s to plant in {month}: {combined}"
    else:
        return f"No {plant_kind} to plant in {month}."
