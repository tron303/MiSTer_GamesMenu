import os
files = os.listdir()
for files in os.listdir():
    filename = os.path.splitext(files)[0]
    filename_old = os.path.basename(files)
    import xml.etree.ElementTree as ET
    tree = ET.parse("system.xml")
    root = tree.getroot()
    for romset in root.iter('romset'):
        romname = romset.attrib["name"]
        altname = romset.attrib["altname"] 
        if filename == romname:
           import re
           altname = re.sub('[\/:*?!"<>|]'," -", altname)
           filename_new = str(altname + '.mgl')
           #lower_case_romname = str(romname).lower()
           #print(filename,romname,altname)
           #print(altname.lower())
           print('MMMM   MMMMM   WWWWW   WWWMM   MMMMM   WWWWW')
           if altname.lower() != filename.lower():
               print("#*************#")
               print(filename,altname)
               print(filename_old,filename_new)
               os.rename (filename_old,filename_new)
           else:
               print("*############*#") 
               filename_old1 = filename_old + "1"
               print(filename_old,filename_old1)
               print(filename_old1,filename_new)
               os.rename (filename_old,filename_old1) 
               os.rename (filename_old1,filename_new) 
           print("Renaming: " + filename_old + " ---> " + filename_new)
           print("=====================================")