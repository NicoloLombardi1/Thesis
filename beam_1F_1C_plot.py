import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib import cm

def beam_1F_1C_plot(L, freq_matrix):

    def A(x):
        return 0.5 * (np.cosh(x) + np.cos(x))
    def B(x):
        return 0.5 * (np.sinh(x) + np.sin(x))
    def C(x):
        return 0.5 * (np.cosh(x) - np.cos(x))
    def D(x):
        return 0.5 * (np.sinh(x) - np.sin(x))

    def beam_1F_1C_equation(x, k):
        return (1/(λ_m[k])**2)*(C(x*λ_m[k])-(A(L*λ_m[k])*D(x*λ_m[k]))/B(L*λ_m[k]))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    [m,n] = np.shape(freq_matrix)
    xpoints = np.linspace(0, L, 200)
    λ_m = freq_matrix[1,:]
    ypoints = beam_1F_1C_equation(xpoints, 0)

    N = abs(ypoints) / ypoints.max()
    ax.scatter(xpoints, ypoints, c = cm.jet(np.abs(ypoints) / ypoints.max()), s = 5)
    ax.set_xlim([0,L])
    ax.set_ylim([-max(abs(ypoints))-L/4, max(abs(ypoints))+L/4])
    ax.set_title('Mode 1: ' + str("{:.2f}".format(freq_matrix[0, 0])) + ' Hz')

    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    bprev = Button(axprev, 'Previous')

    class index:
        ind = 0
        def next_click(self, event):
            self.ind += 1
            ypoints = beam_1F_1C_equation(xpoints, self.ind % n)
            ax.cla()
            ax.grid()
            ax.scatter(xpoints, ypoints, c = cm.jet(np.abs(ypoints) / ypoints.max()), s = 5)
            ax.set_xlim([0,L])
            ax.set_ylim([-max(abs(ypoints))-L/4, max(abs(ypoints))+L/4])
            ax.set_title('Mode ' + str(1 + self.ind % n) + ': ' + str("{:.2f}".format(freq_matrix[0, self.ind % n])) + ' Hz')
            return 0

        def prev_click(self, event):
            self.ind -= 1
            ypoints = beam_1F_1C_equation(xpoints, self.ind % n)
            ax.cla()
            ax.grid()
            ax.scatter(xpoints, ypoints, c = cm.jet(np.abs(ypoints) / ypoints.max()), s = 5)
            ax.set_xlim([0,L])
            ax.set_ylim([-max(abs(ypoints))-L/4, max(abs(ypoints))+L/4])
            ax.set_title('Mode ' + str(1 + self.ind % n) + ': ' + str("{:.2f}".format(freq_matrix[0, self.ind % n])) + ' Hz')
            return 0

    callback = index()
    bnext.on_clicked(callback.next_click)
    bprev.on_clicked(callback.prev_click)

    plt.xlim([0, L])
    plt.ylim([-L, L])
    ax.grid()
    plt.subplots_adjust(bottom=0.2)
    plt.show()

