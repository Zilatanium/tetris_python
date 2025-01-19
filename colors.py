class Colors:
    dark_gray = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 243, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    pink = (255, 105, 180)
    white = (255,255,255)
    dark_blue = (44,44,127)
    light_blue = (59,85,162)
    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_gray, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.pink, cls.white, cls.dark_blue, cls.light_blue]

