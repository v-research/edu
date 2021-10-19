#!/usr/bin/python3

import sys
import os
import re 
import xml.etree.ElementTree as ET
import pprint

def get_components_from_xmi(xmi,cps_spec_name,schema="{http://schema.omg.org/spec/XMI/2.1}",):
    components_flows={}
    tree = ET.parse(xmi)
    root = tree.getroot()

    type_of_block={}
    dict_of_block={}
    flows={}

    c = 1


    for child in root:
        if(child.tag == "packagedElement"):
            if(child.attrib[schema+'type'] == "uml:Class"):
                type_of_block[child.attrib[schema + 'id']] = child.attrib['name']

    #print(type_of_block)

    for child in root:
            if(child.tag == "packagedElement" and child.attrib['name'] == cps_spec_name):
                for innerchild in child:
                    #print(innerchild.tag, innerchild.attrib)
                    if (innerchild.attrib[schema + 'type'] == "uml:Node"):
                        for attribute in innerchild:
                            #print(attribute.attrib)
                            dict_of_block[attribute.attrib[schema + 'id']]={'name':attribute.attrib['name'],'type':type_of_block.get(attribute.attrib['type'])}

                    elif (innerchild.attrib[schema + 'type'] == "uml:InstanceSpecification"):
                        if('classifier' in innerchild.attrib.keys()):
                            dict_of_block[innerchild.attrib[schema + 'id']]={'name':innerchild.attrib['name'],'type':type_of_block.get(innerchild.attrib['classifier'])}
                        else:
                            dict_of_block[innerchild.attrib[schema + 'id']] = {'name': innerchild.attrib['name'],'type': 'other'}
                        #print(innerchild.tag, innerchild.attrib)

                    elif (innerchild.attrib[schema + 'type'] == "uml:InformationFlow"):
                        #print(innerchild.attrib.keys())
                        #s=str("'name'")
                        #print(s)

                        if ('name' in innerchild.attrib.keys()):
                            flows[c]={'source':innerchild.attrib['informationSource'],'target':innerchild.attrib['informationTarget'], 'information':innerchild.attrib['name']}
                        else:
                            flows[c] = {'source': innerchild.attrib['informationSource'],'target': innerchild.attrib['informationTarget'],'information': None}
                        c+=1
    #print(dict_of_block)
    #print(flows)


    components_flows['blocks']=dict_of_block
    components_flows['flows']=flows
    return components_flows



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Devi passare due parametri allo script!")
        print("Sto uscendo...")
        sys.exit()
    path = os.path.join("./", "output")
    if not os.path.exists(path):
        os.mkdir(path)
    xmi= sys.argv[1]
    spec = sys.argv[2]
    components_flows=get_components_from_xmi(xmi,spec)
    blocks=components_flows['blocks']
    flows=components_flows['flows']

    f = open(os.path.join(path, spec + "_struct_V2.txt"), "w+")

    pp = pprint.PrettyPrinter(indent=0, stream=f)


    f.write("Blocks:\n")
    pp.pprint(blocks)
    f.write("\nFlows:\n")
    pp.pprint(flows)
    f.close()