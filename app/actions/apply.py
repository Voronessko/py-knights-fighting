from __future__ import annotations


def apply_armour(player: dict) -> None:
    player["protection"] = 0
    for item in player["armour"]:
        player["protection"] += item["protection"]


def apply_weapon(player: dict) -> None:
    player["power"] += player["weapon"]["power"]


def apply_potion_if_exist(player: dict) -> None:
    if player["potion"]:
        if "power" in player["potion"]["effect"]:
            player["power"] += player["potion"]["effect"]["power"]

        if "protection" in player["potion"]["effect"]:
            player["protection"] += player["potion"]["effect"]["protection"]

        if "hp" in player["potion"]["effect"]:
            player["hp"] += player["potion"]["effect"]["hp"]


def apply_all_for(player: dict) -> None:
    apply_armour(player)
    apply_weapon(player)
    apply_potion_if_exist(player)
