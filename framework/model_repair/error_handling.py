"""
================================================================================
                              DESCRIPTION
================================================================================

  This document contains the error handling structures for the framework.

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
  Last Update: 31-01-2016

  Date        Alias      Description
--------------------------------------------------------------------------------
  09-01-2016  ulisesma   Initial file creation
  31-01-2016  ulisesma   Adding new CTL exception


"""

from logger import LOG


class PetriNetException(Exception):
    """ Exception used in the Petri Net modules """
    def __init__(self, message):
        LOG.error(message)


class CTLException(Exception):
    """ Exception used in the CTL and Model Checking modules """
    def __init__(self, message):
        LOG.error(message)


class PetriNetInterpreterException(Exception):
    """ Exception used in the Petri net interpreter module """
    def __init__(self, message):
        LOG.error(message)
