import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider


class Widgets:
    def __init__(self, screen, sim_paused=0):
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
        self.slider = Slider(
            screen,
            20,
            200,
            100,
            4,
            min=0,
            max=100,
            step=1
        )
        self.slider.colour = (100, 100, 100)
        self.slider.handleColour = (255, 255, 255)
        self.slider.handleRadius = 10

    def simulation_change(self):
        self.sim_paused = not self.sim_paused

    def update(self, events):
        pygame_widgets.update(events=events)
        self.sim_button.inactiveColour = [(200, 50, 0), (0, 200, 20)][self.sim_paused]
        self.sim_button.hoverColour = [(250, 50, 0), (0, 250, 20)][self.sim_paused]
        self.sim_button.pressedColour = [(0, 200, 20), (200, 50, 0)][self.sim_paused]
