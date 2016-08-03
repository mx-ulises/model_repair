"""
================================================================================
                              DESCRIPTION
================================================================================

  This module perform calls to the command line to run external programs.

================================================================================
                              MAINTAINERS
================================================================================

  This section contains all the maintainers primary information to get track of
  the contributors to this code in the file. The maintainer's list contains a
  maintainer alias (required), his name (optional) and contact mails (one
  required).


  Alias     Name              Mail
--------------------------------------------------------------------------------
  ulisesma  Ulises Martinez   ulises.martinezaraiza.mx@ieee.org
                              umartinez@gdl.cinvestav.mx


================================================================================
                              CHANGE LOG
================================================================================

      Version: 0.1
  Last Update: 27-03-2016

  Date        Alias      Description
--------------------------------------------------------------------------------
  27-03-2016  ulisesma   Runner module to perform command line calls

"""

import subprocess

from logger import LOG

def run(command):
    cmd_string = " ".join(command)
    LOG.info("Runnin command \"{0}\"".format(cmd_string))
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ret = process.wait()
    stdout, stderr = process.communicate()
    LOG.info("RC: \"{0}\"".format(ret))
    LOG.info("STDOUT: \"{0}\"".format(stdout))
    LOG.info("STDERR: \"{0}\"".format(stderr))
    return (ret, stdout, stderr)
