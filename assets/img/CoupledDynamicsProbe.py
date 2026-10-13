from base64 import b64encode

import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib import animation
from qutip import *

N1 = 10
w1 = 0*7.804 * 2 * np.pi  # oscillator frequency
N2 = 10
w2 = 5.622 * 2 * np.pi  # oscillator frequency
tlist = np.linspace(0, 7.804*5, 101)  # periods

#Es=np.linspace(0,400,21) # epsilon=1/(3mus) gamma_c=1/(1.3 mus)
#m=int(sys.argv[1])
#print(m, Es[m])
#E=Es[m]

#r=np.zeros((N,N))
#k=3
#ld=3000
#r[k][k-1]=1
#r[k-1][k]=1

#X=Qobj(r)
#print(ld*X)

# operators
a = tensor(destroy(N1),identity(N2))
b = tensor(identity(N1),destroy(N2))
n_a = tensor(num(N1),identity(N2))
x_a = (a + a.dag()) / np.sqrt(2)
p_a = -1j * (a - a.dag()) / np.sqrt(2)

n_b = tensor(identity(N1),num(N2))
sigmax_b=tensor(identity(N1),sigmax())
x_b = (b + b.dag()) / np.sqrt(2)
p_b = -1j * (b - b.dag()) / np.sqrt(2)



c_ops = [0*np.sqrt(0.0000001/ (2 * np.pi)) * a, 0*np.sqrt(0.00000012/ (2 * np.pi)) * b]

g=1*0.1 * 2 * np.pi
E_a=1*0.08*2 * np.pi
D_b=1.0*0.5* 2 * np.pi
w_a=w1
w_d=w2*(np.sqrt(1+1.0*4*(g/w2)))
print(w_d)

H0=w1*a.dag()*a+w2*b.dag()*b+g*a.dag()*a*(b.dag()+b)*(b.dag()+b)
H=[]
for i in range(len(tlist)):
    if i<1001:
        H.append(H0+np.cos(w_a*tlist[i])*E_a*p_a+np.sin(w_a*tlist[i])*E_a*x_a+np.cos(w_d*tlist[i])*D_b*p_b+np.sin(w_d*tlist[i])*D_b*x_b)
    else:
        H.append(H0)

def plot_expect_with_variance(N, op_list, op_title, states):
    """
    Plot the expectation value of an operator (list of operators)
    with an envelope that describes the operators variance.
    """

    fig, axes = plt.subplots(1, len(op_list), figsize=(14, 3))

    for idx, op in enumerate(op_list):

        e_op = expect(op, states)
        v_op = variance(op, states)

        axes[idx].plot(tlist, e_op, label="expectation")
        axes[idx].set_xlabel("Time")
        axes[idx].set_title(op_title[idx])

    return fig, axes
    
def display_embedded_video(filename):
    video = open(filename, "rb").read()
    video_encoded = b64encode(video).decode("ascii")
    video_tag = '<video controls alt="test" \
                src="data:video/x-m4v;base64,{0}">'.format(
        video_encoded
    )
    return HTML(video_tag)

alpha=0
psi0 = tensor(basis(N1, 0),basis(N2,0))




result=[psi0.proj()]
results=[psi0.proj().ptrace(0)]
results_b=[psi0.proj().ptrace(1)]
for i in range(len(tlist)-1):
    #H.append(H0+E*np.heaviside(np.cos(w2*tlist[i])-0.999,0)*p+E*0*np.sin(w2*tlist[i])*x)
    adv=mesolve(H[i],result[i],[tlist[i],tlist[i+1]],c_ops,[])
    result.append(adv.states[1])
    results.append(result[i].ptrace(0))
    results_b.append(result[i].ptrace(1))
    #results.append(projector*adv.states[1]*projector/(adv.states[1]*projector).tr())
    

plot_expect_with_variance(N1, [n_a.ptrace(0), x_a.ptrace(0), p_a.ptrace(0)], [r"$n$", r"$x$", r"$p$"],results);

                          
fig, axes = plt.subplots(1, 2, figsize=(10, 5))



def update(n):
    axes[0].cla()
    plot_wigner_fock_distribution(results[n], fig=fig, axes=axes)
    return axes[0].artists + axes[1].artists


anim = animation.FuncAnimation(fig, update, frames=len(results),
                               blit=True)

anim.save(os.path.abspath(os.getcwd())+"/prep_A_animation.mp4", fps=10, writer="ffmpeg")


f = open("probs_A_.txt", "w")
for i in range(len(results)):
    f.write(str(tlist[i])+" ")
    for j in range(N1):
        f.write(str(results[i].diag()[j])+" ")
    f.write(" \n")


f = open("prep_A_probab.txt", "w")
for i in range(len(results)):
    f.write(str(tlist[i])+" ")
    for j in range(N1):
        f.write(str(results[i].diag()[j].real)+" ")
    f.write(" \n")


plot_expect_with_variance(N2, [n_b.ptrace(1), x_b.ptrace(1), p_b.ptrace(1)], [r"$n$", r"$x$", r"$p$"],results_b);

                          
fig, axes = plt.subplots(1, 2, figsize=(10, 5))



def update(n):
    axes[0].cla()
    plot_wigner_fock_distribution(results_b[n], fig=fig, axes=axes)
    return axes[0].artists + axes[1].artists


anim = animation.FuncAnimation(fig, update, frames=len(results_b),
                               blit=True)

anim.save(os.path.abspath(os.getcwd())+"/prep_B_animation.mp4", fps=10, writer="ffmpeg")


f = open("probs_B_.txt", "w")
for i in range(len(results)):
    f.write(str(tlist[i])+" ")
    for j in range(N2):
        f.write(str(results[i].diag()[j])+" ")
    f.write(" \n")


f = open("prep_B_probab.txt", "w")
for i in range(len(results)):
    f.write(str(tlist[i])+" ")
    for j in range(N2):
        f.write(str(results_b[i].diag()[j].real)+" ")
    f.write(" \n")
