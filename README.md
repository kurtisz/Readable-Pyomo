# Readable-Pyomo
An interpretation layer to bring the power of [Pyomo](http://www.pyomo.org/) closer to the modelers' vernacular
## Features
* "Human" syntax for linear programs (LPs)
* Direct translation to Pyomo models
* Extensibility to full power of Pyomo / Python <sup>[1](#fullpower)</sup>
* Open infrastructure for translation to other frameworks
* Open infrastructure for implementation of other optimization model types

<a id="fullpower">[1]</a> *One of the desirable features of Pyomo is that models can be defined with the full power of Python and libraries like SciPy, among others. Readable Pyomo intends to maintain that benefit, without requiring its use.*
## Goals
This project is intended to be a functional finished product, but since this is a side project, I am also setting some goals for how it should be implemented.
### Define syntax first
The primary goal of this module is to allow for specification of LPs in a language as close to a modeler's typical syntax as possible. The language required by this project is expected to evolve, but at all phases the language should be defined first, with the framework built around it. Limitations at each phase will mold the language specification at that phase.
### Implement several examples
The best way to test this module is to implement as many example LPs as possible. This will include examples from the [Pyomo gallery](https://github.com/Pyomo/PyomoGallery/wiki) as well as optimization modeling text.
### Build as needed (Example-Driven Development?)
Rather than tackling an expansive potential set of features, the aforementioned examples will drive development in a TDD-like fashion. Instead, I intend to utilize high-level examples and implement the feature set necessary for that LP. Ongoing development will take on a "rearchitect as needed" philosophy.