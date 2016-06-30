from pyneuroml.neuron import export_to_neuroml2
# from pyneuroml.neuron.nrn_export_utils import clear_neuron

export_to_neuroml2("../NERON/test_ca3pyr.hoc", 
                   "ca3pyr.cell.nml", 
                   includeBiophysicalProperties=True,
                   known_rev_potentials={'cal':0, 'can':0, 'cat':0})

