# Geometric model for rectangular detectors in 2x1 array
# (C) Harri Toivonen, HT Nuclear Oy, 27 Dec 2024
# Documentation: Array of two spectrometers for source directional estimation, HT 28 May 2024

def parameterPlotting(a, b, w, h):
    import matplotlib.pyplot as plt
    from matplotlib.figure import Figure
    import numpy as np

    def rectangularModel(a, b, w, h, theta):
        y_theoretical = ((a + w) * np.cos(theta) - h * np.sin(theta)) / (a * np.cos(theta) + b * np.sin(theta))
        for i in range(len(y_theoretical)):
            if y_theoretical[i] > 1:
                y_theoretical[i] = 1
            if y_theoretical[i] < 0:
                y_theoretical[i] = 0
        return y_theoretical

    figureText = 'Source direction using a shield between two Detectors\n'
    x = np.arange(0, 91)
    theta = x * np.pi / 180

    figDirection = plt.figure(num='Rectangular geometry', figsize=[11, 9])
    figDirection.suptitle(figureText + '\nGeometric model: R = [(a + w) * cos(theta) - h * sin(theta)] / [a * cos(theta) + b * sin(theta)] \n Function not valid on the insensitive regions (0 or 1)')
    ax1 = plt.subplot(1, 1, 1)
    
    # Clear the axes to avoid over-plotting
    ax1.cla()

    y_ideal = rectangularModel(a, b, 0, 0, theta)
    ax1.plot(-x, y_ideal, 'r-', linewidth=2)
    ax1.plot(x, y_ideal, 'r-', linewidth=2, label='Ideal case (w=0; h=0)')

    y_theoretical = rectangularModel(a, b, w, h, theta)
    ax1.plot(-x, y_theoretical, 'c-', linewidth=2)
    ax1.plot(x, y_theoretical, 'c-', linewidth=2, label='Geometric model (a, b, w, h)')

    ax1.set_xlabel('Angle \u03b8, deg', fontsize=14)
    ax1.set_ylabel('Ratio of voxel counts (back/front)', fontsize=14)
    ax1.set_xticks([-90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90])
    ax1.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    ax1.grid(alpha=0.6)
    ax1.legend(loc='upper right')

    return figDirection  # Return the figure object

if __name__ == '__main__':
    # Rectangular model parameters
    a = 10
    b = 10
    w = 7.5 
    h = 6

    fig = parameterPlotting(a, b, w, h)
    fig.show()
