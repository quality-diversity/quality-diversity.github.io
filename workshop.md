# Workshop on Benchmarks for Quality-Diversity algorithms
## Description

Quality Diversity (QD) algorithms are a recent family of evolutionary algorithms that aim at generating a large collection of high-performing solutions to a problem. They originated in the "Generative and Developmental Systems'' community of GECCO between 2011 (Lehman and Stanley, 2011) and 2015 (Mouret and Clune, 2015) with the "Novelty Search with Local Competition'' and "MAP-Elites'' evolutionary algorithms. Since then, many algorithms have been introduced (mostly at GECCO), inspired, for example, by surrogate modeling (Gaier et al., 2018, best paper of the CS track), by CMA-ES (Fontaine et al., 2019) or by deep-neuroevolution (Colas et al., 2020, Nilsson et al., 2021 -- Best paper in NE track). Hence, 47\% (7/15) of the papers accepted in the GECCO CS track in 2021 used or introduced novel Quality-Diversity optimization algorithms and 56\%(5/9) in 2020 (see the [list of papers](https://quality-diversity.github.io)).

The objective of this workshop is to develop a first set of benchmarks functions and a set of indicators to compare QD algorithms: for now, most authors introduced their own benchmark functions and indicators, which makes it challenging to compare algorithms and validate implementations. Similar sets of indicators and functions were developed for multi-objective algorithms (ZDT set of functions, Zitzler, Deb and Thiele, 2000) and single-objective algorithms (BBOB series of workshops at GECCO, since 2009). These benchmark suites catalysed research in these fields --- we aim to do the same for quality diversity algorithms. 

Quality Diversity algorithms are different from multi-objective, multi-modal and single-objective algorithms, this is why special benchmarks are needed. In particular, (1) they use a behavior space in addition to the genotype space and the fitness value(s), (2) they aim at both covering the behavior space and finding high-performing solutions, which are often two antagonistic objectives.

This workshop will invite two types of contributions, in the form of short papers (1 to 2 pages):

1. Proposals of benchmark functions, which should ideally be fast to run, easy to implement, and test specific properties (e.g., invariance to a rotation of the behavioral space, alignment between the behavior space and the fitness function, number of local optima, relevance to real-world applications, etc.); for each function, the short paper will at least describe:
	- the genotype space (bounds, etc.);
	- the behavior space;
	- the fitness function.
2. Proposals of indicators to compare algorithms; for instance, the MAP-Elites paper (Mouret \& Clune, 2015) introduced global performance, global reliability and opt-in reliability, but other papers used different indicators. "Confronting the challenge of quality diversity'' (Pugh et. al. 2015) introduced the QD-score indicator often used to compare NSLC-based algorithms. 


Each short paper will be encouraged to showcase preliminary benchmark results with some of the published algorithms. The papers will be reviewed by the organizers of the workshop.

Authors of the selected short papers will be invited to write a common journal article that will be submitted to an evolutionary computation journal (e.g., ECJ/TEC/TELO). This article will be the answer of the community to the question "how to compare Quality Diversity optimization algorithms?'' and will provide the first unified benchmark results with as many algorithms as possible.

## Important dates
TBD

## Organisers (alphabetical order)
- Antoine Cully
- Stéphane Doncieux
- Matthew Fontaine
- Jean-Baptiste Mouret
- Stefanos Nikolaidis
- John Rieffel
- Julian Togelius
