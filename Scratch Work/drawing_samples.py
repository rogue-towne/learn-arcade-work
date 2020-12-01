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
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.LIGHT_GREEN)

#Draws a tree trunk
#center(x,y),width,height,color
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

#Tree with circle
#center(x,y), radius, color
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

#Tree with ellipse
#center(x,y), radius, color
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 360, 60, 80, arcade.csscolor.DARK_GREEN)

#Tree with arc
#center(x,y),width,height, color, start angle, end angle,
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 325, 60, 100, arcade.csscolor.DARK_GREEN,0, 180)

#Tree with triangle
# 3 points:(x,y), (x,y), (x,y), color
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

#Tree with polygon
# 5 points
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360), 
                            (470, 320),
                            (530, 320),
                            (520, 360)), arcade.csscolor.DARK_GREEN)

#draw sun
arcade.draw_circle_filled(500,550,40, arcade.color.YELLOW)
#lines
#starting point(x,x), ending point(x,y), color, line width
#horizontal
arcade.draw_line(400, 550, 600, 550, arcade.color.YELLOW, 3)
#verical
arcade.draw_line(500, 450, 500, 600, arcade.color.YELLOW, 3)
#diagonal
arcade.draw_line(450, 600, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(450, 500, 550, 600, arcade.color.YELLOW, 3)



#finish drawing
arcade.finish_render()
#keeps the window open
arcade.run()