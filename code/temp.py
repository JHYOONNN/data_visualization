'''
emtion_data
[anger, happiness, neutral, sadness]

'''

from tkinter import *
from PIL import Image, ImageTk
import time
import capture_img as cap_img
import emotion_get as emo
import random
import math

# data processing before code
################################################################################

mus = [[800, 160], [905, 185]]
for i in range(0,300):
    mus.append([random.uniform(792,913), random.uniform(160, 185)])
for i in range(0,200):
    mus.append([random.uniform(800,895), random.uniform(185, 195)])
for i in range(0,200):
    mus.append([random.uniform(810,880), random.uniform(195, 205)])
for i in range(0,100):
    mus.append([random.uniform(825,865), random.uniform(205, 215)])  
data = [[0.0, 0.002, 0.997, 0.001],
        [0.0, 0.0, 0.998, 0.002],
        [0.0, 0.999, 0.001, 0.0],
        [0.0, 0.013, 0.971, 0.016],
        [0.004, 0.0, 0.981, 0.014],
        [0.0, 0.998, 0.0, 0.0],
        [0.0, 0.53, 0.001, 0.0],
        [0.0, 0.564, 0.433, 0.0],
        [0.001, 0.006, 0.716, 0.276],
        [0.5, 0.006, 0.216, 0.276]
        ]

root = Tk()

ted = Image.open("Ted_fixed.png")
eye_brush_right = Image.open("eye_brush_right.png")
eye_brush_left = Image.open("eye_brush_left2.png")
photoimg = ImageTk.PhotoImage(ted)
photoimg2 = ImageTk.PhotoImage(eye_brush_right)
photoimg3 = ImageTk.PhotoImage(eye_brush_left)
canvas = Canvas(root, width=1000, height=500)
canvas.pack()
my_color = '#%02x%02x%02x' % (30, 30, 30)
ted = canvas.create_image(850, 250, image = photoimg)
eye_brush_right_canv = canvas.create_image(878, 110, image = photoimg2)
eye_brush_left_canv = canvas.create_image(837, 112, image = photoimg3)
mouse = canvas.create_arc(830,180,880,180, start = 0, extent = 180, style = 'arc', width = 3, outline = my_color)
before_value = 0
mouse_before = 0
mouse_value = 0
emotion_change = 0
dxdy_data = []
################################################################################


