#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
import os
import random
import string

__author__ = "Damian Kęska"
__license__ = "LGPLv3"
__maintainer__ = "Damian Kęska"
__copyright__ = "Copyleft by Panthera Team"

# get current working directory to include local files (debugging mode)
t = sys.argv[0].replace(os.path.basename(sys.argv[0]), "") + "src/"

if os.path.isdir(t):
    sys.path.append(t)
    
import pantheradesktop.kernel

class buildZipArgs (pantheradesktop.argsparsing.pantheraArgsParsing):
    """ 
        Arguments parser extension
    """
    
    description = "Panthera ZIP/Targz archive builder"
    branch = "master"
    zipPath = None
    targzPath = None
    
    def setBranch(self, branchName):
        """ Set git branch """
    
        self.branch = branchName
        
    def zipPathSet(self, path):
        """ Set zip save path """
    
        self.zipPath = path
        
    def targzPathSet(self, path):
        """ Set tar.gz save path """
        
        self.targzPath = path

    def addArgs(self):
        """ Add application command-line arguments """
    
        self.createArgument('--branch', self.setBranch, '', 'Set git branch')
        self.createArgument('--zip', self.zipPathSet, '', 'Set zip path')
        self.createArgument('--targz', self.targzPathSet, '', 'Set tar.gz path')
        
class buildZip(pantheradesktop.kernel.pantheraClass):
    """ App main class"""
    
    gitAddress = "https://github.com/Panthera-Framework/panthera"
    
    def randomString(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    
    def main(self):
        if self.panthera.argsParser.zipPath == None and self.panthera.argsParser.targzPath == None:
            print("You must specify a zip or tar.gz archive")
            sys.exit(0)
            
        tmpDir = "/tmp/"+self.randomString()
        
        while os.path.isfile(tmpDir):
            tmpDir = "/tmp/"+self.randomString()
            
        self.panthera.logging.output("Teporary directory: "+tmpDir, "buildZip")
            
        os.system("mkdir "+tmpDir)
        os.system("git clone -b "+self.panthera.argsParser.branch+" "+self.gitAddress+" "+tmpDir)
        os.chdir(tmpDir)
        os.system("chmod +x "+tmpDir+"/install.sh")
        os.system(tmpDir+"/install.sh")
        os.system("rm -rf "+tmpDir+"/.git") # cleanup
        
        if self.panthera.argsParser.zipPath:
            self.panthera.logging.output("Creating zip file "+self.panthera.argsParser.zipPath, "buildZip")
            os.system("zip -r "+self.panthera.argsParser.zipPath+" . --exclude='*.git/*'")
            
        if self.panthera.argsParser.targzPath:
            self.panthera.logging.output("Creating tar.gz file "+self.panthera.argsParser.targzPath, "buildZip")
            os.system("tar -zcvf "+self.panthera.argsParser.targzPath+" * --exclude='*.git/*'")
            
        os.system("rm -rf "+tmpDir)
       
# Application beigns here

# initialize kernel
kernel = pantheradesktop.kernel.pantheraDesktopApplication()
kernel.appName = "panthera-buildZip"
kernel.coreClasses['gui'] = None # disable gui
kernel.coreClasses['argsparsing'] = buildZipArgs
kernel.initialize(quiet=True)
kernel.main(buildZip)
