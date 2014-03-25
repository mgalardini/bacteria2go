#!/usr/bin/python

__author__ = "Marco Galardini"

import hashlib
import sys
import os
import subprocess
import logging

logger = logging.getLogger('bacteria2go.utils')

def get_dspan(oset, span=20):
    out = set()
    for k,x in oset.items():
        if len(out) == span:
            yield out
            out = set()
        out.add(x)
    if len(out) > 0:
        yield out

def get_span(oset, span=20):
    out = set()
    for x in oset:
        if len(out) == span:
            yield out
            out = set()
        out.add(x)
    if len(out) > 0:
        yield out

def mean(obj):
    return float(sum(obj))/len(obj)
    
# Thanks to @Omnifarious on StackOverflow
def hashfile(afile, hasher=hashlib.sha256(), blocksize=65536):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.hexdigest()

def runCmd(cmd, ignore_error=False):
    '''
    Run a command line command
    Returns True or False based on the exit code
    '''
    proc = subprocess.Popen(cmd,shell=(sys.platform!="win32"),
                            stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out = proc.communicate()
    return_code = proc.returncode
    if return_code != 0 and not ignore_error:
        logger.warning('Command (%s) failed w/ error %d'
                        %(cmd, return_code))
        logger.warning('%s'%str(out[1]))
                                        
    return bool(not return_code)
