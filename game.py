from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.level = 0

    def update_score(self, lines_cleared):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 200
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 1000

        self.update_level()

    def update_level(self):
        score_thresholds = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000]
        for i, threshold in enumerate(score_thresholds):
            if self.score <= threshold:
                self.level = i
                break
        else:
            self.level = 9

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def drop_down(self):
        while True:
            if self.block_inside() == False or self.block_fits() == False:
                self.current_block.move(-1, 0)
                break
            self.current_block.move(1, 0)

    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)
            
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared)
        if self.block_fits() == False:
            self.game_over = True

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True
    
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.level = 0
        self.score = 0

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        if self.next_block.id == 1:
            self.next_block.draw(screen, 300, 420)
        elif self.next_block.id == 2:
            self.next_block.draw(screen, 300, 420)
        elif self.next_block.id == 5:
            self.next_block.draw(screen, 300, 420)
        elif self.next_block.id == 6:
            self.next_block.draw(screen, 295, 420)
        elif self.next_block.id == 7:
            self.next_block.draw(screen, 305, 420)
        else:
            self.next_block.draw(screen, 280, 420)
