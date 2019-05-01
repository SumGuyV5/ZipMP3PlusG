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
import zipfile

from FilesToArchive import FilesToArchive

class ArchiveFiles:
    def __init__(self):
        self.command = "7za a -tzip "

    def Archive(self, filestoarchive):
        """Archive(filestoarchive):
        Input: Files to archive
        Output: None
        Side effects: zips the .cdg and .mp3 files into
        the same zip file useing pythons ZipFile object."""
        for files in filestoarchive.filenames:
            zipf = zipfile.ZipFile(files + ".zip", "w")

            zipf.write(files + '.cdg', os.path.basename(files) + '.cdg', zipfile.ZIP_DEFLATED)
            zipf.write(files + '.mp3', os.path.basename(files) + '.mp3', zipfile.ZIP_DEFLATED)

            zipf.close()
            

    """def Archive(self, filestoarchive):
        ""Archive(filestoarchive):
        Input: Files to archive
        Output: None
        Side effects: zips the .cdg and .mp3 file into
        the same zip file useing 7zip""
        for files in filestoarchive.filenames:
            command = self.command
            command = command + '\"' + files + '.zip\"' + ' \"' + files

            commandcdg = command + '.cdg\"'
            commandmp3 = command + '.mp3\"'

            os.system(commandcdg)
            os.system(commandmp3)"""

if __name__ == "__main__":
    files = FilesToArchive()
    files.GetFileNames(os.getcwd())
    
    archive = ArchiveFiles()
    archive.Archive(files)

    if len(files.filenames) == 0:
        print "No Files found"
    else:
        print "Files found."
        print files.filenames
