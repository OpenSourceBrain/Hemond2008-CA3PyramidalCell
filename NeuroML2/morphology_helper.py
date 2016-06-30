# -*- coding: utf-8 -*-
""" 
    Helper method to handle Ca++ dynamics in the pyramidal cell model of Hemond 2008 (implemented by Migliore)
    1) the code deletes numberInternalDivisions from annotation (makes it a valid nml file)
    2) iterates over dendrites and apical_dendrites and calculate the average diam of segments (the depth of Ca++ shell is changed (from hoc level) according to the diameter in the original code)
    Authors: András Ecker, Padraig Gleeson
"""

import neuroml

import neuroml.loaders as loaders
import neuroml.writers as writers

import numpy as np


def helper_morphology(morph_file):   

    doc = loaders.NeuroMLLoader.load(morph_file)
    print("Loaded morphology file from: %s"%morph_file)
    
    dSegs = {}; dSegs["apical_dendrite"] = []; dSegs["dendrite"] = []
    # iterates over segment groups
    for segGroup in doc.cells[0].morphology.segment_groups:
        # deletes numberInternalDivisions from annotation (will be valid -> it will be possible to visualize it on OSB)
        if segGroup.annotation:
            segGroup.annotation = None
       
        # gets the seg.ids of segmentGroups (dendrite_group and apical_dendrite_group)
        if segGroup.neuro_lex_id:
            if segGroup.id[:segGroup.id.rfind('_')] == "apical_dendrite":
                for member in segGroup.members:
                    dSegs["apical_dendrite"].append(member.segments)
            elif segGroup.id[:segGroup.id.rfind('_')] == "dendrite":
                for member in segGroup.members:
                    dSegs["dendrite"].append(member.segments)
    
    
    dSegDiams = {}; dSegDiams["apical_dendrite"] = []; dSegDiams["dendrite"] = []
    # iterates over segments and gets the diameter of the segment (distal.diam)
    for seg in doc.cells[0].morphology.segments:
        d = seg.distal.diameter
        if seg.id in dSegs["apical_dendrite"]:
            dSegDiams["apical_dendrite"].append(d)
        elif seg.id in dSegs["dendrite"]:
            dSegDiams["dendrite"].append(d)
            

    capool = ''
    capool += '\t<HemondCaConcentrationModel id="capool_diam_%s" ion="ca" decayConstant="100ms" restingConc="5e-5mM" shellThickness="%gum"/>\n\n'%(str(np.mean(dSegDiams["dendrite"])).replace('.', '_'), np.mean(dSegDiams["dendrite"])/2)
    capool += '\t<HemondCaConcentrationModel id="capool_diam_%s" ion="ca" decayConstant="100ms" restingConc="5e-5mM" shellThickness="%gum"/>\n\n'%(str(np.mean(dSegDiams["apical_dendrite"])).replace('.', '_'), np.mean(dSegDiams["apical_dendrite"])/2)

    # write out to file... afterwards copy them (manually) to capool.nml TODO: automate this... 
    capools = open("capools.txt", 'w')
    capools.write(capool)
    capools.close()

    writers.NeuroMLWriter.write(doc, morph_file)
    print("Saved modified file to: " + morph_file)


if __name__ == "__main__":

    helper_morphology("ca3pyr.cell.nml")


