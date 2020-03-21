import sys,pygame,random, math

from pygame.locals import *

width=1000
height=500
Color_screen=(255,255,255)
Color_line=(0,0,0)
screen=pygame.display.set_mode((width,height))
screen.fill(Color_screen)


class Node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.visible=True
        self.childs=[]
        self.parent=None
        self.type =0
    
    def draw(self,x,y,scale):
        for c in self.childs:
            if(self.visible):
                if(self.type==0):
                    pygame.draw.line(screen,Color_line,(((self.x*scale)+x),((self.y*scale)+y)),((c.x*scale)+x,(c.y*scale)+y),1)
                elif(self.type==1):
                    if(self.x<c.x):
                        rectx1=(self.x*scale)+x
                        
                        start=3*math.pi/4
                    else:
                        rectx1=(self.x*scale)+x-(2*scale)
                        start=0
                    

                    if(c.y<self.y):
                        recty1=(c.y*scale)+y
                        
                        end=math.pi/4
                    else:
                        
                        recty1=(c.y*scale)+y-(2*scale)
                        end=math.pi
                    
                    pygame.draw.arc(screen,Color_line,Rect(rectx1,recty1,2*scale,2*scale),start,end)
            
            pygame.display.flip()
            c.draw(x,y,scale)

class Glyph:

    def __init__(self,gx,gy):
        
        nodes=[]
        for y in range(5):
            for x in range(4):
                nodes.append(Node(x,y)) 
        n=random.randint(0,len(nodes)-1)
        maze=[]
        self.glyph=[]
        self.root=nodes.pop(n)
        self.glyph.append(self.root)
        maze.append(self.root)
        size=random.randint(3,(len(nodes)-1)/2)
        invisible=random.randint(0,3)
        #print(size)
        while size>0:
            n=random.randint(0,len(maze)-1)
            adjacent=[]
            for i in range(len(nodes)):
                if(nodes[i].x<=maze[n].x+1 and nodes[i].x>=maze[n].x-1 and nodes[i].y<=maze[n].y+1 and nodes[i].y>=maze[n].y-1):
                    if(not(nodes[i].x==maze[n].x and nodes[i].x==maze[n].x)):
                        adjacent.append(i)
                    
                    
            if(len(adjacent)==0):
                maze.pop(n)
            else:
                a=random.randint(0,len(adjacent)-1)
                i=adjacent[a]
                aux=nodes.pop(i)
                
                if(random.random()>0.9):
                    if(invisible>0):
                        aux.visible=False
                        invisible-=1
                aux.parent=maze[n]
                if(aux.x!=aux.parent.x and aux.y!=aux.parent.y):
                    if(random.random()>0.7):
                        aux.type=1
                maze[n].childs.append(aux)
                maze.append(aux)
                self.glyph.append(aux)
                size-=1
        
        smallestx=4
        smallesty=5
        for i in self.glyph:
            if i.x <smallestx:
                smallestx=i.x
            if i.y <smallesty:
                smallesty=i.y

        for i in self.glyph:
            i.x-=smallestx
            i.y-=smallesty        
        self.x=gx
        self.y=gy
        
    
    def draw(self,scale=10):
        self.root.draw(self.x,self.y,scale)
        pygame.display.flip()

glyphs=[]
for x in range(0,16):
    for y in range( 0,8):
        glyphs.append(Glyph(x*60+10,y*60+10))

for g in glyphs:
    g.draw()

while True:
    for events in pygame.event.get():
        if events.type == QUIT:
            sys.exit(0)
    