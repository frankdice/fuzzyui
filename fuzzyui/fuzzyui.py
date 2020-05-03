#!/usr/bin/env python
import sys
import re
import functools
from blessed import Terminal
from fuzzywuzzy import process as fuzzyprocess

class fuzzyui:

  def __init__(self, items = []):
    self.items = items
    self.term = None
    self.echo = functools.partial(print, end='', flush=True)
    self.fuzzysorted = []
    #echo(u'')
    return

  def _idx_bounds(self, idx):
    if idx < len(self.fuzzysorted) and idx >= 0:
      return True
    return False

  def _render(self, idx, input_string):
      self.fuzzysorted = fuzzyprocess.extract(input_string, self.items, limit=len(self.items))
      #Clear screen
      self.echo(self.term.home + self.term.clear)
      # Set bottom height for list to be displayed
      #   idx is set to 0 for the bottom item in find(), incremented + when going up
      #   which keeps this functional and reasonably sanely implemented
      self.echo(self.term.move_xy(0, self.term.height - 3))
      
      # fuzzysorted reutrns an array of tuples: [('one', 45), ('three', 45), ('two', 0)]
      _displayed_items=0
      for index, item in enumerate(self.fuzzysorted):
        #If there's no input_string filter, output everything
        if item[1] >= 30 or input_string == "":
          _displayed_items += 1
          if index == idx:
            self.echo(self.term.on_grey30("> {0}".format(item[0])))
          else:
            self.echo(self.term.on_grey30(" ") + " {0}".format(item[0]))
          self.echo(self.term.move_x(0) + self.term.move_up(1))
      
      #Count of how many displayed vs total passed in
      self.echo(self.term.move_xy(0, self.term.height - 2) + "{0}/{1}".format(_displayed_items, len(self.items)))
      #Bottom display prompt
      self.echo(self.term.move_xy(0, self.term.height - 1) + "> {0}\u2588".format(input_string))


  def find(self, items, searchtext=""):
    self.term = Terminal()
    self.items = items
    with self.term.fullscreen(), self.term.hidden_cursor(), self.term.cbreak():
      idx = 0
      input_string = searchtext
      selected_value = None
      dirty = True
      inp = None
      while True:
        inp=self.term.inkey(timeout=.05)

        if dirty:
          self._render(idx, input_string)

        if inp.code == self.term.KEY_DOWN:
          if self._idx_bounds(idx - 1):
            idx -= 1
            dirty = True
        elif inp.code == self.term.KEY_UP:
          if self._idx_bounds(idx + 1):
            idx += 1
            dirty = True
        elif inp.code == self.term.KEY_ESCAPE:
          selected_value = None
          break
        elif inp.code == self.term.KEY_ENTER:
          selected_value = self.fuzzysorted[idx][0]
          break
        elif re.match(r'^[a-zA-z-_. ]{1}$', inp):
          dirty = True
          input_string += inp
          idx = 0
        elif inp.code == self.term.KEY_BACKSPACE:
          dirty = True
          input_string = input_string[:-1]
          idx = 0
        else:
          dirty = False

    self.term.exit_fullscreen()
    self.term = None
    return selected_value


if __name__ == "__main__":
    items = ['one', 'two', 'three']
    fzf = fuzzyui()
    return_value = fzf.find(items, 'tw')
    print(return_value)
