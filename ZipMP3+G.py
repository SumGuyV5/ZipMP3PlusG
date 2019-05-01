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
import os #used to walk the systems file structure
import sys
sys.path.append('Module.zip')

from Module.FilesToArchive import FilesToArchive
from Module.ArchiveFiles import ArchiveFiles

#import Module.FilesToArchive as FilesTo
#import Module.ArchiveFiles as AF

if __name__ == "__main__":
        
        filesA = FilesToArchive()
        archive = ArchiveFiles()

        for path, dirs, files in os.walk(os.getcwd()):
                filesA.GetFileNames(path)
                archive.Archive2(filesA)
