---
layout: page
title: Spontaneous symmetry breaking
description: Chimera states in optomechanics
img: assets/img/publication_preview/Chimera.gif
importance: 4
category: science
related_publications: true
---

<h3><b><i><u> Chimera States in Small Optomechanical Arrays</u></I></b></h3>

This paper studies how groups of tiny mechanical oscillators—systems that can vibrate and interact through light—can organize themselves into surprising collective patterns. These systems, called **optomechanical arrays**, consist of multiple coupled mechanical resonators whose motion is driven and controlled by light.

When such oscillators are weakly connected, they often try to synchronize, much like metronomes placed on a shared surface eventually falling into step. However, we show that in optomechanical arrays, synchronization does not always occur uniformly. Instead, the system can split into a strange mixed state known as a **chimera state**, where some oscillators move in perfect sync while others remain incoherent and disordered.

The paper demonstrates that these chimera states can emerge naturally when the mechanical elements have small differences in their intrinsic frequencies (a property called *frequency heterogeneity*). Using a combination of analytical calculations and numerical simulations, we show that this imbalance is not a flaw but a key ingredient for stabilizing these hybrid synchronized–unsynchronized phases.

<h3><b><i><u> Why this matters</u></I></b></h3>

Understanding how synchronization breaks down is important for both fundamental physics and future technologies. Optomechanical arrays are promising building blocks for precision sensing and signal processing, where coordinated motion is often essential. Chimera states reveal that even in well-controlled quantum and classical devices, partial synchronization can arise spontaneously, potentially affecting performance—or even being harnessed as a feature.

More broadly, the results connect quantum optomechanics to the wider study of collective behavior in complex systems, showing how simple interactions between many oscillators can produce unexpectedly rich and structured dynamics.

In short, the paper shows that even in carefully engineered light–matter systems, order and disorder can coexist in stable patterns, revealing new ways collective motion can organize itself in the quantum regime.

My first venture during my PhD went into the statistical physics of optomechanical arrays as their nonlinear dynamics offers a rich variety of behaviour. I found out in {% cite Pelka2020 %} that two identical arrays can encounter so-called spontaneous symmetry breaking upon coupling them weakly together. Here, the broken symmetry is the $$\mathbb{Z}_2$$-exchange symmetry of the arrays while the order parameter is given by the complex synchronisation-parameter $$\frac{1}{N}\sum\limits_{j=1}^{N}\exp(i\phi_j)$$ of each array. The control parameter is the mechanical coupling which can lead the system to attain synchronisation in only one of the arrays whilst the other cannot synchronise anymore. 

<div class="row" style="text-align: center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/publication_preview/Chimerasq.gif" title="example image" class="img-fluid rounded z-depth-1" width="500" %}
    </div>
</div>
<div class="caption">
    Animation of a chimera state.
</div>

This animation shows the behaviour of a two arrays in the Chimera phase under slight variation of the initial condition. The upper line shows the evolutino of some initial condition of the first array (upper left picture) and the second array (upper right picture) which shows that the second array synchronises under the weak mechanical coupling. The second row shows that only changing this inital condition slightly as indicated in the red circles characterising the deviation in initial condition hinders the first array (lower left picture) to synchronise whilst the second array (lower right picture) perfectly synchronises now. This behaviour depends only on the initial condition, as caused by a thermal fluctuation for instance, and has been coined Chimera state reflecting the two different behaviours that each system shows.
