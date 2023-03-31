# proto-top-k-early-termination
Early Termination Top-K prototype

The goal of the projet is to make a prototype inspired by the sage engine to build and try our algorithm on a benchmark.

The algorithm has the particularity to use early termination on top-k request to optimise the time need to complete top-k request.

<!-- Tech used -->
## Tech used
 [HDT](https://www.rdfhdt.org/) for the data structure of the triples

 Library [HDT](https://pypi.org/project/hdt/) for the python implementation of HDT

 [Python](https://python.org/) for the implementation of the algorithm

## Usage

To create ntriples files from csv file use ntriples_creation.py with a file data.csv containing your triples.

To convert .nt files in .hdt files use this [tool](https://github.com/rdfhdt/hdt-java) and use the following command:

`./rdf2hdt.sh data/test.nt data/test.hdt`
