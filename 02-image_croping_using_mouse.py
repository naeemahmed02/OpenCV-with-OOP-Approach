import cv2

class MouseCrop:
    """
    A class for cropping images using mouse clicks.

    Attributes:
        image (numpy.ndarray): The input image.
        coordinates (list): A list to store the coordinates of the selected region.
        width (int): The width of the selected region.
        height (int): The height of the selected region.
        cropping (bool): A flag indicating whether the cropping process is active.
    """

    def __init__(self, image):
        """
        Initialize the MouseCrop object.

        Parameters:
            image (numpy.ndarray): The input image.
        """
        self.image = image
        self.coordinates = []
        self.width = 0
        self.height = 0
        self.cropping = False

    def handle_clicks(self, event, x, y, flags, params):
        """
        Method to handle mouse click events.

        Parameters:
            event (int): The type of mouse event.
            x (int): The x-coordinate of the mouse click.
            y (int): The y-coordinate of the mouse click.
            flags (int): Any flags associated with the mouse event.
            params: Optional parameters.
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            self.coordinates = [(x, y)]
            self.cropping = True

        elif event == cv2.EVENT_MOUSEMOVE and self.cropping:
            self.width = abs(x - self.coordinates[0][0])
            self.height = abs(y - self.coordinates[0][1])

        elif event == cv2.EVENT_LBUTTONUP and self.cropping:
            self.coordinates.append((x, y))
            self.cropping = False
            self.width = abs(self.coordinates[1][0] - self.coordinates[0][0])
            self.height = abs(self.coordinates[1][1] - self.coordinates[0][1])

            cv2.rectangle(self.image, self.coordinates[0], self.coordinates[1], (0, 255, 0), 2)

            # Draw width and height strings
            cv2.putText(self.image, f"Width: {self.width}px", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            cv2.putText(self.image, f"Height: {self.height}px", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            cv2.imshow('Image', self.image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            self.crop_image()

    def crop_image(self):
        """
        Method to crop the image based on the selected region.
        """
        if self.width > 0 and self.height > 0:
            cropped_image = self.image[self.coordinates[0][1]: self.coordinates[0][1] + self.height,
                                       self.coordinates[0][0]: self.coordinates[0][0] + self.width]
            cv2.imshow("Cropped Image", cropped_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Please select the image region to crop")

    def show_image(self):
        """
        Method to display the image and handle mouse events.
        """
        cv2.imshow("Image", self.image)
        cv2.setMouseCallback("Image", self.handle_clicks)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    path = "OpenCV-with-OOP-Approach\Lenna.png"
    image = cv2.imread(path)
    if image is not None:
        mouse_click_handler = MouseCrop(image)
        mouse_click_handler.show_image()
    else:
        print("Could not load image")
