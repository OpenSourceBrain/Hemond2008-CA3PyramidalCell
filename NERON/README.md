### NEURON scripts for model

This folder contains files from the original model scripts [ModelDB:101629](https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=101629) and additional tester scripts (in order to create a .mep file, which against LEMS/NeuroML2 implementation could be tested).

To run the scripts, [install NEURON](https://www.neuron.yale.edu/neuron/download) and run:

    git clone https://github.com/OpenSourceBrain/Hemond2008-CA3PyramidalCell.git  # clone git repository
    cd Hemond2008-CA3PyramidalCell/NEURON
    nrnivmodl  # compile .mod files
    nrngui test_ca3pyr.hoc  # runs a simulation (single cell, current clamp) and saves data into ca3pyr.dat
