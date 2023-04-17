global hbar, m, a
hbar = 1.0545718e-34
m = 9.10938356e-31
#could work in atomic units and call hbar and m as 1
a = 5.2917721092e-11

#states n=1,2,3,4,....
def energy(n):
    return (n**2 * hbar**2) / (2*m*a**2)

def dtheta(energy, psi):
    return (psi*energy)*(-2m/hbar**2)

def dpsi(energy, theta):


#we want to eventually solve for psi
def psi(n):
    alpha_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    """
    this is a coupled situation and I'm somehow sucking eggs so look at the way I 
    have solved these before and try again. format of equations in greenb nb.
    """


if __name__ == '__main__':
    print(energy(1))
