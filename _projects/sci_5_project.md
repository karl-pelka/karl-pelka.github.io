---
layout: page
title: Near-field optics
description: Number theoretic information in the Talbot-effect
img: assets/img/publication_preview/Talbot.gif
importance: 5
category: science
related_publications: true
---
<h3><b><i><u> Prime Number Decomposition Using the Talbot Effect</u></I></b></h3>

This paper explores an unusual connection between **wave optics** and **number theory**, showing how a physical interference phenomenon can be used to reveal the structure of prime numbers. The key physical ingredient is the **Talbot effect**, a self-imaging phenomenon in optics where a periodic pattern of light reproduces itself at specific distances as it propagates.

We exploit this effect by encoding a mathematical sequence into a diffraction pattern and then letting it evolve under free-space propagation. At certain propagation distances (the so-called **Talbot lengths**), the interference pattern reconstructs structured information that depends sensitively on number-theoretic properties of the input.

The central idea is that when the system is set up with a carefully chosen periodic input, the resulting optical intensity patterns naturally separate contributions associated with **divisibility structure**. In particular, the interference fringes encode information that can be interpreted as a form of **prime decomposition signal**, where primes and composites leave distinct signatures in the reconstructed wave pattern.

Rather than performing factorization through traditional computation, the method effectively uses physics itself to carry out a highly parallel interference process. The “computation” happens through wave propagation, where constructive and destructive interference amplify or suppress contributions tied to specific integer factors.

<h3><b><i><u> Why this matters</u></I></b></h3>

While this is not a replacement for efficient classical or quantum factoring algorithms, it demonstrates a striking example of **physical computation**, where mathematical structure emerges from wave dynamics. It highlights how optical systems can be used as analog computers for certain classes of problems, especially those involving periodicity and number structure.

More broadly, the work connects optics, signal processing, and number theory, showing that concepts like interference and self-imaging can be repurposed to explore deep mathematical properties in a physically intuitive way.

In short, the paper shows that wave interference in the Talbot effect can be engineered to reveal hidden structure in integers, offering a physical lens through which prime decomposition can be visualized rather than computed.

During my Master's thesis I dove into the connection of the Talbot effect and it's description through Gauss Sums which are commonly used in number theory. It turns out that a clever measurement of the intensity in the "Talbot-carpet" along a certain line measures the Gauss-Sum directly and hence it can be used to "measure" prime number decompositions which we have shown experimentally in {%cite Pelka2018%}

<div class="row" style="text-align: center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/publication_preview/Talbot.gif" title="example image" class="img-fluid rounded z-depth-1" width="500" %}
    </div>
</div>
<div class="caption">
    Measurement of the Talbot Effect.
</div>
