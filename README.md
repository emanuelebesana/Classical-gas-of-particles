# Classical-gas-of-particles
With this code I analyze the behavior of a classical gas of particles in 2D. To run the code, simply run the file **gas\.py**.
<br>

I implement the **graphics.py** library to plot in real time the motion of every simulated particle. Then I plot the histogram of the particles' velocities, which should relax to a Maxwell-Boltzmann distribution:\\
$$f(v)d^3v = \left(\frac{m}{2\pi k T}\right)^{3/2} \exp{-\left(\frac{mv^2}{2kT}\right)}d^3v$$
The following figures epresent a certain istant in the simulation:

![histogram](histogram.png) ![particles](particles.png) 


Since this was my first Python project (while getting to learn the language), there is some further work that can be done:

- Write some documentation and clean up the code
- Implement GPU optimization in order to deal with many more particles and speed up everything
- Implement some computational fluid dynamics to speed everything up even more, since I am for now using very basic methods to check whether the particles are in contact with one another or with the 4 walls




