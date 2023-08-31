import pygame_widgets
from pygame_widgets.button import Button


class Widgets():
    def __init__(self, screen):
        self.sim_paused = 0
        self.button = Button(
            # Mandatory Parameters
            screen,  # Surface to place button on
            20,  # X-coordinate of top left corner
            100,  # Y-coordinate of top left corner
            260,  # Width
            150,  # Height

            # Optional Parameters
            text=['Stop', 'Start'][self.sim_paused],  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=[(200, 50, 0), (0, 200, 20)][self.sim_paused],
            # Colour of button when not being interacted with
            hoverColour=[(200, 50, 0), (0, 200, 20)][self.sim_paused],  # Colour of button when being hovered over
            pressedColour=[(0, 200, 20), (200, 50, 0)][self.sim_paused],  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=self.simulation_change()  # Function to call when clicked on
        )

    def simulation_change(self):
        self.sim_paused = not self.sim_paused

    @staticmethod
    def update(events):
        pygame_widgets.update(events=events)
