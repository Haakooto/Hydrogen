import numpy as np
from scipy.special import assoc_laguerre, lpmv
from math import factorial as f


class Hydrogen:
    """
    Class for handling all physics-related matter
    Should make sure quantum numbers nlm are valid,
    and calculate probability distrubution of electrons
    """
    """
    Bunch of functions for setting and validating quantum numbers.
    ! Look absolutely HORRIBLE!!
    * But works ¯\_(ツ)_/¯
    """

    def n_inc(self):
        self.n += 1

    def n_dec(self):
        if self.n != 1:
            self.n -= 1
        if self.l == self.n:
            self.l -= 1
        if self.m == self.n:
            self.m -= 1
        elif self.m + self.n == 0:
            self.m += 1

    def l_inc(self):
        if self.l != self.n - 1:
            self.l += 1

    def l_dec(self):
        if self.m == self.l != 0:
            self.m -= 1
        elif self.m == -self.l != 0:
            self.m += 1
        if self.l != 0:
            self.l -= 1

    def m_inc(self):
        if self.m != self.l:
            self.m += 1

    def m_dec(self):
        if self.m + self.l != 0:
            self.m -= 1

    def get_n(self):
        return self.n

    def get_l(self):
        return self.l

    def get_m(self):
        return self.m


class Hydrogen(Hydrogen):
    def __init__(self, n=1, l=0, m=0):
        self.n = n
        self.l = l
        self.m = m

        self.polar()

        self.prob = 0.001
        self.dprob = 0.0001

    def up(self):
        self.prob += self.dprob

    def down(self):
        self.prob -= self.dprob

    def polar(self):
        r = np.linspace(0, 14, 50)
        theta = np.linspace(0, np.pi, 50)
        phi = np.linspace(0, 3 * np.pi / 2, 50)

        self.R, self.Theta, self.Phi = np.meshgrid(r, theta, phi)

        # Cartesian coords
        self.X = self.R * np.cos(self.Phi) * np.sin(self.Theta)
        self.Y = self.R * np.sin(self.Phi) * np.sin(self.Theta)
        self.Z = self.R * np.cos(self.Theta)

    def Radial(self):
        n, l = self.n, self.l
        norm = np.sqrt((2 / n) ** 2 * f(n - l - 1) / 2 / n / f(n + l))
        R = np.exp(-self.R / n) * (2 * self.R / n) ** l
        L = assoc_laguerre(2 * self.R / n, n - l - 1, 2 * l + 1)
        return norm * R * L

    def SphericalHarmonics(self):
        l, m = self.l, self.m
        norm = np.sqrt((2 * l + 1) * f(l - m) / 4 / np.pi / f(l + m))
        phase = np.exp(1j * m * self.Phi)
        L = lpmv(m, l, np.cos(self.Theta))
        return norm * phase * L

    def __call__(self):
        psi = self.Radial() * self.SphericalHarmonics()
        psisq = psi * np.conj(psi)
        X = np.where(psisq > self.prob, self.X, 0)
        Y = np.where(psisq > self.prob, self.Y, 0)
        Z = np.where(psisq > self.prob, self.Z, 0)
        psisq = np.where(psisq > self.prob, psisq, np.nan)
        A = np.asarray(np.where(psisq == np.nan, True, False))
        X = np.ma.masked_array(data=X.flatten(), mask=A.flatten())
        Y = np.ma.masked_array(Y.flatten(), mask=A.flatten())
        Z = np.ma.masked_array(Z.flatten(), mask=A.flatten())

        return X, Y, Z, psisq
