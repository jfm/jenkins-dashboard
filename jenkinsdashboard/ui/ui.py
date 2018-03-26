from termcolor import colored


class Row:
    def __init__(self, cells, width):
        self.cells = cells
        self.columns = len(cells)
        self.cell_width = int(width / self.columns)

    def render(self):
        self.rendered_value = ''
        for cell in self.cells:
            self.rendered_value = self.rendered_value + \
                cell.render(self.cell_width)
        print(self.rendered_value)


class Cell:
    def __init__(self, value, **kwargs):
        self.value = value
        if 'right_aligned' in kwargs:
            self.right_aligned = kwargs['right_aligned']
        else:
            self.right_aligned = False

        if 'is_header' in kwargs:
            self.is_header = kwargs['is_header']
        else:
            self.is_header = False

        if 'color' in kwargs:
            self.color = kwargs['color']
        else:
            self.color = 'white'

        if 'blink' in kwargs:
            self.blink = kwargs['blink']
        else:
            self.blink = False

    def render(self, width):
        value_length = len(self.value)
        if value_length < width:
            if self.right_aligned:
                self.rendered_value = self.left_padding(self.value, width)
            else:
                self.rendered_value = self.right_padding(self.value, width)
        else:
            self.rendered_value = self.value[:width]

        return self.colorize(
            self.rendered_value,
            self.is_header,
            self.blink,
            self.color
        )

    def left_padding(self, value, width):
        spaces = width - len(value)
        return (" " * spaces) + value

    def right_padding(self, value, width):
        spaces = width - len(value)
        return value + (" " * spaces)

    def colorize(self, text, is_header, blink, color):
        if is_header:
            return colored(text, color, attrs=['bold'])
        else:
            if blink:
                return colored(text, color, attrs=['blink'])
            else:
                return colored(text, color)
