from game.potion import Potion, PotionEffect
from playerRPG import PlayerRPG, RPGType

player = PlayerRPG(RPGType.warrior)
player.inventory.append(Potion("Potion de vie", PotionEffect.heal, 10))
player.inventory.append(Potion("Potion de force", PotionEffect.strength, 10))
player.inventory.append(Potion("Potion de défense", PotionEffect.defence, 10))

player.open_inventory()
