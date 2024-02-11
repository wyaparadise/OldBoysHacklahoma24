import pygame
import scenes 

pygame.init()

#Font

text_speed = 20
FONT_SCREEN_BIG = pygame.freetype.Font("/Users/charliestreet/Desktop/Hacklahoma 2024/OldBoysHacklahoma24/assets/fonts/oldterminal.ttf",50)
FONT_SCREEN = pygame.freetype.Font("/Users/charliestreet/Desktop/Hacklahoma 2024/OldBoysHacklahoma24/assets/fonts/oldterminal.ttf",24)
FONT_SCREEN_SMALL = pygame.freetype.Font("/Users/charliestreet/Desktop/Hacklahoma 2024/OldBoysHacklahoma24/assets/fonts/oldterminal.ttf",18)
COLOR_TERMINAL = (110,230,10)

#UI 
image_computer = pygame.image.load("/Users/charliestreet/Desktop/Hacklahoma 2024/OldBoysHacklahoma24/assets/computerbase.png")
image_computer = pygame.transform.scale(image_computer, (1280, 720))
TEXT_POS = (400,150)

#Display

pygame.display.set_caption("|---VEGA---|")
screen = pygame.display.set_mode((1280, 720))

#Sounds

SOUND_CHITTER1 = pygame.mixer.Sound("/Users/charliestreet/Desktop/Hacklahoma 2024/OldBoysHacklahoma24/assets/sounds/Chitter1.wav") 
SOUND_TYPINGSOUND1 = pygame.mixer.Sound("/Users/charliestreet/Desktop/Hacklahoma 2024/OldBoysHacklahoma24/assets/sounds/TypingSound1.wav")
SOUND_TYPINGSOUND = pygame.mixer.Sound("/Users/charliestreet/Desktop/Hacklahoma 2024/OldBoysHacklahoma24/assets/sounds/TypingSound.wav")
SOUND_TOGGLE = pygame.mixer.Sound("/Users/charliestreet/Desktop/Hacklahoma 2024/OldBoysHacklahoma24/assets/sounds/Toggle.wav") 
SOUND_BEEP5 = pygame.mixer.Sound("/Users/charliestreet/Desktop/Hacklahoma 2024/OldBoysHacklahoma24/assets/sounds/Beep5.wav") 

pygame.mixer.music.load('/Users/charliestreet/Desktop/Hacklahoma 2024/OldBoysHacklahoma24/assets/sounds/BackgroundEther.wav')

# Setting the volume 

  
# Start playing the song 
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#Time

fps =  60

clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT + 1, text_speed)
pygame.time.set_timer(pygame.USEREVENT + 2, 1)

#Game

class Resources(object):
    def __init__(self, food, fuel, credits):
        self.food = food
        self.fuel = fuel
        self.credits = credits


resources = Resources(50, 500, 1250)

def main():

    running = True

    #Main Loop
    

    currentScene = Scene("1",TEXT_POS,FONT_SCREEN, COLOR_TERMINAL)
    CurrentSound = None

    onTitle = True

    while running: 

        if onTitle == True:
            #print("hi")
        
            screen.fill('black')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        onTitle = False
                        print("keydown")


            FONT_SCREEN_BIG.render_to(screen,(50,50), "WELCOME TO VEGA",COLOR_TERMINAL)
            FONT_SCREEN_BIG.render_to(screen,(50,150), "Press Space",COLOR_TERMINAL)

        else:
            for event in pygame.event.get():
                result = None
                if event.type == pygame.QUIT:
                    running = False 

                if event.type == pygame.USEREVENT + 1: 
                    currentScene.update()


                if event.type == pygame.USEREVENT + 2: 
                    #print("userevent2")
                    if currentScene.done == False:

                        CurrentSound = SOUND_TYPINGSOUND
                        if pygame.mixer.Sound.get_num_channels(CurrentSound) < 1:
                            pygame.mixer.Sound.play(CurrentSound)
                        #SoundTick = pygame.mixer.Sound.get_length

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        result = processChoice(currentScene,"a")

                    if event.key == pygame.K_2:
                        result = processChoice(currentScene,"b")

                    if event.key == pygame.K_3:
                        result = processChoice(currentScene,"c")

                    if event.key == pygame.K_4:
                        result = processChoice(currentScene,"d")
                    
                    if result != None:
                        currentScene = Scene(result,TEXT_POS,FONT_SCREEN,COLOR_TERMINAL)

                        print("Current scene ID is: " + str(currentScene.id))

            #Draw UI

            screen.fill('black')
            screen.blit(image_computer,(0,0))

            #Draw text

            #Food meter
            FONT_SCREEN_SMALL.render_to(screen,(25,475), "FOOD:", COLOR_TERMINAL)
            FONT_SCREEN.render_to(screen,(25,495), (str(resources.food) + "kg"), COLOR_TERMINAL)

            #Fuel meter
            FONT_SCREEN_SMALL.render_to(screen,(150,475), "FUEL:", COLOR_TERMINAL)
            FONT_SCREEN.render_to(screen,(150,495), (str(resources.fuel)) + "L", COLOR_TERMINAL)

            #Credits

            FONT_SCREEN.render_to(screen,(310,675), "CREDITS:", COLOR_TERMINAL)
            FONT_SCREEN.render_to(screen,(420,670), "$" + (str(resources.credits)), COLOR_TERMINAL)
            currentScene.draw()

            #Debug

            FONT_SCREEN_SMALL.render_to(screen,(940,490), str(currentScene.id), COLOR_TERMINAL)

        pygame.display.flip()

        clock.tick(fps)


def processChoice(scene, choice):
    key = scene.id + choice
    pygame.mixer.Sound.play(SOUND_BEEP5)

    if key in scenes.textDict:
 
        if key in functionDict:
            functionDict[key]()
        return key
    else: return "1"




def text_generator(text):
    tmp = ''
    for letter in text:
        tmp += letter
        # don't pause for spaces
        if letter != ' ':
            yield tmp


class Scene(object):
    def __init__(self, id, pos, font, color):
        self.color = color
        self.font = font

        self.done = False
        self.id = id

        self.textgap = 40

        self.text = scenes.textDict[id]
        self.index = 0

        self._gen = text_generator(self.text[self.index])

        self.pos = pos
        self.update()
        
    def update(self):
        if not self.done:
            try: 
                self.rendered = next(self._gen)

            except StopIteration: 
                
                if self.index > (len(self.text)-2):
                    self.done = True
                    return
                self.index += 1

                self._gen = text_generator(self.text[self.index])
                self.update()

    def draw(self):

        for i in range(0, self.index):
            self.font.render_to(screen,(self.pos[0],self.pos[1]+i*self.textgap),self.text[i], self.color)
            
        self.font.render_to(screen,(self.pos[0],self.pos[1]+self.index*self.textgap),self.rendered, self.color)

class Astroneer(object):
    def __init__(self,name,color):
        self.name = name
        self.color = color

        sanity = 0
        status = 0


def f1aa():
    print("option 1aa function called")

def f1ab():
    print("f1ab called")
    resources.food = resources.food - 10
    resources.fuel = resources.fuel + 30

def f1ba():

    resources.credits = resources.credits + 10*10 
    resources.food = resources.food -10
    
def f1bb():
    resources.credits = resources.credits + 25*10
    resources.food = resources.food - 25
    

def f1bc():
    resources.credits = resources.credits + resources.food*10
    resources.food = 0

    
functionDict = { 
    "1aa" : f1aa,
    "1ab" : f1ab,
    "1ba" : f1ba,
    "1bb" : f1bb,
    "1bc" : f1bc
}

main()
pygame.quit