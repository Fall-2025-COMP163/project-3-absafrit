"""
COMP 163 - Project 3: Quest Chronicles
Character Manager Module - Starter Code

Name: Arina Safrit

AI Usage: Used AI Assistance to debug coding

This module handles character creation, loading, and saving.
"""

from fileinput import filename
import os
import numpy

from numpy import character
from custom_exceptions import (
    InvalidCharacterClassError,
    CharacterNotFoundError,
    SaveFileCorruptedError,
    InvalidSaveDataError,
    CharacterDeadError
)

# ============================================================================
# CHARACTER MANAGEMENT FUNCTIONS
# ============================================================================

def create_character(name, character_class):
    """
    Create a new character with stats based on class
    
    Valid classes: Warrior, Mage, Rogue, Cleric
    
    Returns: Dictionary with character data including:
            - name, class, level, health, max_health, strength, magic
            - experience, gold, inventory, active_quests, completed_quests
    
    Raises: InvalidCharacterClassError if class is not valid
    """
    # TODO: Implement character creation
    # Validate character_class first
    # Example base stats:
    # Warrior: health=120, strength=15, magic=5
    # Mage: health=80, strength=8, magic=20
    # Rogue: health=90, strength=12, magic=10
    # Cleric: health=100, strength=10, magic=15
    
    base_stats = {
        'Warrior': {'health': 120, 'strength': 15, 'magic': 5},
        'Mage': {'health': 80, 'strength': 8, 'magic': 20},
        'Rogue': {'health': 90, 'strength': 12, 'magic': 10},
        'Cleric': {'health': 100, 'strength': 10, 'magic': 15}
    }
    if character_class not in base_stats:
        raise InvalidCharacterClassError(f"Invalid class: {character_class}")
    # All characters start with:
    # - level=1, experience=0, gold=100
    # - inventory=[], active_quests=[], completed_quests=[]

    character_data = {
        'name': name,
        'class': character_class,
        'level': 1,
        'health': base_stats[character_class]['health'],
        'max_health': base_stats[character_class]['health'],
        'strength': base_stats[character_class]['strength'],
        'magic': base_stats[character_class]['magic'],
        'experience': 0,
        'gold': 100,
        'inventory': [],
        'active_quests': [],
        'completed_quests': []
    }

    return character_data

def save_character(character, save_directory="data/save_games"):
    """
    Save character to file
    
    Filename format: {character_name}_save.txt
    
    File format:
    NAME: character_name
    CLASS: class_name
    LEVEL: 1
    HEALTH: 120
    MAX_HEALTH: 120
    STRENGTH: 15
    MAGIC: 5
    EXPERIENCE: 0
    GOLD: 100
    INVENTORY: item1,item2,item3
    ACTIVE_QUESTS: quest1,quest2
    COMPLETED_QUESTS: quest1,quest2
    
    Returns: True if successful
    Raises: PermissionError, IOError (let them propagate or handle)
    """
    # TODO: Implement save functionality
    # Create save_directory if it doesn't exist
    # Handle any file I/O errors appropriately
    # Lists should be saved as comma-separated values
    try:
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        filename = os.path.join(save_directory, f"{character['name']}_save.txt")
        with open(filename, 'w') as file:
            file.write(f"NAME: {character['name']}\n")
            file.write(f"CLASS: {character['class']}\n")
            file.write(f"LEVEL: {character['level']}\n")
            file.write(f"HEALTH: {character['health']}\n")
            file.write(f"MAX_HEALTH: {character['max_health']}\n")
            file.write(f"STRENGTH: {character['strength']}\n")
            file.write(f"MAGIC: {character['magic']}\n")
            file.write(f"EXPERIENCE: {character['experience']}\n")
            file.write(f"GOLD: {character['gold']}\n")
            file.write(f"INVENTORY: {','.join(character['inventory'])}\n")
            file.write(f"ACTIVE_QUESTS: {','.join(character['active_quests'])}\n")
            file.write(f"COMPLETED_QUESTS: {','.join(character['completed_quests'])}\n")

    except (PermissionError, IOError) as e:
        # Handle file I/O errors
        print(f"Error saving character: {e}")
        return False

    return True

