# -*- coding: utf-8 -*-
""" 
    Helper method to handle Ca++ dynamics in the pyramidal cell model of Hemond 2008 (implemented by Migliore)
    1) the code deletes numberInternalDivisions from annotation (makes it a valid nml file)
    2) iterates over segments and creates new segment groups based on diameter (the depth of Ca++ shell is changed (from hoc level) according to the diameter in the original code)
    Authors: András Ecker, Padraig Gleeson
"""

import neuroml

import neuroml.loaders as loaders
import neuroml.writers as writers


def helper_morphology(morph_file):   

    doc = loaders.NeuroMLLoader.load(morph_file)
    print("Loaded morphology file from: %s"%morph_file)
    
    # iterates over segment groups and deletes numberInternalDivisions from annotation (will be valid -> it will be possible to visualize it on OSB)
    for segGroup in doc.cells[0].morphology.segment_groups:
        if segGroup.annotation:
            segGroup.annotation = None

            
    # iterates over segments and gets the diameter of the segment (distal.diam)
    dSegDiams = {}
    dSegGroupDiams = {}
    capool = ''
    for seg in doc.cells[0].morphology.segments:
        d = seg.distal.diameter
        if d not in dSegDiams:
            capool += '\t<HemondCaConcentrationModel id="capool_diam_%s" ion="ca" decayConstant="100ms" restingConc="5e-5mM" shellThickness="%gum"/>\n\n'%(str(d).replace('.', '_'), d/2)
            dSegDiams[d] = 1
            dSegGroupDiams[d] = []
            dSegGroupDiams[d].append(seg.id)
        else:
            dSegDiams[d] += 1
            dSegGroupDiams[d].append(seg.id)
            
       
    # write out to file... afterwards copy them (manually) to capool.nml TODO: automate this... 
    capools = open("capools.txt", 'w')
    capools.write(capool)
    capools.close()
    
    
    # create segment groups from the segments with same diameter
    for d, segList in dSegGroupDiams.iteritems():
        segGroup = neuroml.SegmentGroup(id="diam_%s"%str(d).replace('.', '_'),
                                        notes="all segments with diam:%g (for implementing Ca++ dynamics)"%d)
        
        for id in segList:
            if id not in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:  # these are the seg IDs of segGroup axon_0, which doesn't have Ca++ dynamics (<- yeah I know that it's ugly... András) 
                member = neuroml.Member(segments=id)
                segGroup.members.append(member)
                
        doc.cells[0].morphology.segment_groups.append(segGroup)
        print ("segment group added with diam:%g"%d)


    writers.NeuroMLWriter.write(doc, morph_file)
    print("Saved modified file to: " + morph_file)


if __name__ == "__main__":

    helper_morphology("ca3pyr.cell.nml")


