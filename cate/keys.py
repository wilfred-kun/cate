import pygame.locals
from collections import namedtuple

_keys = [attr for attr in dir(pygame.locals) if attr.startswith("K_")]

class Keys:
    def __init__(self):
        for _key in _keys:
            setattr(self, _key, eval(f"pygame.locals.{_key}"))
            
Keys = Keys()
