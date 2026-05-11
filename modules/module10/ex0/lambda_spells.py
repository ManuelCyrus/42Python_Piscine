def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    Sort artifacts by power in descending order.
    """
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(
    mages: list[dict],
    min_power: int
) -> list[dict]:
    """
    Filter mages with power >= min_power.
    """
    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages
        )
    )


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Add decorative symbols around spell names.
    """
    return list(
        map(
            lambda spell: f"* {spell} *",
            spells
        )
    )


def mage_stats(mages: list[dict]) -> dict:
    """
    Calculate mage power statistics.
    """
    if not mages:
        return {
            "max_power": 0,
            "min_power": 0,
            "avg_power": 0.0
        }

    max_power = max(
        mages,
        key=lambda mage: mage["power"]
    )["power"]

    min_power = min(
        mages,
        key=lambda mage: mage["power"]
    )["power"]

    avg_power = round(
        sum(
            map(lambda mage: mage["power"], mages)
        ) / len(mages),
        2
    )

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":

    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Shadow Dagger", "power": 76, "type": "dagger"}
    ]

    mages = [
        {"name": "Merlin", "power": 95, "element": "fire"},
        {"name": "Morgana", "power": 80, "element": "shadow"},
        {"name": "Ezren", "power": 65, "element": "ice"}
    ]

    spells = [
        "fireball",
        "heal",
        "shield"
    ]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)

    for artifact in sorted_artifacts:
        print(
            f"{artifact['name']} "
            f"({artifact['power']} power)"
        )

    print("\nTesting power filter...")
    strong_mages = power_filter(mages, 70)

    for mage in strong_mages:
        print(
            f"{mage['name']} "
            f"({mage['power']} power)"
        )

    print("\nTesting spell transformer...")
    print(*spell_transformer(spells))

    print("\nTesting mage stats...")
    print(mage_stats(mages))