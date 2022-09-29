import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib import cm

def beam_2S_plot(L, freq_matrix):

    def beam_2S_equation(x, k):
        return (1 / freq_matrix[1, k]) * np.sin(freq_matrix[1, k] * x)
    fig = plt.figure()
    ax = fig.add_subplot(111)

    [m,n] = np.shape(freq_matrix)
    xpoints = np.linspace(0, L, 200)
    λ_m = freq_matrix[1,:]
    ypoints = beam_2S_equation(xpoints, 0)
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
            ypoints = beam_2S_equation(xpoints, self.ind % n)/L
            ax.cla()
            ax.grid()
            ax.scatter(xpoints, ypoints, c = cm.jet(np.abs(ypoints) / ypoints.max()), s = 5)
            ax.set_xlim([0,L])
            ax.set_ylim([-max(abs(ypoints))-L/4, max(abs(ypoints))+L/4])
            ax.set_title('Mode ' + str(1 + self.ind % n) + ': ' + str("{:.2f}".format(freq_matrix[0, self.ind % n])) + ' Hz')
            return 0

        def prev_click(self, event):
            self.ind -= 1
            ypoints = beam_2S_equation(xpoints, self.ind % n)/L
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
