import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib import cm


def recpl_4s_plot(a, b, freq_matrix):
    
    def fun(x, y, k):
        return np.sin(freq_matrix[3,k] * np.pi * y / b) * np.sin(freq_matrix[2,k] * np.pi * x / a)
    
    [m,n] = np.shape(freq_matrix)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(0, a, 50)
    y = np.linspace(0, b, 50)
    X, Y = np.meshgrid(x, y)
    zs = np.array(fun(np.ravel(X), np.ravel(Y), 0))
    Z = zs.reshape(X.shape)

    N = abs(Z)/Z.max()
    ax.set_zlim(zmin = -Z.max()*3, zmax = +Z.max()*3)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cm.jet(N), linewidth=0, antialiased=False, shade=False)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('Mode 1: ' + str("{:.2f}".format(freq_matrix[0, 0])) + ' Hz')

    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    bprev = Button(axprev, 'Previous')

    class index:
        ind = 0
        def next_click(self, event):
            self.ind += 1
            ax.clear()
            zs = np.array(fun(np.ravel(X), np.ravel(Y), self.ind % n))
            Z = zs.reshape(X.shape)
            N = abs(Z)/Z.max()
            ax.set_zlim(zmin = -Z.max()*3, zmax = +Z.max()*3)
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cm.jet(N), linewidth=0, antialiased=False, shade=False)
            ax.set_title('Mode ' + str(1 + self.ind % n) + ': ' + str("{:.2f}".format(freq_matrix[0, self.ind % n])) + ' Hz')
            return 0

        def prev_click(self, event):
            self.ind -= 1
            ax.clear()
            zs = np.array(fun(np.ravel(X), np.ravel(Y), self.ind % n))
            Z = zs.reshape(X.shape)
            N = abs(Z)/Z.max()
            ax.set_zlim(zmin = -Z.max()*3, zmax = +Z.max()*3)
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cm.jet(N), linewidth=0, antialiased=False, shade=False)
            ax.set_title('Mode ' + str(1 + self.ind % n) + ': ' + str("{:.2f}".format(freq_matrix[0, self.ind % n])) + ' Hz')
            return 0

    callback = index()
    bnext.on_clicked(callback.next_click)
    bprev.on_clicked(callback.prev_click)

    plt.subplots_adjust(bottom=0.2)
    plt.show()
