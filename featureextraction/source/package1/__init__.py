import xml.etree.ElementTree as ET
import os

if __name__ == '__main__':
    tree = ET.ElementTree(file='DrugbankTraining/abarelix_ddi.xml')
    tree.getroot()
    root = tree.getroot()
    negindex=0
    negationtags= tree.findall(".//negationtags")
    for child_of_root in root:
        #print child_of_root.tag 
        #print child_of_root.attrib
        sentence = "this is a foo bar i want to parse."
        os.popen("echo '"+ child_of_root.attrib['text']+"' > stanfordtemp.txt")
        parser_out = os.popen("lexparser.bat stanfordtemp.txt").readlines()
        bracketed_parse = " ".join( [i for i in parser_out ] )
        print bracketed_parse
        for child_of_child_root in child_of_root:
            #print child_of_child_root.tag
            #print child_of_child_root.attrib
            if child_of_child_root.tag == 'negationtags':
                negationtagstring = child_of_child_root.text
                negindex+= 1
                print negationtagstring
                cueopenpos= negationtagstring.find("<cue>")
                cueclospos= negationtagstring.find("</cue>")
                cue = negationtagstring[cueopenpos+6:cueclospos]
                print cue
                scopeopenpos= negationtagstring.find("<xcope>")
                scopeclospos= negationtagstring.find("</xcope>")
                escope = negationtagstring[scopeopenpos+8:scopeclospos]
                print escope
                for child_of_child_root in child_of_root:
                    if child_of_child_root.tag == 'pair':
                        drugid1 = child_of_child_root.attrib["e1"]
                        drugid2 = child_of_child_root.attrib["e2"]
                        if child_of_child_root.tag == 'entity':
                                entityid = child_of_child_root.attrib["id"]
                                #print entityname
                        
               
                
            
            
            

