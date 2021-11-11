'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
#DRAWING OF CROSSY ROAD GAME
import arcade
arcade.open_window(600, 600, "Landen Thompson")
arcade.set_background_color((0, 255, 0))
arcade.start_render()
for x in range(200, 500, 100): #roads start
    arcade.draw_line(x, 600, x, 0, (69, 69, 69), 70)
    for y in range(25, 575, 50):
        arcade.draw_line(x, y, x, y+25, (255, 255, 255), 20) #roads end
arcade.draw_rectangle_filled(50, 300, 30, 30, (240, 240, 240)) #chicken start
arcade.draw_lrtb_rectangle_filled(60, 80, 335, 315, (240, 240, 240))
arcade.draw_lrtb_rectangle_filled(80, 95, 325, 315, (240, 90, 10))
arcade.draw_point(70, 325, (0, 0, 0), 4)
arcade.draw_line(40, 285, 40, 275, (0, 0, 0))
arcade.draw_line(60, 285, 60, 275, (0, 0, 0))
arcade.draw_lrtb_rectangle_filled(30, 35, 315, 310, (240, 240, 240)) #chicken end
for z in range(100, 550, 100): #cars start
    arcade.draw_lrtb_rectangle_filled(180, 220, z, z-40, (0, 60, 255))
    arcade.draw_lrtb_rectangle_filled(280, 320, z+50, z+10, (0, 150, 130))
    arcade.draw_lrtb_rectangle_filled(380, 420, z + 75, z + 35, (250, 150, 130))
    arcade.draw_lrtb_rectangle_filled(290, 310, z + 40, z + 20, (50, 50, 50))
    arcade.draw_lrtb_rectangle_filled(390, 410, z + 65, z + 45, (50, 50, 50))
    arcade.draw_lrtb_rectangle_filled(190, 210, z-10, z-30, (50, 50, 50))
for w in range(100, 550, 100):
    arcade.draw_line(180, w+5, 180, w-5, (50, 50, 50), 3) #blue car start
    arcade.draw_line(180, w -45, 180, w-35, (50, 50, 50), 3)
    arcade.draw_line(220, w + 5, 220, w - 5, (50, 50, 50), 3)
    arcade.draw_line(220, w - 45, 220, w - 35, (50, 50, 50), 3) #blue car end
    arcade.draw_line(280, w + 55, 280, w +45, (50, 50, 50), 3) #green car start
    arcade.draw_line(280, w + 5, 280, w + 15, (50, 50, 50), 3)
    arcade.draw_line(320, w + 55, 320, w +45, (50, 50, 50), 3)
    arcade.draw_line(320, w +5, 320, w +15, (50, 50, 50), 3) #green car end
    arcade.draw_line(380, w + 80, 380, w +70, (50, 50, 50), 3) #red car start
    arcade.draw_line(380, w +30, 380, w +40, (50, 50, 50), 3)
    arcade.draw_line(420, w + 80, 420, w +70, (50, 50, 50), 3)
    arcade.draw_line(420, w +30, 420, w +40, (50, 50, 50), 3) #red car end, cars end
arcade.draw_rectangle_filled(525, 300, 100, 100, (230, 20, 0)) #barn start
barnPoints = (475, 350), (575, 350), (525, 400)
barnPoints2 = (480, 350), (570, 350), (525, 395)
arcade.draw_polygon_filled(barnPoints, (230, 20, 0))
arcade.draw_polygon_outline(barnPoints2, (240, 240, 240), 3)
arcade.draw_rectangle_outline(525, 300, 90, 90, (240, 240, 240), 3)
arcade.draw_line(480, 345, 570, 255, (240, 240, 240), 3)
arcade.draw_line(570, 345, 480, 255, (240, 240, 240), 3)
arcade.draw_lrtb_rectangle_filled(500, 550, 310, 255, (240, 240, 240)) #barn end
arcade.draw_text("CROSSY ROAD", 200, 559, (0, 0, 0), 24) #text
arcade.finish_render()
arcade.run()



