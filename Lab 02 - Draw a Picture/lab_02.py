import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Draw the ground
def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_snowman(x,y):
    # Snow
    arcade.draw_circle_filled(300 + x, 200 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 280 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 340 + y, 40, arcade.color.WHITE)
    # Eyes
    arcade.draw_circle_filled(285 + x, 350 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315 + x, 350 + y, 5, arcade.color.BLACK)
    # Nose
    arcade.draw_triangle_filled(300+ x, 335 + y, 300+ x, 345 + y, 330+ x, 335 + y, arcade.csscolor.ORANGE)

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_snowman(50,50)
    draw_snowman(on_draw.snow_person1_x, 50)

    # Negative numbers move left. Larger numbers move faster.
    on_draw.snow_person1_x -= 1

on_draw.snow_person1_x = 50

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
   
    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()