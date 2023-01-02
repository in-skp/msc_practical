"""
Created on Thu Dec 29

@author: Santosh Parse
@program name: Logging
"""
import sys
import os
import logging
import uuid
import shutil
import time

if sys.platform == 'linux':
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'

sCompanies=['01-Vermeulen','02-Krennwallner','03-Hillman','04-Clark']
sLayers=['01-Retrieve','02-Assess','03-Process','04-Transform','05-Organise','06-Report']
sLevels=['debug','info','warning','error']

for sCompany in sCompanies:
    sFileDir=Base + '/' + sCompany
    if not os.path.exists(sFileDir):
        os.makedirs(sFileDir)
    for sLayer in sLayers:
        log = logging.getLogger() # root logger
        for hdlr in log.handlers[:]: # remove all old handlers
            log.removeHandler(hdlr)
        sFileDir=Base + '/' + sCompany + '/' + sLayer + '/Logging'
        if os.path.exists(sFileDir):
            shutil.rmtree(sFileDir)
        time.sleep(2)
        if not os.path.exists(sFileDir):
            os.makedirs(sFileDir)
        skey=str(uuid.uuid4())
        sLogFile=Base + '/' + sCompany + '/' + sLayer + '/Logging/Logging_'+skey+'.log'
        print('Set up:',sLogFile)

        # setup up logging to file
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename=sLogFile,
                            filemode='w')

        # define a handler, which writes all messages to sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)

        # set a format for console use
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')

        # activate the handler to use this format
        console.setFormatter(formatter)

        # add the handler to the root logger
        logging.getLogger('').addHandler(console)

        # Test root loggin
        logging.info('Practical Data Science is fun!.')

        # Test all other levels
        for sLevel in sLevels:
            sApp='Application-'+ sCompany + '-' + sLayer + '-' + sLevel
            logger = logging.getLogger(sApp)
            if sLevel == 'debug':
                logger.debug('Practical Data Science logged a debugging message.')
            if sLevel == 'info':
                logger.info('Practical Data Science logged information message.')
            if sLevel == 'warning':
                logger.warning('Practical Data Science logged a warning message.')
            if sLevel == 'error':
                logger.error('Practical Data Science logged an error message.')