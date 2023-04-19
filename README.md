# color_picker

Image Color Analysis Project
This project is written in Python and aims to analyze images to select the top 10 most frequently occurring colors in an image. The project uses the K-means algorithm for color clustering in the image.

System Requirements
The project is written in Python and requires an installed Python interpreter (version 3.x) and the following libraries:

numpy
scikit-learn
PIL (Pillow)

Running the Project
Clone or download the repository to your local environment.
Make sure you have the required libraries described in the "System Requirements" section installed.
Run the main.py script in your Python environment, providing the path to the image you want to analyze as an argument.
The program will generate an output file with the top 10 most frequently occurring colors in the image.
How the Program Works
The program loads the image using the PIL (Pillow) library and converts it to a numpy array. Then, using the K-means algorithm from the scikit-learn library, it clusters the colors in the image into 10 groups. For each group, the program calculates the average color (cluster center) and saves it as one of the top 10 most frequently occurring colors in the image. The result is saved to a text file.

License
This project is available under the MIT License.



Thank you for your interest in the project!






