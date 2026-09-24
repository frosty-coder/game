import arcade

game_name = "peak"
game_width = 800
console_width = 300

height = 600
width = game_width + console_width

circle_pos_x = 400
circle_pos_y = 300
speed = 5
score = 0
score_rate = 0.2


class Platform:
    def __init__(self, x, y, width=80, height=10):
        self.x = x
        self.speed = 0.5
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        arcade.draw_lbwh_rectangle_filled(
            self.x,
            self.y,
            self.width,
            self.height,
            (130, 128, 18)
        )

    def move_left(self):
        self.x -= self.speed

    def collision(self, player_x, player_y, player_radius, player_velocity):
        if (
            player_x + player_radius > self.x
            and player_x - player_radius < self.x + self.width
            and player_y - player_radius <= self.y
            and player_y - player_radius >= self.y - self.height
            and player_velocity <= 0
            
        ):
            return True

        return False


class Game(arcade.Window):

    def __init__(self):
        super().__init__(width, height, game_name)

        self.circle_radius = 20

        self.up = False
        self.down = False
        self.left = False
        self.right = False

        self.velocity_y = 0
        self.gravity = 0.5
        self.jump = 10
        self.max_jump = 2
        self.jump_count = 0
        self.poly_x = 140
        self.paused = False

        self.platforms = [
            Platform(150, 250),
            Platform(300, 400),
            Platform(230, 330)
        ]

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            if self.jump_count < self.max_jump:
                self.velocity_y = self.jump
                self.jump_count += 1

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
        global circle_pos_x, circle_pos_y

        if self.paused:
            return

        for i in [0, 1, 2]:
            self.platforms[i].move_left()

        self.velocity_y -= self.gravity
        circle_pos_y += self.velocity_y

        if circle_pos_y - self.circle_radius < 100:
            circle_pos_y = 100 + self.circle_radius
            self.velocity_y = 0
            self.jump_count = 0

        if self.down and circle_pos_y - self.circle_radius > 100:
            circle_pos_y -= speed

        if self.left and circle_pos_x - self.circle_radius > 0:
            circle_pos_x -= speed

        if self.right and circle_pos_x + self.circle_radius < 800:
            circle_pos_x += speed

        for platform in self.platforms:
            if platform.collision(
                circle_pos_x,
                circle_pos_y,
                self.circle_radius,
                self.velocity_y,
                
            ):
                circle_pos_y = platform.y + self.circle_radius
                if circle_pos_x > 19.5:
                    circle_pos_x -= platform.speed
                
                self.velocity_y = 0
                self.jump_count = 0

    def ground(self):
        arcade.draw_lbwh_rectangle_filled(
            0,
            0,
            800,
            100,
            (128, 106, 0)
        )
    
    def buttons(self):
        

        """arcade.draw_lbwh_rectangle_filled(
            140,
            height - 60,
            50,
            40,
            (175, 174, 184)
        )"""
        
        arcade.draw_polygon_filled(
            [
            (self.poly_x, height - 40),
            (self.poly_x + 12, height - 60),
            (self.poly_x + 38, height - 60),
            (self.poly_x + 50, height - 40),
            (self.poly_x + 38, height - 20),
            (self.poly_x + 12, height - 20)
            ],
            arcade.color.ALLOY_ORANGE)
        
        global side2
        side2 = 20
        arcade.draw_triangle_filled(
            
            45,
            height - side2,
            45,
            height - side2*3,
            90,
            height - side2*2,
            (51, 54, 2)
        )

        

    def on_mouse_press(self, x, y, button, modifiers):

        if self.paused:

            if 300 <= x <= 500 and 350 <= y <= 400:
                self.paused = False

            if 300 <= x <= 500 and 280 <= y <= 330:
                self.restart()

            return

        if 45 <= x <= 90 and height - (side2*3) <= y <= height - 20:
            self.paused = True

        if 140 <= x <= 190 and height - (side2*3) <= y <= height - 20:
            self.restart()

    def restart(self):
        global circle_pos_x, circle_pos_y

        circle_pos_x = 400
        circle_pos_y = 300

        self.velocity_y = 0
        self.jump_count = 0

        self.down = False
        self.left = False
        self.right = False

        self.paused = False

        self.platforms = [
            Platform(150, 250),
            Platform(300, 400),
            Platform(230, 330)
        ]

    def pause_screen(self):

        arcade.draw_lbwh_rectangle_filled(
            0,
            0,
            game_width,
            height,
            arcade.color.BLACK
        )

        arcade.draw_text(
            "GAME PAUSED",
            (game_width - console_width)/ 2,
            450,
            arcade.color.WHITE,
            30
        )

        arcade.draw_lbwh_rectangle_filled(
            300,
            350,
            200,
            50,
            arcade.color.BLUE
        )

        arcade.draw_text(
            "RESUME",
            350,
            365,
            arcade.color.WHITE,
            18
        )

        arcade.draw_lbwh_rectangle_filled(
            300,
            280,
            200,
            50,
            arcade.color.RED
        )

        arcade.draw_text(
            "RESTART",
            345,
            295,
            arcade.color.WHITE,
            18
        )
    def scores():
        None

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
            f"X: {circle_pos_x}",
            game_width + 20,
            height - 80,
            arcade.color.WHITE,
            14
        )

        arcade.draw_text(
            f"Y: {circle_pos_y}",
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

        if self.paused:
            self.console()
            self.pause_screen()
            return

        self.ground()
        self.console()
        self.buttons()

        for platform in self.platforms:
            platform.draw()

        arcade.draw_circle_filled(
            circle_pos_x,
            circle_pos_y,
            self.circle_radius,
            arcade.color.RED
        )


game = Game()
arcade.run()
