import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import scipy.optimize 
from matplotlib import cm
import matplotlib.animation as animation
from scipy.interpolate import CubicSpline
from sympy import *
from scipy.special import jv, iv


def cirpl_1C_plot(a, freq_matrix):
    λ = freq_matrix[1,:] / a

    def cirpl_1C_equation(r, p, k):
        return (jv(freq_matrix[3,k], λ[k] * r) - jv(freq_matrix[3,k], freq_matrix[1,k]) * iv(freq_matrix[3,k],  λ[k] * r) / iv(freq_matrix[3,k], freq_matrix[1,k])) * np.cos(p * freq_matrix[3,k])


    [m,n] = np.shape(freq_matrix)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    r_points = np.linspace(0, a, 100)
    p_points = np.linspace(0, 2 * np.pi, 100)
    R, P = np.meshgrid(r_points, p_points)
    X, Y = R*np.cos(P), R*np.sin(P)
    zs = np.array(cirpl_1C_equation(np.ravel(R), np.ravel(P), 0))
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
            zs = np.array(cirpl_1C_equation(np.ravel(R), np.ravel(P), self.ind % n))
            Z = zs.reshape(X.shape)
            N = abs(Z)/Z.max()
            ax.set_zlim(zmin = -Z.max()*3, zmax = +Z.max()*3)
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cm.jet(N), linewidth=0, antialiased=False, shade=False)
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cm.jet(N), linewidth=0, antialiased=False, shade=False)
            ax.set_title('Mode ' + str(1 + self.ind % n) + ': ' + str("{:.2f}".format(freq_matrix[0, self.ind % n])) + ' Hz')
            ax.set_zlim
            return 0

        def prev_click(self, event):
            self.ind -= 1
            ax.clear()
            zs = np.array(cirpl_1C_equation(np.ravel(R), np.ravel(P), self.ind % n))
            Z = zs.reshape(X.shape)
            N = abs(Z)/Z.max()
            ax.set_zlim(zmin = -Z.max()*3, zmax = +Z.max()*3)
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cm.jet(N), linewidth=0, antialiased=False, shade=False)
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cm.jet(N), linewidth=0, antialiased=False, shade=False)
            ax.set_title('Mode ' + str(1 + self.ind % n) + ': ' + str("{:.2f}".format(freq_matrix[0, self.ind % n])) + ' Hz')
            return 0

    callback = index()
    bnext.on_clicked(callback.next_click)
    bprev.on_clicked(callback.prev_click)

    plt.subplots_adjust(bottom=0.2)
    plt.show()