from sys import exit as nelxd
try:
    import sys
    import numpy as np
    import cv2
    from utils import detectColor
except ImportError as err:
    nelxd(err)


class Webcam:

    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.stickers = self.get_coord('main')
        self.current_stickers = self.get_coord('current')
        self.preview_stickers = self.get_coord('preview')

    def get_coord(self, name):
        # This function will be in charge of creating the stickers in the screen, for this
        # a dictionary of webcam coordinates will be applied in order loop through them and
        # write rectangles on screen at that location.

        stickers = {
            'main': [
                    [200, 120],  [270, 120],  [340, 120],
                    [200, 190],  [270, 190],  [340, 190],
                    [200, 260],  [270, 260],  [340, 260]
            ],
            'current': [
                [20, 20], [54, 20], [88, 20],
                [20, 54], [54, 54], [88, 54],
                [20, 88], [54, 88], [88, 88]
            ],
            'preview': [
                [20, 130], [54, 130], [88, 130],
                [20, 164], [54, 164], [88, 164],
                [20, 198], [54, 198], [88, 198]
            ]
        }
        return stickers[name]

    def draw_main_stickers(self, frame):
        """Draws the 9 stickers in the frame."""
        for x, y in self.stickers:
            cv2.rectangle(frame, (x, y), (x+40, y+40), (255, 255, 255), 2)

    def draw_current_stickers(self, frame, state):
        """Draws the 9 current stickers in the frame."""
        for index, (x, y) in enumerate(self.current_stickers):
            cv2.rectangle(frame, (x, y), (x+32, y+32),
                          detectColor.stringtoRGB(state[index]), -1)

    def draw_preview_stickers(self, frame, state):
        """Draws the 9 preview stickers in the frame."""
        for index, (x, y) in enumerate(self.preview_stickers):
            cv2.rectangle(frame, (x, y), (x+32, y+32), detectColor.stringtoRGB(state[index]), -1)

    def color_ordered(self, color):
        order = {
            'green': 'F',
            'white': 'U',
            'blue': 'B',
            'red': 'R',
            'orange': 'L',
            'yellow': 'D'
        }
        return order[color]

    def scan(self):
        """
        Open up the webcam and scans the 9 regions in the center
        and show a preview in the left upper corner.
        After hitting the space bar to confirm, the block below the
        current stickers shows the current state that you have.
        This is show every user can see what the computer toke as input.

        :returns: dictionary
        """

        sides = {}
        preview = ['white', 'white', 'white',
                   'white', 'white', 'white',
                   'white', 'white', 'white']
        state = [0, 0, 0,
                 0, 0, 0,
                 0, 0, 0]
        while len(sides) < 6:
                _, frame = self.cam.read()
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                key = cv2.waitKey(10) & 0xff

                # init certain stickers.
                self.draw_main_stickers(frame)
                self.draw_preview_stickers(frame, preview)

                for index, (x, y) in enumerate(self.stickers):
                    roi = hsv[y:y+40, x:x+40]
                    avg_hsv = detectColor.average_hsv(roi)
                    color_name = detectColor.hsv_tostring(avg_hsv)
                    state[index] = color_name

                    # update when space bar is pressed.
                    if key == 32:
                        preview = list(state)
                        self.draw_preview_stickers(frame, state)
                        face = self.color_ordered(state[4])
                        order = [self.color_ordered(color) for color in state]
                        sides[face] = order
                        print(len(sides))

                # show the new stickers
                self.draw_current_stickers(frame, state)

                # append amount of scanned sides
                text = 'scanned sides: {}/6'.format(len(sides))
                cv2.putText(frame, text, (20, 460), cv2.FONT_HERSHEY_TRIPLEX,
                            0.5, (255, 255, 255), 1, cv2.LINE_AA)

                # quit on escape.
                if key == 27:
                    print(len(sides))
                    break

                # show result
                cv2.imshow("default", frame)

        if len(sides) == 6: 

            self.cam.release()
            cv2.destroyAllWindows()

        return sides


webcam = Webcam()
