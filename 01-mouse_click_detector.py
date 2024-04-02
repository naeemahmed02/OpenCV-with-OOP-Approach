# Importing necessary libraries.
import cv2

# Creating a class to handle mouse clicks on an image
class MouseClickHandler:
    """
    A class to detect mouse clicks on an image.
    """
    def __init__(self, image):
        """
        Initialize the MouseClickHandler object.

        Parameters:
            image (numpy.ndarray): The image on which mouse clicks will be detected.
        """
        self.image = image
        self.coordinates = []  # List to store coordinates of mouse clicks

    # Method to handle mouse clicks
    def handle_click(self, event, x, y, flags, params):
        """
        Method to handle mouse click events.

        Parameters:
            event (int): The type of mouse event.
            x (int): The x-coordinate of the mouse click.
            y (int): The y-coordinate of the mouse click.
            flags (int): Any flags associated with the mouse event.
            params (object): Additional parameters (not used in this method).
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            # Append the coordinates of the mouse click to the list
            self.coordinates.append((x, y))
            print("================================")
            print("Mouse Click detected at: ", (x, y))
            print('Type of the coordinates:', type(self.coordinates))

    # Method to display the image and detect mouse clicks
    def show_image(self):
        """
        Display the image and set up the mouse click event handler.
        """
        cv2.imshow("Mouse Click", self.image)
        cv2.setMouseCallback("Mouse Click", self.handle_click)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Path to the image file
    image_path = 'resources/images/Lenna.png'

    # Read the image from the specified path
    image = cv2.imread(image_path)

    # Check if the image is successfully loaded
    if image is not None:
        # Create an instance of MouseClickHandler class
        mouse_click_handler = MouseClickHandler(image)

        # Show the image and detect mouse clicks
        mouse_click_handler.show_image()
    else:
        print("image not found")
