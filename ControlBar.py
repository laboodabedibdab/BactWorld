import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider


class Widgets:
    def __init__(self, screen, sim_paused=0):
        self.clearV = False
        self.running = True
        self.clr_button = Button(
            # Mandatory Parameters
            screen,  # Surface to place button on
            20,  # X-coordinate of top left corner
            250,  # Y-coordinate of top left corner
            100,  # Width
            40,  # Height

            # Optional Parameters
            text='clear',  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(200, 50, 0),
            # Colour of button when not being interacted with
            hoverColour=(250, 50, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=self.clear  # Function to call when clicked on
        )
        self.ext_button = Button(
            # Mandatory Parameters
            screen,  # Surface to place button on
            20,  # X-coordinate of top left corner
            300,  # Y-coordinate of top left corner
            100,  # Width
            40,  # Height

            # Optional Parameters
            text='exit',  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(200, 50, 0),
            # Colour of button when not being interacted with
            hoverColour=(250, 50, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=self.stop  # Function to call when clicked on
        )
        self.sim_paused = sim_paused
        self.sim_button = Button(
            # Mandatory Parameters
            screen,  # Surface to place button on
            20,  # X-coordinate of top left corner
            100,  # Y-coordinate of top left corner
            100,  # Width
            40,  # Height

            # Optional Parameters
            text=['Stop', 'Start'][self.sim_paused],  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=[(200, 50, 0), (0, 200, 20)][self.sim_paused],
            # Colour of button when not being interacted with
            hoverColour=[(250, 50, 0), (0, 250, 20)][self.sim_paused],  # Colour of button when being hovered over
            pressedColour=[(0, 200, 20), (200, 50, 0)][self.sim_paused],  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=self.simulation_change  # Function to call when clicked on
        )
        self.sim_slider = Slider(
            screen,
            20,
            200,
            100,
            4,
            min=1,
            max=100,
            step=1
        )
        self.sim_slider.colour = (100, 100, 100)
        self.sim_slider.handleColour = (255, 255, 255)
        self.sim_slider.handleRadius = 10
        self.sim_slider.value = 1
        self.FPS = 0

    def simulation_change(self):
        self.sim_paused = not self.sim_paused

    def clear(self):
        self.clearV = True

    def stop(self):
        self.running = False

    def update(self, events, screen, clock: pygame.time.Clock):
        self.FPS = clock.get_fps()
        self.FPS = "0" * (4 - len(str(int(self.FPS)))) + str(int(self.FPS) // 5 * 5)
        screen.blit(pygame.font.SysFont('arial', 55).render(self.FPS, False, (200, 200, 200)), (20, 10))
        pygame_widgets.update(events)
        self.sim_button.inactiveColour = [(200, 50, 0), (0, 200, 20)][self.sim_paused]
        self.sim_button.hoverColour = [(250, 50, 0), (0, 250, 20)][self.sim_paused]
        self.sim_button.pressedColour = [(0, 200, 20), (200, 50, 0)][self.sim_paused]
        self.sim_button.text = self.sim_button.font.render(['Stop', 'Start'][self.sim_paused], True,
                                                           self.sim_button.textColour)
