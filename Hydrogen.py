import numpy as np


class Hydrogen:
    def __init__(self, n=1, l=0, m=0):
        self.n = n
        self.l = l
        self.m = m

        r = np.linspace(0, 20, 70)
        theta = np.linspace(0, np.pi, 40)
        phi = np.linspace(0, 3 * np.pi / 2, 40)

        self.R, self.Theta, self.Phi = np.meshgrid(r, theta, phi)

        self.x = self.R * np.cos(self.Phi) * np.sin(self.Theta)
        self.y = self.R * np.sin(self.Phi) * np.sin(self.Theta)
        self.z = self.R * np.cos(self.Theta)

    def Radial(self):
        if self.n == 1:
            R = 2 * np.exp(-self.R)
        elif self.n == 2:
            R = 2 ** -0.5 * (1 - self.R / 2) * np.exp(-self.R / 2)
        else:
            R = 2 / 3 / np.sqrt(3) * (1 - 2 / 3 * self.R + 2/27 * self.R ** 2) * np.exp(-self.R / 3)
        print("|R| ", np.sum(R))
        return R

    def SphericalHarmonics(self):
        #Y = - np.sqrt(3 / 8 / np.pi) * np.sin(self.Theta) * np.exp(1j * self.Phi)
        Y = np.sqrt(1 / 4 / np.pi)
        print("|Y| ", np.sum(Y))
        return Y

    def __call__(self):
        psi = self.Radial() * self.SphericalHarmonics()
        # psi /= np.sum(psi) * 2
        print("|psi| ", np.sum(psi))
        print("max psi ", np.max(psi ** 2))
        sig = np.where(psi ** 2 > 0.0005)
        print(sig[2].shape, np.prod(psi.shape))
        return self.x[sig], self.y[sig], self.z[sig], psi[sig]**2

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
