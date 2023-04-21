from enum import Enum

class ButtonState(Enum): # Enumeration for Button States
    INACTIVE = "RECORD"
    PLAYING = "STOP"
    FINALIZED = "RETRY"