---
layout: post
title: New paper on ArXiv
date: 2024-02-15 21:01:00
description: Rounting entanglement in quantum networks now on ArXiv!
tags: Entanglement Nonreciprocity
categories: Publications
thumbnail: assets/img/Nonreciprocity.png
---

We have finally put our new paper on routing entanglement in quantum networks on the [ArXiv](https://arxiv.org/abs/2402.08102). We encourage you to go and check it out and discuss with us on the conferences we will attend this year.

The basic idea revolves around amorphous quantum networks---where the nodes consist of bosonic modes---which can be used in some sense to employ any quantum cryptographic scheme or quantum information processing. At some point it will be necessary to distribute quantum resources---such as entanglement---in a controllable manner in distinct nodes of the network. This is where our work comes into play.

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
