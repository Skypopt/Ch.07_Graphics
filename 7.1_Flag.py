'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''
import arcade #
arcade.open_window(494, 260, "Flag project")
arcade.set_background_color((256, 256, 256))
arcade.start_render()
for y in range(10, 281, 40): arcade.draw_line(0, y, 494, y, (191, 10, 48), 20)
arcade.draw_lrtb_rectangle_filled(0, 197.6, 260, 121, (0, 40, 104))
for z in range(142, 260, 30):
    for w in range(33, 165, 31): arcade.draw_text("*", w, z, (255, 255, 255), 10)
for z in range(126, 260, 30):
    for x in range(18, 195, 31): arcade.draw_text("*", x, z, (255, 255, 255), 10)
arcade.finish_render()
arcade.run()