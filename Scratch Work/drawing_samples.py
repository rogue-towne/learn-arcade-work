import arcade
arcade.open_window(600, 600, "Drawing Example")

#set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
#Get ready to draw
arcade.start_render()
#drawing code

# Draws a Big Rectangle
#lrtb = start from left to right then top to bottom
#left of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

#Draws a tree trunk
#Center pixels: 100,320
#Width pixels: 20
#height pixels: 60
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

#finish drawing
arcade.finish_render()
#keeps the window open
arcade.run()