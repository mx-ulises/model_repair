"""
================================================================================
                              DESCRIPTION
================================================================================

  This file contains the logger configuration. It should be inported as follows:

      from mr_logger import LOG

  and it should be used as:

      LOG.info("This is an info message")
      LOG.error("This is an error message")

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
  Last Update: 09-01-2016

  Date        Alias      Description
--------------------------------------------------------------------------------
  11-01-2016  ulisesma   Initial file creation


"""

import logging

FILE_NAME = "model_repair_2.log"
TAGS = "[%(asctime)s][%(filename)s:%(lineno)s][%(levelname)s]"
FORMAT = "{0}:%(message)s".format(TAGS)

LOG = logging.getLogger('model_repair_2')
hdlr = logging.FileHandler(FILE_NAME)
formatter = logging.Formatter(FORMAT)
hdlr.setFormatter(formatter)
LOG.addHandler(hdlr)
LOG.setLevel(logging.INFO)
