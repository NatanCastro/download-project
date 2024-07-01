import tkinter as tk


class ColoredListbox(tk.Listbox):
    def __init__(self, *args, **kwargs):
        tk.Listbox.__init__(self, *args, **kwargs)
        self.color_map = {}

    def set_item_color(self, index, color):
        self.color_map[index] = color
        self.itemconfig(index, {'bg': color, 'fg': "#000000"})

    def delete(self, first, last=None):
        first = int(first)
        if last is None:
            last = first
        elif last == tk.END:
            last = self.size() - 1
        else:
            last = int(last)
        for i in range(first, last + 1):
            if i in self.color_map:
                del self.color_map[i]
            tk.Listbox.delete(self, i)

    def insert(self, index, *elements):
        tk.Listbox.insert(self, index, *elements)
        for element in elements:
            index = tk.Listbox.index(self, tk.END) - 1
            self.itemconfig(
                index, {'bg': self.color_map.get(index, self.cget("bg"))})
