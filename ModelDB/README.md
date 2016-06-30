### Original NEURON scripts for model

These files are the original model scripts for use with the [NEURON simulator](https://www.neuron.yale.edu/neuron/) as [submitted to ModelDB](https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=101629).

To run the scripts, [install NEURON](https://www.neuron.yale.edu/neuron/download) and run:

    git clone https://github.com/OpenSourceBrain/Hemond2008-CA3PyramidalCell.git  # clones the git repository
    cd Hemond2008-CA3PyramidalCell/ModelDB
    nrnivmodl  # compile .mod files
    nrngui ca3b-cell1zr.hoc  # runs a simulation
    select a figure (to reproduce) by clicking on a figure name (fig 9b is implemented in NeuroML2)

-------------------------------------------------------------------------------------------------------------------

Authors summary:

In the paper, this model was used to identify how relative differences in K+ conductances, specifically KC, KM, & KD, between cells contribute to the different characteristics of the three types of firing patterns observed experimentally.

> Questions on how to use this model should be directed to michele.migliore@pa.ibf.cnr.it

> Bugs fixed: Added the value for the I-h reversal potential (ehd_hd = -30), which was missed from the original hoc file used to generate Fig.9. Minor adjustements of the current injections were needed to obtain the same patterns.  Apr-14-2008, M.Migliore
