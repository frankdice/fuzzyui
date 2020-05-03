#!/usr/bin/env python
from fuzzyui import fuzzyui

items = ["baseball", "football", "soccer", "programming", "cooking", "sleeping"]
initial_search = ''

fui = fuzzyui()
found = fui.find(items)
print(found)