class draw_ted_emotion:
    def __init__(self, emotion_data, emo_change):     
        global emotion_change
        self.emotion_data = emotion_data
        self.emo_change = emo_change
        if(emo_change == 1):
            emotion_change += 1
    def update_img_by_emotion(self):
        print(self.emotion_data)
        global before_value, eye_brush_left_canv,  eye_brush_right_canv, mouse, mouse_value, mouse_before
        rotate_value = (self.emotion_data[1] - (self.emotion_data[0] + self.emotion_data[3])) * 13
        mouse_value = (self.emotion_data[1] - (self.emotion_data[0] + self.emotion_data[3])) * 20
        
        rotate_value = int(rotate_value // 1)
        rotate = before_value
        before_value = rotate_value
        
        mouse_value = int(mouse_value//1)
        mouse_move = mouse_before
        mouse_before = mouse_value
        
        while(rotate != rotate_value or mouse_value != mouse_move):
            if(rotate != rotate_value):
                if(rotate < rotate_value):
                    rotate += 1
                elif(rotate > rotate_value):
                    rotate -= 1
                ## left eye brush    
                photoimg3_changed = ImageTk.PhotoImage(eye_brush_left.rotate(rotate))
                eye_brush_left_canv = canvas.create_image(837, 112, image = photoimg3_changed)
                ##
                ## right eyebrush
                photoimg2_changed = ImageTk.PhotoImage(eye_brush_right.rotate(-rotate))
                eye_brush_right_canv = canvas.create_image(878, 110, image = photoimg2_changed)
                ##
                
            ## mouse
            if(mouse_move != mouse_value):
                canvas.delete(mouse)
                if(mouse_move >= 0 and mouse_value >= 0):
                    if(mouse_move < mouse_value):
                        mouse_move += 1
                        mouse = canvas.create_arc(830, 180 - mouse_move/2,880,180 + mouse_move/2, start = 180, extent = 180, style = 'arc', width = 3, outline = my_color)
                        print('mouse y : ', 180 -mouse_move)
                    else:
                        mouse_move -= 1
                        mouse = canvas.create_arc(830, 180 - mouse_move/2,880,180 + mouse_move/2, start = 180, extent = 180, style = 'arc', width = 3, outline = my_color)
                elif(mouse_move > 0 and mouse_value < 0):
                    mouse_move -= 1
                    mouse = canvas.create_arc(830, 180 - mouse_move/2,880,180 + mouse_move/2, start = 180, extent = 180, style = 'arc', width = 3, outline = my_color)
                elif(mouse_move < 0 and mouse_value > 0):
                    mouse_move += 1
                    mouse = canvas.create_arc(830, 180 + mouse_move/2,880,180 - mouse_move/2, start = 0, extent = 180, style = 'arc', width = 3, outline = my_color)
                elif(mouse_move <= 0 and mouse_value <= 0):
                    if(mouse_move < mouse_value):
                        mouse_move += 1
                        mouse = canvas.create_arc(830, 180 + mouse_move/2,880,180 - mouse_move/2, start = 0, extent = 180, style = 'arc', width = 3, outline = my_color)
                    else:
                        mouse_move -= 1
                        mouse = canvas.create_arc(830, 180 + mouse_move/2,880,180 - mouse_move/2, start = 0, extent = 180, style = 'arc', width = 3, outline = my_color)
                
                print(mouse_move, mouse_value)
            canvas.after(10)
            canvas.update()
    
    def draw_mus(self):
        global mus, my_color, dxdy_data, emotion_change
        print(len(mus))
        if(self.emo_change == 1 and emotion_change == 1):
            for i in range(0, len(mus)): 
                rand = random.uniform(5/8, 3/8)
                if(rand > 0.5):
                    dx = -math.cos(rand*math.pi)
                    dy = math.sin(rand*math.pi)
                else:
                    dx = -math.cos(rand*math.pi)
                    dy = math.sin(rand*math.pi)
                print("dx, dy : ", dx,dy)
                dxdy_data.append([dx,dy])
        if(emotion_change >= 1):
            for i in range(0, len(mus)):
                canvas.create_line(mus[i][0], mus[i][1], mus[i][0]+dxdy_data[i][0]*emotion_change*0.5,mus[i][1]+dxdy_data[i][1]*emotion_change*0.5, width = 1, fill = my_color)
            canvas.create_arc(830,128,845,140+(emotion_change-1)*0.5, style= 'arc', start = 180, extent = 180, width = 4, outline = '#%02x%02x%02x' % (50, 50, 60))
            canvas.create_arc(872,130,887,142 + (emotion_change-1)*0.5, style= 'arc', start = 180, extent = 180, width = 4, outline = '#%02x%02x%02x' % (50, 50, 60))
            
    def draw(self):
        self.update_img_by_emotion()
        self.draw_mus()
        canvas.after(10)
        canvas.update()
class main:
    def __init__(self):
        #self.get_image_info = cap_img.main("./video/emotion_test.mp4").return_value()
        root.after(1000, self.print_emotion)
        root.mainloop()
       
    def print_emotion(self):
         #for i in range(0, self.get_image_info[0]):
            #emotion_get = emo.get_emotion(self.get_image_info[1]).get_emotion_pic(i)
        for i in range(0,len(data)):
            emotion_change = 0
            if(i>0):
                if((data[i][0] + data[i][3]) - data[i][1]<0 and (data[i-1][0] + data[i-1][3]) - data[i-1][1]>0):
                    emotion_change = 1
                if((data[i][0] + data[i][3]) - data[i][1]>0 and (data[i-1][0] + data[i-1][3]) - data[i-1][1]<0):
                    emotion_change = 1
            draw_ted_emotion(data[i],emotion_change).draw()
        print("done")
    
if __name__ == '__main__':
    main()