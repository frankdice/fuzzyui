# fuzzyui

`fuzzyui` is a python module that sets out to recreate some of the awesomeness that is [fzf in unix](https://github.com/junegunn/fzf).

The module itself is simple, pass in a list (and an optional initial search string), and you'll get a fullscreen interface in your terminal to help pick exactly which item you want (with text input to filter).

### Example
```
#!/usr/bin/env python
from fuzzyui import fuzzyui

items = ["baseball", "football", "soccer", "programming", "cooking", "sleeping"]
initial_search = ''

fui = fuzzyui()
found = fui.find(items)
print(found)
```

It also accepts text input within the screen takeover, updating the items list and probability order automatically. Hit enter, and it'll return the selected value.
