---
layout: page
title: Floquet Dynamics
description: Optomechanical systems under the influence of periodic modulation
img: assets/img/publication_preview/FloquetLasing.gif
importance: 2
category: science
related_publications: Pelka2022A, Mercade2021

---

During my PhD I studied the backaction of optomechanical systems under periodic intensity modulation, which lead to a periodic Hamiltonian. It enables the mechanical modes to trigger the instability of another mechanical mode. In the blue detuned regime, it is possible to attain mode-locked lasing of two modes even though there is mode competition which was shown experimentally in {% cite Mercade2021 %}. The theoretical formalism shows, that the intensity modulation needs to occur at the difference frequency of the two mechanical oscillators. There is a wonderful intuition that explains the physics of this system in terms of a choir as shown in the figure below.

<div class="row" style="text-align: center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/publication_preview/FloquetLasing.gif" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Floquet Lasing.
</div>

Imagine two groups singing a 4/3 polyrhythm such that the upper group sings notes at a frequency of 4 Hz whilst the other group in the lower line of the clave sings notes at a frequency of 3 Hz. A conductor would indicate the 1 of each measure at a frequency of 1 Hz which happens to be the difference frequency of the two groups.

Employing the same formalism it is also possible to have one mechanical mode trigger the instability---optomechanical bistability in this case---of the other mechanical mode which is published in {% cite Pelka2022A %}.
