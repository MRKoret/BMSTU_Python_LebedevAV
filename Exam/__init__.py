# Делаем функции доступными на уровне пакета
from .Exs_13 import longest_word

# Указываем, что экспортируется при 'from text_utils import *'
__all__ = ['longest_word']