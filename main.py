import arcade

game_name = "peak"

game_width = 800
console_width = 300

height = 600

width = game_width + console_width

circle_pos = 400
circle_pos2 = 300
speed = 5


class Game(arcade.Window):

    def __init__(self):
        super().__init__(width, height, game_name)

        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.velocity_y = 0
        self.gravity = 0.5
        self.jump = 10
        self.max_jump = 2
        self.jump_count = 0

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            if self.jump_count < self.max_jump:
                self.velocity_y = self.jump
                self.jump_count += 1
            else:
                None

        if key == arcade.key.DOWN:
            self.down = True

        if key == arcade.key.LEFT:
            self.left = True

        if key == arcade.key.RIGHT:
            self.right = True

    def on_key_release(self, key, modifiers):

       

        if key == arcade.key.DOWN:
            self.down = False

        if key == arcade.key.LEFT:
            self.left = False

        if key == arcade.key.RIGHT:
            self.right = False

    def on_update(self, delta_time):
        global circle_pos, circle_pos2

        self.velocity_y -= self.gravity
        circle_pos2 += self.velocity_y

        if circle_pos2 - 50 < 100:
            circle_pos2 = 150
            self.velocity_y = 0
            self.jump_count = 0


        if self.down and circle_pos2 - 50 > 100:
            circle_pos2 -= speed

        if self.left and circle_pos -50 > 0:
            circle_pos -= speed

        if self.right:
            circle_pos += speed
    def ground(self):
        arcade.draw_lbwh_rectangle_filled(
            0, 0, 800, 100, (128,106,0)
        )
    def console(self):
        arcade.draw_lbwh_rectangle_filled(
            game_width,
            0,
            console_width,
            height,
            arcade.color.DARK_BROWN
        )

        arcade.draw_text(
            "DEBUG CONSOLE",
            game_width + 20,
            height - 40,
            arcade.color.WHITE,
            18
        )

        arcade.draw_text(
            f"X: {circle_pos}",
            game_width + 20,
            height - 80,
            arcade.color.WHITE,
            14
        )

        arcade.draw_text(
            f"Y: {circle_pos2}",
            game_width + 20,
            height - 105,
            arcade.color.WHITE,
            14
        )
        arcade.draw_text(
            f"jump count: {self.jump_count}",
            game_width + 20,
            height - 130,
            arcade.color.WHITE,
            14
        )

        arcade.draw_text(
            f"Velocity: {self.velocity_y:.2f}",
            game_width + 20,
            height - 155,
            arcade.color.WHITE,
            14
        )

    def on_draw(self):
        self.clear()
        self.ground()
        self.console()
        arcade.draw_circle_filled(
            circle_pos,
            circle_pos2,
            50,
            arcade.color.RED
        )
    


game = Game()
arcade.run()