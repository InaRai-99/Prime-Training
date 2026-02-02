factory = CharacterFactory()

character = factory.create_character("warrior")
print(character.attack())

character = factory.create_character("mage")
print(character.attack())
