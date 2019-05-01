#!/usr/bin/env python
"""***************************************************************
**  Program Name:   ZipMP3+G						                **
**  Version Number: V1.0                                        **
**  Copyright (C):	 June 15, 2009 Richard W. Allen              **
**  Date Started:   May 28, 2009                                **
**  Date Ended:     June 15, 2009                               **
**  Author:         Richardn W. Allen                           **
**  Webpage:        http://richard-allen.homelinux.com/         **
**  IDE:            IDLE 2.6.2                                  **
**  Compiler:       Python 2.6.2                                **
**  Langage:        Python 2.6.2							        **
**  License:		    GNU GENERAL PUBLIC LICENSE Version 2	       **
**		    see license.txt for for details	            **
***************************************************************"""
import os

#A class used to find and hold all the .cdg
class FilesToArchive:
    def __init__(self):
        self.filenames = []

    #Note we only look for .cdg files
    def GetFileNames(self, dir):
        """GetFileNames(dir):
        Input: File directory
        Output: None
        Side effects: Finds and stores .cdg files in
        the self.filenames variable."""
        self.filenames = []
        files = os.listdir(dir)
        for name in files:
            if name.find(".cdg") != -1:
                name = name.split('.')
                name = name[0]
                self.filenames.append(dir + '//' + name)

        print "Files found."
        print self.filenames

if __name__ == "__main__":
    files = FilesToArchive()
    files.GetFileNames(os.getcwd())

    if len(files.filenames) == 0:
        print "No Files found"
    else:
        print "Files found."
        print files.filenames
