# Workshop on Benchmarks for Quality-Diversity algorithms
We would like to invite you to submit papers to, and participate in, our GECCO'23 Workshop on Quality Diversity Algorithm Benchmarks.

- When:  Jul 14-16, 2023 (check dates)
- Where: Lisbon, Portugal

Contact: qd-gecco-workshop@inria.fr 

Papers should be submitted to the workshop using the GECCO submission system (https://ssl.linklings.net/conferences/gecco/) and the GECCO LaTeX template.


## Important Dates:
- Submission deadline: April 14, 2023
- Notification: May 3, 2023

## Contributions: 
This workshop encourages short papers (a few pages) and invites two types of contributions:
1) Proposals of benchmark functions, which should ideally be fast to run, easy to implement, and test specific properties (e.g., invariance to a rotation of the behavioral space, alignment between the behavior space and the fitness function, number of local optima, relevance to real-world applications, etc.); for each function, the short paper will at least describe:
	- the genotype space (bounds, etc.);
	- the behavior space;
	- the fitness function.
2) Proposals of indicators to compare algorithms; for instance, the MAP-Elites paper (Mouret and Clune, 2015) introduced global performance, global reliability and opt-in reliability, but other papers used different indicators. “Confronting the challenge of quality diversity’’ (Pugh et. al. 2015) introduced the QD-score indicator often used to compare NSLC-based algorithms.

## Details and Background:



Quality Diversity (QD) algorithms find a large set of high-performing solutions to an optimization problem so that all solutions behave differently according to some behavioral metrics. This set of solutions has numerous uses, from providing users with a pool of options from which they can choose (e.g., using, e.g., aesthetics), to preparing for future adaptations in case of a change of optimization objective. In addition, QD algorithms with well-chosen behavioral dimensions can help providing stepping stones to the global optima. 

Originally proposed as Novelty Search with Local Competition (Lehman and Stanley, 2011) and MAP-Elites (Mouret and Clune, 2015), QD-based approaches now account for approximately half of submissions to the GECCO Complex Systems (CS) track. While these methods are all inspired by NSLC or MAP-Elites, new approaches introduce components of surrogate modeling (Gaier et al., 2018, best paper of the CS track), CMA-ES (Fontaine et al., 2019) or even deep-neuroevolution (Colas et al., 2020, Nilsson et al., 2021 – Best paper in NE track). With broadening interest in QD and the number and types of new proposed domains, it is becoming increasingly difficult to compare algorithms and validate implementations.

Inspired by the impact of benchmarking functions in multi-objective and black-box optimization, the objective of this workshop is twofold: (1)  to select a set of benchmark functions that capture the unique challenges posed by quality diversity and (2) to determine appropriate indicators of performance for QD algorithms (e.g., global reliance, QD-Score). Like the ZDT functions (Zitzler, Deb, Thiele) and the BBOB (Black-Box Optimization Benchmarking) workshop catalyzed research in multi and single objective evaluation, we aim at doing the same for quality diversity. 

Beyond publishing  submissions in the proceedings, the objective of this workshop is to present ideas regarding benchmarks and quality indicators to each other, and collectively submit our findings as a journal submission.Each short paper will be encouraged to showcase preliminary benchmark results with some of the published algorithms. The papers will be reviewed by the organizers of the workshop.


As a published ACM author, you and your co-authors are subject to all ACM Publications Policies (https://www.acm.org/publications/policies/toc), including ACM's new Publications Policy on Research Involving Human Participants and Subjects (https://www.acm.org/publications/policies/research-involving-human-participants-and-subjects).



## Organisers (alphabetical order)
- Antoine Cully
- Stéphane Doncieux
- Matthew Fontaine
- Adam Gaier
- Amy Hoover
- Jean-Baptiste Mouret
- Stefanos Nikolaidis
- John Rieffel
- Julian Togelius
