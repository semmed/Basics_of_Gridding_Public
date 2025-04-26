## This file implements a bathymetry class - it also contains functions that construct Bathymetry objects and returns them

# Semme J. Dijkstra 2025 04 10


import os
from datetime import datetime, timezone, timedelta
import numpy as np


# Construct a bathymetry object by reading a file - the object may just hold the meta data if so desired - this is achieved by 
# using the 'meta' or 'header' arguments and is the case by default 

class Bathymetry:
    """A Class for handling simple bathymetry data"""
    
    def __init__(self, path, how, file_type = ' '):
        
        if not (file_type.lower() == 'bathy_sjd'):
            raise RuntimeError('Bathymetry.__init__: Not currently implemented for : ' + file_type)

        self.file_type = file_type
        self.path = path
            
        # Default meta data by default for geodetic coordinates, with ellipsoidal elevations in m, relative to ITRF 2014
        self.metadata = {}
        self.metadata['horizontal units of measurement:'] = 'degrees'
        self.metadata['vertical units of measurement:'] = 'meters'
        self.metadata['projected coordinate units:'] = 'NA'
        self.metadata['geoid name:'] = 'NA'
        self.metadata['horizontal datum EPSG code:'] = '7913'
        self.metadata['vertical datum: EPSG code:'] = '7913'
        self.metadata['time basis:'] = 'NA'
        self.metadata['proj projection string:'] = 'NA'
        
        # if a path was provide then read the data
       
        if not self.path == '': 
            self.read( how)
            
            
    def read(self, how):
        # This method reads a data file at the given path. If it does not find the file at the path it will check the 
        # mydata folder as that is the default location
        
        if not (how.lower() == 'header' or  \
                    how.lower() == 'meta'):
            raise RuntimeError('Bathymetry.__init__: Not currently implemented for : ' + how)
        
        try:
            # Try in the path location
            bathy_file = open(self.path)
        except:
            head, tail = os.path.split(self.path)
            self.path = os.path.join( os.getcwd(), 'mydata', tail)
            try:
                bathy_file = open(self.path)
            except:
                raise RuntimeError('Bathymetry.read: file ' + tail + ' not found')
            
        # We now have an open file - For now read the entire file - later this should just be the header
        
        print( 'Opened file: ' + self.path)
        bathy_content = bathy_file.read()
        bathy_file.close
        
        # Break the file contents in a set of lines
        
        bathy_lines = bathy_content.splitlines()
        
        # Read the header
        n_header_lines = 0
        for line in bathy_lines:
            n_header_lines += 1
            
            # If the end of the header is reached break out of the loop
            if line == 'EOH':
                break
                
            # Find the metadata
            if 'horizontal units of measurement:'.lower() in line.lower():
                self.metadata['horizontal units of measurement:'] = line.split()[-1]
            elif 'vertical units of measurement:'.lower() in line.lower():
                self.metadata['vertical units of measurement:'] = line.split()[-1]
            elif 'projected coordinate units: '.lower() in line.lower():
                self.metadata['projected coordinate units:'] = line.split()[-1]
            elif 'geoid name:'.lower() in line.lower():
                self.metadata['geoid name:'] = line.split()[-1]
            elif 'horizontal datum EPSG code:'.lower() in line.lower():
                self.metadata['horizontal datum EPSG code:'] = line.split()[-1]
            elif 'vertical datum: EPSG code:'.lower() in line.lower():
                self.metadata['vertical datum: EPSG code:'] = line.split()[-1]
            elif 'horizontal units of measurement:'.lower() in line.lower():
                self.metadata['time basis:'] = line.split()[-1]
            elif 'proj projection string:'.lower() in line.lower():
                self.metadata['proj projection string:'] = line.split()[-1]
            else:
                self.metadata[' '.join(line.lower().split()[0:-1])] = line.split()[-1]
                        
    def __str__(self):
        s = ''
        
        keys_meta = self.metadata.keys()
        for key in keys_meta:
            s += key + ' ' + self.metadata[key] + '\n'
        return s
        

def ReadBathy( path, how = 'header'):
    bathymetry = Bathymetry(path, how, file_type = 'bathy_sjd')
    return bathymetry