def load_character(character_name, save_directory="data/save_games"):
    """
    Load character from save file
    
    Args:
        character_name: Name of character to load
        save_directory: Directory containing save files
    
    Returns: Character dictionary
    Raises: 
        CharacterNotFoundError if save file doesn't exist
        SaveFileCorruptedError if file exists but can't be read
        InvalidSaveDataError if data format is wrong
    """
    # TODO: Implement load functionality
    filename = os.path.join(save_directory, f"{character_name}_save.txt")
    if not os.path.exists(filename):
        raise CharacterNotFoundError(f"Character '{character_name}' not found.")    # Check if file exists → CharacterNotFoundError
    character = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ', 1)
                character[key.lower()] = value
    except Exception as e:
        raise SaveFileCorruptedError(f"{e} exists but can't be read") from e # Try to read file → SaveFileCorruptedError

    if not all(key in character for key in ['name', 'class', 'level', 'health', 'max_health', 'strength', 'magic', 'experience', 'gold', 'inventory', 'active_quests', 'completed_quests']):
        raise InvalidSaveDataError(f"data format is wrong") # Validate data format → InvalidSaveDataError

    # Parse comma-separated lists back into Python lists
    character['inventory'] = character['inventory'].split(',') if character['inventory'] else []
    character['active_quests'] = character['active_quests'].split(',') if character['active_quests'] else []
    character['completed_quests'] = character['completed_quests'].split(',') if character['completed_quests'] else []

    return character    

def list_saved_characters(save_directory="data/save_games"):
    """
    Get list of all saved character names
    
    Returns: List of character names (without _save.txt extension)
    """
    # TODO: Implement this function
    # Return empty list if directory doesn't exist
    if not os.path.exists(save_directory):
        return []
    character_names = []
    for filename in os.listdir(save_directory):
        if filename.endswith("_save.txt"):
            character_name = filename[:-9]  # Remove '_save.txt'
            character_names.append(character_name)
    # Extract character names from filenames

    return character_names

def delete_character(character_name, save_directory="data/save_games"):
    """
    Delete a character's save file
    
    Returns: True if deleted successfully
    Raises: CharacterNotFoundError if character doesn't exist
    """
    # TODO: Implement character deletion
    # Verify file exists before attempting deletion
    filename = os.path.join(save_directory, f"{character_name}_save.txt")
    if not os.path.exists(filename):
        raise CharacterNotFoundError(f"Character '{character_name}' not found.")
    os.remove(filename)
    return True

# ============================================================================
# CHARACTER OPERATIONS
# ============================================================================

def gain_experience(character, xp_amount):
    """
    Add experience to character and handle level ups
    
    Level up formula: level_up_xp = current_level * 100
    Example when leveling up:
    - Increase level by 1
    - Increase max_health by 10
    - Increase strength by 2
    - Increase magic by 2
    - Restore health to max_health
    
    Raises: CharacterDeadError if character health is 0
    """
    # TODO: Implement experience gain and leveling
    if is_character_dead(character):
        raise CharacterDeadError(f"Character '{character['name']}' is dead and cannot gain experience.")
    # Check if character is dead first
    # Add experience
    character['experience'] += xp_amount

    # Check for level up (can level up multiple times)
    while character['experience'] >= character['level'] * 100:
        character['level'] += 1
        character['max_health'] += 10
        character['strength'] += 2
        character['magic'] += 2
        character['health'] = character['max_health']
        character['experience'] -= character['level'] * 100

    return character

def add_gold(character, amount):
    """
    Add gold to character's inventory
    
    Args:
        character: Character dictionary
        amount: Amount of gold to add (can be negative for spending)
    
    Returns: New gold total
    Raises: ValueError if result would be negative
    """
    # TODO: Implement gold management
    # Check that result won't be negative
    # Update character's gold

    new_gold = character['gold'] + amount
    if new_gold < 0:
        raise ValueError("Gold amount cannot be negative.")
    character['gold'] = new_gold
    return character['gold']

def heal_character(character, amount):
    """
    Heal character by specified amount
    
    Health cannot exceed max_health
    
    Returns: Actual amount healed
    """
    # TODO: Implement healing
    # Calculate actual healing (don't exceed max_health)
    # Update character health
    if is_character_dead(character):
        raise CharacterDeadError(f"Character '{character['name']}' is dead and cannot be healed.")
    character['health'] += amount
    if character['health'] > character['max_health']:
        character['health'] = character['max_health']
    return amount

