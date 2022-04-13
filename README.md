# Probabilistic LCA - Server

This is part of a Master of Engineering dissertation for the program Integrated Computational Design at _Technische Hochschule Ostwestfalen-Lippe_.

## Goal

Early phase LCA based on a structured underspecification of materials and assemblies 
- to give the chance to get an idea of the environmental impacts very early in the design phase but also 

- address uncertainty and guide the Life Cycle Assessment by evaluating significance of each assembly in the design's total impact. 

A lot of work has been done in the past years researching ways to underspecify LCA in order to make it more viable in terms of time and cost. Ultimately, this means more chances an LCA will be done for more projects, and less total embodied and use stage carbon for the whole industry. The  _MIT Concrete Sustainability Hub_ has published several studies of this method. (Streamlining the Life Cycle Assessment of Buildings by Structured Under-Specification and Probabilistic Triage).

# Server
(this app)

## Why?
This app encapsulates the core functionality of an LCA calculator in a Web server. We have gone to the trouble of doing this because we believe that this will make it easier to escalate it to different platforms. Instead of rewriting the whole program, to work specifically with certain design programs - this allows the functionality to be reused in other programs, as long as they can access and send http requests. 

We chose to do the server in python because it was quick to iterate, the libraries vailable and because this is part of a learning exercise. 

## Libraries used

Pandas

Numpy

Scipy

Flask


## References

- Paolo Tecchio, Jeremy Gregory, Elsa Olivetti, Randa Ghattas, Randolph Kirchain, (2018) Streamlining the Life Cycle Assessment of Buildings by Structured Under-Specification and Probabilistic Triage




