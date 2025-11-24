"""
COMP 163 - Project 3: Quest Chronicles
Custom Exception Definitions

This module defines all custom exceptions used throughout the game.
"""

# ============================================================================
# BASE GAME EXCEPTIONS
# ============================================================================

class GameError(Exception):
    """Base exception for all game-related errors"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class DataError(GameError):
    """Base exception for data-related errors"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class CharacterError(GameError):
    """Base exception for character-related errors"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class CombatError(GameError):
    """Base exception for combat-related errors"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class QuestError(GameError):
    """Base exception for quest-related errors"""
    def __init__(self, message):
        super().__init__(message)
        GameError.message = message

class InventoryError(GameError):
    """Base exception for inventory-related errors"""
    def __init__(self, message):
        super().__init__(message)
        GameError.message = message

# ============================================================================
# SPECIFIC EXCEPTIONS
# ============================================================================

# Data Loading Exceptions
class InvalidDataFormatError(DataError):
    """Raised when data file has incorrect format"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class MissingDataFileError(DataError):
    """Raised when required data file is not found"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class CorruptedDataError(DataError):
    """Raised when data file is corrupted or unreadable"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Character Exceptions
class InvalidCharacterClassError(CharacterError):
    """Raised when an invalid character class is specified"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class CharacterNotFoundError(CharacterError):
    """Raised when trying to load a character that doesn't exist"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class CharacterDeadError(CharacterError):
    """Raised when trying to perform actions with a dead character"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InsufficientLevelError(CharacterError):
    """Raised when character level is too low for an action"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Combat Exceptions
class InvalidTargetError(CombatError):
    """Raised when trying to target an invalid enemy"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class CombatNotActiveError(CombatError):
    """Raised when trying to perform combat actions outside of battle"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class AbilityOnCooldownError(CombatError):
    """Raised when trying to use an ability that's on cooldown"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Quest Exceptions
class QuestNotFoundError(QuestError):
    """Raised when trying to access a quest that doesn't exist"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class QuestRequirementsNotMetError(QuestError):
    """Raised when trying to start a quest without meeting requirements"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class QuestAlreadyCompletedError(QuestError):
    """Raised when trying to accept an already completed quest"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class QuestNotActiveError(QuestError):
    """Raised when trying to complete a quest that isn't active"""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Inventory Exceptions
class InventoryFullError(InventoryError):
    """Raised when trying to add items to a full inventory"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class ItemNotFoundError(InventoryError):
    """Raised when trying to use an item that doesn't exist"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InsufficientResourcesError(InventoryError):
    """Raised when player doesn't have enough gold or items"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InvalidItemTypeError(InventoryError):
    """Raised when item type is not recognized"""
    
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Save/Load Exceptions
class SaveFileCorruptedError(GameError):
    """Raised when save file cannot be loaded due to corruption"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message
    
class InvalidSaveDataError(GameError):
    """Raised when save file contains invalid data"""
    def __init__(self, message):
        super().__init__(message)
        self.message = message