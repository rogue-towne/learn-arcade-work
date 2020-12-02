import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# def main():
#     function open window 
#     arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "DRAWING EXAMPLE")
    
#     #Create Window object to open window
#     window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    
#     arcade.run()

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
    
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
    
    def update(self):
        """ Code to control the ball's movement. """
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height,title)
        #set background color
        arcade.set_background_color(arcade.color.ASH_GREY)
        
        self.ball_list = []
        
        #Create balls
        self.ball = Ball(50, 50, 3, 3, 15, arcade.color.AUBURN)
        self.ball_list.append(self.ball)

        self.ball = Ball(100, 50, 3, 3, 15, arcade.color.DARK_IMPERIAL_BLUE)
        self.ball_list.append(self.ball)

        self.ball = Ball(150, 50, 3, 3, 15, arcade.color.GUPPIE_GREEN)
        self.ball_list.append(self.ball)


    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            ball.draw()
    
    def update(self, delta_time):
        for ball in self.ball_list:
            ball.update()

def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()

main()

