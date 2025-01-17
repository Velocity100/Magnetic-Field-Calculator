# Magnetic-Field-Calculator
Uses Biot-Savart law to calculate the magnetic field components and magnitude for arbitrary current contributions and user-defined coordinates, for both 2D and 3D, for magnetostatic systems. Any version of numpy is needed.

# Usage
The BlibV3.py file is the main Python file with the magnetic field calculator function. The current distribution(s) must be parametrized using a 3D cartesian coordinate system, which must be inputted as lists or arrays for x, y and z positions. For multiple current distributions, each x, y and z list/array for each wire must be v-stacked (using np.vstack() for example), separately for each dimension. (For example, if we had 2 wires and x1 and x2 are the x positions for wire 1 and wire 2, then the x position must be inputted as np.vstack((x1,x2)) for the function to work properly. Repeat for y and z). A coordinate point (x,y,z) is then defined to evaluate the magnetic field components and magnitude. For singular points, no list/array is necessary and can just be inputted as an int or float, but multiple points must be inputted as numpy arrays, separate for each dimension. See the Examples folder for further details. 

For example, looking at the Solenoid.py file, we can simulate a solenoidal current distribution and plot the magnetic field using the Plotly library (Plotly not required):

![newplot (4)](https://github.com/user-attachments/assets/c950aa6c-ed06-4fda-93d9-7f3f5b352130)
