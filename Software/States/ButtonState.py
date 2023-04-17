from enum import Enum
from functools import partial

class ButtonState(Enum):
    INACTIVE = "RECORD"
    PLAYING = "STOP"
    FINALIZED = "RETRY"