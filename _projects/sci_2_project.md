---
layout: page
title: CV Quantum Information
description: Non-reciprocal entanglement propagation
img: assets/img/Nonreciprocity.png
importance: 2
category: science
related_publications: true
---

<h3><b><i><u>Giving Quantum Entanglement a Sense of Direction</u></I></b></h3>

One of the strangest features of quantum physics is entanglement—a connection between particles that persists even when they are far apart. Entanglement is the key ingredient behind future technologies such as quantum communication, distributed quantum computing, and ultra-secure networks. But there is a practical problem: once entanglement is created, it tends to spread in all directions rather than flowing where it is actually needed.

The paper "Routing Entanglement through Quantum Networks" {% cite Pelka2026 %} tackles exactly this challenge. Rather than asking how to create more entanglement, we asked a subtler question: Can we steer entanglement through a network as if it were traffic on a road system?

Their answer is yes.

We worked on this by considering a network of continuously interacting quantum systems, where each node can exchange quantum information with its neighbors. Normally, these interactions are reciprocal: if one node influences another, the reverse is equally true. This symmetry makes entanglement spread much like ripples on a pond.

The key innovation is to break this symmetry. By carefully engineering the interactions between the nodes—and exploiting a technique known as engineered dissipation—we create non-reciprocal transport. In effect, the network behaves like a system of one-way streets, allowing entanglement to preferentially travel in a chosen direction instead of diffusing everywhere. Importantly, this requires only Gaussian operations, which are among the best-understood and most experimentally accessible tools in continuous-variable quantum optics.

An interesting finding is that stronger is not always better. One might expect that making the initial source of entanglement more powerful would simply allow it to travel farther through the network. Instead, the study reveals a more complicated picture. The distance over which useful entanglement survives depends on a delicate balance between the strength of the source, the coupling between neighboring nodes, and unavoidable thermal noise. In some cases, increasing one parameter can actually reduce how far entanglement propagates—a counterintuitive result that highlights the subtle nature of quantum systems.

<h3><b><i><u>Why does this matter?</u></I></b></h3>

Today's internet routes packets of classical information through switches and routers. Tomorrow's quantum internet will need to distribute fragile entangled states between distant users. Much of the existing research focuses on deciding which path entanglement should follow through a network. This work explores a complementary idea: designing the physical network itself so that entanglement naturally flows in the desired direction, reducing the need for active control.

The work remains theoretical, but it points toward hardware that could one day behave like quantum diodes or quantum traffic systems, directing entanglement to where it is needed while suppressing unwanted backflow. If realized experimentally, such devices could become an important building block for scalable quantum communication networks, distributed quantum sensors, and interconnected quantum computers.

In short, the paper shows that the future quantum internet may require more than just generating entanglement—it may also require learning how to route it.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/Nonreciprocity.png" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/RETQNFig2.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Our imagination of an open system arrays decaying into common baths to establish nonreciprocity (left) and its capability to route entanglement (right) as evaluated through the logarithmic negativity
</div>

We imagine an array of open bosonic quantum systems, depicted in the left picture, that are arranged such that there exist two different possibilities to hop from one node to the next. These can be tuned to enable nonreciprocal hopping such that any excitation that travels down the channel cannot travel back. Through connecting this quantum channel with an external, squeezed oscillator we generate quanta that are identical in their quantum properties. We investigate the steady state where these quanta have been propagated through the channel and see that the quantifier---the logarithmic negativity which is non-zero for entangled parties---shows entanglement if the directionality permits transmission of excitations.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/RETQNFig3.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    The propagation depth through the channel as it depends on the squeezing and coupling into the channel and the amount of excitations generated in the final entangled node
</div>

Moreover we find that stronger squeezing reduces the amount of nodes that the entanglement can be propagated through the network even though it is the entanglement generating process. We link it to the amount of mean excitations that are generated in this process "heating" up the channel until it becomes unstable.

