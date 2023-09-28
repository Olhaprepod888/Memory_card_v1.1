import pygame as p
from random import randint
from time import sleep
from time import*
import sys
p.init()
start_time = time()
fps = p.time.Clock()
mw=p.display.set_mode((1000,700))
image=p.image.load('bgg.jpg')
mw.blit(image,(0,0))
class Area():
    def __init__(self,x,y,width,height, color=None):
        self.rec=p.Rect(x,y,width,height)
        self.color=color
    def draw(self):
        p.draw.rect(mw,self.color,self.rec)
    def ann(self,color):
        p.draw.rect(mw,color,self.rec,5)
    def setx(self,text):
        font1=p.font.Font(None,45)
        image=font1.render(text,True,(0,0,0))
        mw.blit(image,(self.x,self.y))
    def collidepoint(self,x,y):
        return self.rec.collidepoint(x,y)
    def col(self,col):
        p.draw.rect(mw,col,self.rec)
class Picture(Area):
    def __init__(self,x,y,width,height,name):
        super().__init__(x=x,y=y,width= width,height =height,color=None)
        self.image=p.image.load(name)
    def draw2(self):
        mw.blit(self.image,(self.rec.x,self.rec.y))
px=50
py=400
krot= Picture(px, py, 100,100, 'kartin8.png')
krot_up=[p.image.load('kartin5.png'),
      p.image.load('kartin6.png'),
      p.image.load('kartin7.png'),
      p.image.load('kartin8.png')]
krot_down=[p.image.load('kartin7.png'),
        p.image.load('kartin6.png'),
        p.image.load('kartin5.png')]


    
        
        
period = 0
anim=0
game = True
wait = 0
while game:
    
    if wait == 0 :
        wait = 20
        window.blit(ferma, (0,0))
        kurka.drawkartinki()
        sleep(1)
    else:
        wait - = 1
        kurka.rec.x = randint(0,500)
        kurka.rec.y = randint()
        window.blit(ferma, (0,0))



        
        py.time.delay(300)





    
    if wait == 0:
        wait = 20
        
        for i in range(3):
            
            sleep(0.5)
            mw.blit(image,(0,0))
            mw.blit(krot_up[i],(krot.rec.x,krot.rec.y))
            p.display.update()
            
        krot.draw2()
        
        for i in range(3):
            
            sleep(0.5)
            mw.blit(image,(0,0))
            mw.blit(krot_down[i],(krot.rec.x,krot.rec.y))
            p.display.update()           
    else:
        wait -=1
        krot.rec.x = randint(50,900)
        krot.rec.y = randint(50,600)
        mw.blit(image,(0,0))
    
    
    
    for ev in p.event.get():
        if ev.type == p.QUIT:
            game = False
            p.quit()
            sys.exit()
            
    
    
    p.display.update()
    fps.tick(40)
    
               


