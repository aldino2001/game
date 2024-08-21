import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu du Serpent")
        
        # Configuration du canvas
        self.canvas = tk.Canvas(root, bg="black", width=400, height=400)
        self.canvas.pack()

        # Ajouter les boutons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_game)
        self.start_button.pack(side="left")

        self.restart_button = tk.Button(self.button_frame, text="Restart", command=self.restart_game)
        self.restart_button.pack(side="left")

        # Ajouter le menu de niveau
        self.difficulty = tk.StringVar(value="Medium")
        self.difficulty_menu = tk.OptionMenu(self.button_frame, self.difficulty, "Low", "Medium", "Hard")
        self.difficulty_menu.pack(side="left")

        self.speed_map = {
            "Low": 200,
            "Medium": 100,
            "Hard": 50
        }

        self.reset_game()

    def reset_game(self):
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = self.set_new_food_position()
        self.direction = "Right"
        self.score = 0
        self.game_over = False

        self.canvas.delete("all")
        self.create_objects()
        self.root.bind("<KeyPress>", self.change_direction)

    def start_game(self):
        if not self.game_over:
            self.update_snake()

    def restart_game(self):
        self.reset_game()
        self.start_game()

    def create_objects(self):
        self.canvas.create_text(35, 10, text=f"Score: {self.score}", tag="score", fill="white", font=("TkDefaultFont", 14))
        self.canvas.create_rectangle(*self.food_position, *self.add_tuple(self.food_position, (20, 20)), fill="red", tag="food")
        for x_position, y_position in self.snake_positions:
            self.canvas.create_rectangle(x_position, y_position, x_position + 20, y_position + 20, fill="green", tag="snake")

    def update_snake(self):
        if self.check_collisions():
            self.game_over = True
            self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2, text=f"Game Over\nScore: {self.score}", fill="red", font=("TkDefaultFont", 24))
            return
        
        self.move_snake()
        
        if self.snake_positions[0] == self.food_position:
            self.score += 1
            self.canvas.delete("food")
            self.food_position = self.set_new_food_position()
            self.canvas.create_rectangle(*self.food_position, *self.add_tuple(self.food_position, (20, 20)), fill="red", tag="food")
        else:
            self.snake_positions.pop()
        
        self.canvas.delete("snake")
        for x_position, y_position in self.snake_positions:
            self.canvas.create_rectangle(x_position, y_position, x_position + 20, y_position + 20, fill="green", tag="snake")
        
        self.canvas.itemconfig("score", text=f"Score: {self.score}")
        
        if not self.game_over:
            self.root.after(self.speed_map[self.difficulty.get()], self.update_snake)

    def move_snake(self):
        head_x_position, head_y_position = self.snake_positions[0]
        new_head_position = {
            "Left": (head_x_position - 20, head_y_position),
            "Right": (head_x_position + 20, head_y_position),
            "Up": (head_x_position, head_y_position - 20),
            "Down": (head_x_position, head_y_position + 20)
        }[self.direction]
        self.snake_positions = [new_head_position] + self.snake_positions

    def change_direction(self, event):
        new_direction = event.keysym
        all_directions = ["Left", "Right", "Up", "Down"]
        opposites = ({"Left", "Right"}, {"Up", "Down"})
        
        if new_direction in all_directions:
            if {new_direction, self.direction} not in opposites:
                self.direction = new_direction

    def check_collisions(self):
        head_x_position, head_y_position = self.snake_positions[0]
        return (
            head_x_position in (0, 400) or
            head_y_position in (0, 400) or
            (head_x_position, head_y_position) in self.snake_positions[1:]
        )

    def set_new_food_position(self):
        while True:
            x_position = random.randint(1, 19) * 20
            y_position = random.randint(1, 19) * 20
            food_position = (x_position, y_position)
            if food_position not in self.snake_positions:
                return food_position

    @staticmethod
    def add_tuple(tup1, tup2):
        return tuple(map(sum, zip(tup1, tup2)))


if __name__ == "__main__":
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()