def is_character_dead(character):
    """
    Check if character's health is 0 or below
    
    Returns: True if dead, False if alive
    """
    # TODO: Implement death check
    return character['health'] <= 0


def revive_character(character):
    """
    Revive a dead character with 50% health
    
    Returns: True if revived
    """
    # TODO: Implement revival
    # Restore health to half of max_health
    if not is_character_dead(character):
        return False
    character['health'] = character['max_health'] // 2
    return True

# ============================================================================
# VALIDATION
# ============================================================================

def validate_character_data(character):
    """
    Validate that character dictionary has all required fields
    
    Required fields: name, class, level, health, max_health, 
                    strength, magic, experience, gold, inventory,
                    active_quests, completed_quests
    
    Returns: True if valid
    Raises: InvalidSaveDataError if missing fields or invalid types
    """
    # TODO: Implement validation
    # Check all required keys exist
    # Check that numeric values are numbers
    # Check that lists are actually lists
    required_fields = [
        'name', 'class', 'level', 'health', 'max_health',
        'strength', 'magic', 'experience', 'gold',
        'inventory', 'active_quests', 'completed_quests'
    ]
    for field in required_fields:
        if field not in character:
            raise InvalidSaveDataError(f"Missing field: {field}")
    if not isinstance(character['level'], int) or not isinstance(character['health'], int) or not isinstance(character['max_health'], int) or not isinstance(character['strength'], int) or not isinstance(character['magic'], int) or not isinstance(character['experience'], int) or not isinstance(character['gold'], int):
        raise InvalidSaveDataError("Numeric fields must be integers.")
    if not isinstance(character['inventory'], list) or not isinstance(character['active_quests'], list) or not isinstance(character['completed_quests'], list):
        raise InvalidSaveDataError("Inventory and quests must be lists.")
    return True

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER MANAGER TEST ===")
    
    # Test character creation
    try:
        char = create_character("TestHero", "Warrior")
        print(f"Created: {char['name']} the {char['class']}")
        print(f"Stats: HP={char['health']}, STR={char['strength']}, MAG={char['magic']}")
    except InvalidCharacterClassError as e:
        print(f"Invalid class: {e}")
    
    # Test saving
    try:
        save_character(char)
        print("Character saved successfully")
    except Exception as e:
        print(f"Save error: {e}")
    
    # Test loading
    try:
        loaded = load_character("TestHero")
        print(f"Loaded: {loaded['name']}")
    except CharacterNotFoundError:
        print("Character not found")
    except SaveFileCorruptedError:
        print("Save file corrupted")
    except InvalidSaveDataError:
        print("Invalid save data")
            - experience, gold, inventory, active_quests, completed_quests
    
    Raises: InvalidCharacterClassError if class is not valid
    """
    # TODO: Implement character creation
    # Validate character_class first
    # Example base stats:
    # Warrior: health=120, strength=15, magic=5
    # Mage: health=80, strength=8, magic=20
    # Rogue: health=90, strength=12, magic=10
    # Cleric: health=100, strength=10, magic=15
    
    base_stats = {
        'Warrior': {'health': 120, 'strength': 15, 'magic': 5},
        'Mage': {'health': 80, 'strength': 8, 'magic': 20},
        'Rogue': {'health': 90, 'strength': 12, 'magic': 10},
        'Cleric': {'health': 100, 'strength': 10, 'magic': 15}
    }
    if character_class not in base_stats:
        raise InvalidCharacterClassError(f"Invalid class: {character_class}")
    # All characters start with:
    # - level=1, experience=0, gold=100
    # - inventory=[], active_quests=[], completed_quests=[]

    character_data = {
        'name': name,
        'class': character_class,
        'level': 1,
        'health': base_stats[character_class]['health'],
        'max_health': base_stats[character_class]['health'],
        'strength': base_stats[character_class]['strength'],
        'magic': base_stats[character_class]['magic'],
        'experience': 0,
        'gold': 100,
        'inventory': [],
        'active_quests': [],
        'completed_quests': []
    }

    return character_data

def save_character(character, save_directory="data/save_games"):
    """
    Save character to file
    
    Filename format: {character_name}_save.txt
    
    File format:
    NAME: character_name
    CLASS: class_name
    LEVEL: 1
    HEALTH: 120
    MAX_HEALTH: 120
    STRENGTH: 15
    MAGIC: 5
    EXPERIENCE: 0
    GOLD: 100
    INVENTORY: item1,item2,item3
    ACTIVE_QUESTS: quest1,quest2
    COMPLETED_QUESTS: quest1,quest2
    
    Returns: True if successful
    Raises: PermissionError, IOError (let them propagate or handle)
    """
    # TODO: Implement save functionality
    # Create save_directory if it doesn't exist
    # Handle any file I/O errors appropriately
    # Lists should be saved as comma-separated values
    try:
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        filename = os.path.join(save_directory, f"{character['name']}_save.txt")
        with open(filename, 'w') as file:
            file.write(f"NAME: {character['name']}\n")
            file.write(f"CLASS: {character['class']}\n")
            file.write(f"LEVEL: {character['level']}\n")
            file.write(f"HEALTH: {character['health']}\n")
            file.write(f"MAX_HEALTH: {character['max_health']}\n")
            file.write(f"STRENGTH: {character['strength']}\n")
            file.write(f"MAGIC: {character['magic']}\n")
            file.write(f"EXPERIENCE: {character['experience']}\n")
            file.write(f"GOLD: {character['gold']}\n")
            file.write(f"INVENTORY: {','.join(character['inventory'])}\n")
            file.write(f"ACTIVE_QUESTS: {','.join(character['active_quests'])}\n")
            file.write(f"COMPLETED_QUESTS: {','.join(character['completed_quests'])}\n")

    except (PermissionError, IOError) as e:
        # Handle file I/O errors
        print(f"Error saving character: {e}")
        return False

    return True

def load_character(character_name, save_directory="data/save_games"):
    """
    Load character from save file
    
    Args:
        character_name: Name of character to load
        save_directory: Directory containing save files
    
    Returns: Character dictionary
    Raises: 
        CharacterNotFoundError if save file doesn't exist
        SaveFileCorruptedError if file exists but can't be read
        InvalidSaveDataError if data format is wrong
    """
    # TODO: Implement load functionality
    filename = os.path.join(save_directory, f"{character_name}_save.txt")
    if not os.path.exists(filename):
        raise CharacterNotFoundError(f"Character '{character_name}' not found.")    # Check if file exists → CharacterNotFoundError
    character = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ', 1)
                character[key.lower()] = value
    except Exception as e:
        raise SaveFileCorruptedError(f"Save file for '{character_name}' is corrupted.") from e # Try to read file → SaveFileCorruptedError

    if not all(key in character for key in ['name', 'class', 'level', 'health', 'max_health', 'strength', 'magic', 'experience', 'gold', 'inventory', 'active_quests', 'completed_quests']):
        raise InvalidSaveDataError(f"Save file for '{character_name}' is invalid.") # Validate data format → InvalidSaveDataError

    # Parse comma-separated lists back into Python lists
    character['inventory'] = character['inventory'].split(',') if character['inventory'] else []
    character['active_quests'] = character['active_quests'].split(',') if character['active_quests'] else []
    character['completed_quests'] = character['completed_quests'].split(',') if character['completed_quests'] else []

    return character    

def list_saved_characters(save_directory="data/save_games"):
    """
    Get list of all saved character names
    
    Returns: List of character names (without _save.txt extension)
    """
    # TODO: Implement this function
    # Return empty list if directory doesn't exist
    if not os.path.exists(save_directory):
        return []
    character_names = []
    for filename in os.listdir(save_directory):
        if filename.endswith("_save.txt"):
            character_name = filename[:-9]  # Remove '_save.txt'
            character_names.append(character_name)
    # Extract character names from filenames

    return character_names

def delete_character(character_name, save_directory="data/save_games"):
    """
    Delete a character's save file
    
    Returns: True if deleted successfully
    Raises: CharacterNotFoundError if character doesn't exist
    """
    # TODO: Implement character deletion
    # Verify file exists before attempting deletion
    filename = os.path.join(save_directory, f"{character_name}_save.txt")
    if not os.path.exists(filename):
        raise CharacterNotFoundError(f"Character '{character_name}' not found.")
    os.remove(filename)
    return True

# ============================================================================
# CHARACTER OPERATIONS
# ============================================================================

def gain_experience(character, xp_amount):
    """
    Add experience to character and handle level ups
    
    Level up formula: level_up_xp = current_level * 100
    Example when leveling up:
    - Increase level by 1
    - Increase max_health by 10
    - Increase strength by 2
    - Increase magic by 2
    - Restore health to max_health
    
    Raises: CharacterDeadError if character health is 0
    """
    # TODO: Implement experience gain and leveling
    if is_character_dead(character):
        raise CharacterDeadError(f"Character '{character['name']}' is dead and cannot gain experience.")
    # Check if character is dead first
    # Add experience
    character['experience'] += xp_amount

    # Check for level up (can level up multiple times)
    while character['experience'] >= character['level'] * 100:
        character['level'] += 1
        character['max_health'] += 10
        character['strength'] += 2
        character['magic'] += 2
        character['health'] = character['max_health']
        character['experience'] -= character['level'] * 100

    return character

def add_gold(character, amount):
    """
    Add gold to character's inventory
    
    Args:
        character: Character dictionary
        amount: Amount of gold to add (can be negative for spending)
    
    Returns: New gold total
    Raises: ValueError if result would be negative
    """
    # TODO: Implement gold management
    # Check that result won't be negative
    # Update character's gold

    new_gold = character['gold'] + amount
    if new_gold < 0:
        raise ValueError("Gold amount cannot be negative.")
    character['gold'] = new_gold
    return character['gold']

def heal_character(character, amount):
    """
    Heal character by specified amount
    
    Health cannot exceed max_health
    
    Returns: Actual amount healed
    """
    # TODO: Implement healing
    # Calculate actual healing (don't exceed max_health)
    # Update character health
    if is_character_dead(character):
        raise CharacterDeadError(f"Character '{character['name']}' is dead and cannot be healed.")
    character['health'] += amount
    if character['health'] > character['max_health']:
        character['health'] = character['max_health']
    return amount

def is_character_dead(character):
    """
    Check if character's health is 0 or below
    
    Returns: True if dead, False if alive
    """
    # TODO: Implement death check
    return character['health'] <= 0


def revive_character(character):
    """
    Revive a dead character with 50% health
    
    Returns: True if revived
    """
    # TODO: Implement revival
    # Restore health to half of max_health
    if not is_character_dead(character):
        return False
    character['health'] = character['max_health'] // 2
    return True

# ============================================================================
# VALIDATION
# ============================================================================

def validate_character_data(character):
    """
    Validate that character dictionary has all required fields
    
    Required fields: name, class, level, health, max_health, 
                    strength, magic, experience, gold, inventory,
                    active_quests, completed_quests
    
    Returns: True if valid
    Raises: InvalidSaveDataError if missing fields or invalid types
    """
    # TODO: Implement validation
    # Check all required keys exist
    # Check that numeric values are numbers
    # Check that lists are actually lists
    required_fields = [
        'name', 'class', 'level', 'health', 'max_health',
        'strength', 'magic', 'experience', 'gold',
        'inventory', 'active_quests', 'completed_quests'
    ]
    for field in required_fields:
        if field not in character:
            raise InvalidSaveDataError(f"Missing field: {field}")
    if not isinstance(character['level'], int) or not isinstance(character['health'], int) or not isinstance(character['max_health'], int) or not isinstance(character['strength'], int) or not isinstance(character['magic'], int) or not isinstance(character['experience'], int) or not isinstance(character['gold'], int):
        raise InvalidSaveDataError("Numeric fields must be integers.")
    if not isinstance(character['inventory'], list) or not isinstance(character['active_quests'], list) or not isinstance(character['completed_quests'], list):
        raise InvalidSaveDataError("Inventory and quests must be lists.")
    return True

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER MANAGER TEST ===")
    
    # Test character creation
    try:
        char = create_character("TestHero", "Warrior")
        print(f"Created: {char['name']} the {char['class']}")
        print(f"Stats: HP={char['health']}, STR={char['strength']}, MAG={char['magic']}")
    except InvalidCharacterClassError as e:
        print(f"Invalid class: {e}")
    
    # Test saving
    try:
        save_character(char)
        print("Character saved successfully")
    except Exception as e:
        print(f"Save error: {e}")
    
    # Test loading
    try:
        loaded = load_character("TestHero")
        print(f"Loaded: {loaded['name']}")
    except CharacterNotFoundError:
        print("Character not found")
    except SaveFileCorruptedError:
        print("Save file corrupted")
    except InvalidSaveDataError:
        print("Invalid save data")
