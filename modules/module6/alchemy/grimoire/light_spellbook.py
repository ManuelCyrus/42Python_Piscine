def light_spell_allowed_ingredients() -> list[str]:
    dev = ["earth", "air", "water"]
    return dev

def validate_spell(spell_name: str, ingredients: str) -> bool:
    return bool(spell_name.strip()) and bool(ingredients.strip())


def light_spell_record(spell_name: str, ingredients: str) -> str:
    if validate_spell(spell_name, ingredients):
        return f"Spell '{spell_name}' recorded successfully"
    else:
        return f"Spell '{spell_name}' rejected"