# Introduction

Quality-Diversity optimization (or illumination) is a new type of evolutionary algorithm that bridges this gap by generating large collections of diverse solutions that are all high-performing. This concept was introduced by the ``Generative and Developmental Systems`` community between 2011 (Lehman & Stanley, 2011) and 2015 (Mouret & Clune, 2015) with the ``Novelty Search with Local Competition`` and ``MAP-Elites`` evolutionary algorithms. The main differences with multi-modal optimization algorithms are that (1) Quality Diversity typically works in the behavioral space (or feature space), and not in the genotypic space, and (2) Quality Diversity attempts to fill the whole behavior space, even if the niche is not a peak in the fitness landscape. In less than 4 years, about 70 papers have been written about quality diversity, many of them in the GECCO community (a non exhaustive list is provided as appendix).

The collections of solutions obtained by Quality Diversity algorithms open many new applications for evolutionary computation. In robotics, it was used to create repertoires of behaviors (Cully & Mouret, 2016), to allow robots to adapt to damage in a few minutes (Cully & et al. 2015); in engineering, it can be used to propose a diversity of optimized aerodynamic shapes (Gaier & et al., 2018); they were also recently used in video games (Khalifa & et al., 2018) and for Workforce Scheduling and Routing Problems (WSRP) (Urquhart & Hart, 2018).


# List of papers
### 2020

### 2019

### 2018

### 2017

### 2016

### 2015

### 2014

### 2013

### 2012

### 2011

<details><summary> 
**Abandoning objectives: Evolution through the search for novelty alone**
</summary> 

> #### Abstract:
>> In evolutionary computation, the fitness function normally measures progress towards an objective in the search space, effectively acting as an objective function. Through deception, such objective functions may actually prevent the objective from being reached. While methods exist to mitigate deception, they leave the underlying pathology untreated: Objective functions themselves may actively misdirect search towards dead ends. This paper proposes an approach to circumventing deception that also yields a new perspective on open-ended evolution: Instead of either explicitly seeking an objective or modeling natural evolution to capture open-endedness, the idea is to simply search for behavioral novelty. Even in an objective-based problem, such novelty search ignores the objective. Because many points in the search space collapse to a single behavior, the search for novelty is often feasible. Furthermore, because there are only so many simple behaviors, the search for novelty leads to increasing complexity. By decoupling open-ended search from artificial life worlds, the search for novelty is applicable to real world problems. Counterintuitively, in the maze navigation and biped walking tasks in this paper, novelty search significantly outperforms objective-based search, suggesting the strange conclusion that some problems are best solved by methods that ignore the objective. The main lesson is the inherent limitation of the objective-based paradigm and the unexploited opportunity to guide search through other means.
>
> #### Links
> [Paper](http://eplex.cs.ucf.edu/papers/lehman_ecj11.pdf), [source-code](http://eplex.cs.ucf.edu/software/NoveltySearchC++.zip), [Webpage](http://eplex.cs.ucf.edu/noveltysearch/userspage/)
>
> #### Bibtex
> ```		
> @article{lehman2011abandoning,
> title={Abandoning objectives: Evolution through the search for novelty alone},
>  author={Lehman, Joel and Stanley, Kenneth O},
>  journal={Evolutionary computation},
>  volume={19},
>  number={2},
>  pages={189--223},
>  year={2011},
>  publisher={MIT Press}	}
> ```
  
---
</details>


<details><summary> 
**Evolving a diversity of virtual creatures through novelty search and local competition**
</summary> 

> #### Abstract:
>>An ambitious challenge in artificial life is to craft an evolutionary process that discovers a wide diversity of welladapted virtual creatures within a single run. Unlike in nature, evolving creatures in virtual worlds tend to converge to a single morphology because selection therein greedily rewards the morphology that is easiest to exploit. However, novelty search, a technique that explicitly rewards diverging, can potentially mitigate such convergence. Thus in this paper an existing creature evolution platform is extended with multi-objective search that balances drives for both novelty and performance. However, there are different ways to combine performance-driven search and novelty search. The suggested approach is to provide evolution with both a novelty objective that encourages diverse morphologies and a local competition objective that rewards individuals outperforming those most similar in morphology. The results in an experiment evolving locomoting virtual creatures show that novelty search with local competition discovers more functional morphological diversity within a single run than models with global competition, which are more predisposed to converge. The conclusions are that novelty search with local competition may complement recent advances in evolving virtual creatures and may in general be a principled approach to combining novelty search with pressure to achieve.

>
> #### Links
> [Paper](https://pdfs.semanticscholar.org/6d45/9da1ff73ec7225e92842341605e2b90d0da2.pdf)
> #### Bibtex
> ```		
> @inproceedings{lehman2011evolving,
>   title={Evolving a diversity of virtual creatures through novelty search and local competition},
>   author={Lehman, Joel and Stanley, Kenneth O},
>   booktitle={Proceedings of the 13th annual conference on Genetic and evolutionary computation},
>   pages={211--218},
>   year={2011},
>   organization={ACM}
> }
> ```
