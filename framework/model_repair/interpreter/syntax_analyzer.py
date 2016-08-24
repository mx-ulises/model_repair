"""
================================================================================
                              DESCRIPTION
================================================================================

  This Module include the lexicographical analyzer that will recognize the
  different symbols we can have in Petri Nets and CTL LoLA files.

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
  Last Update: 24-08-2016

  Date        Alias      Description
--------------------------------------------------------------------------------
  22-08-2016  ulisesma   Initial file creation
  24-08-2016  ulisesma   Get object function to get a valid string using the
                         DFA model



--------------------------------------------------------------------------------
Enumerator class for States and Input Classes
--------------------------------------------------------------------------------
"""
class StateEnum(object):
    q_err = -1
    q_0 = 0
    q_sep = 1
    q_1 = 2
    q_num = 3
    q_ident = 4

class InputEnum(object):
    invalid = -1
    separator = 0
    digit = 1
    dash = 2
    character = 3

IE = InputEnum
SE = StateEnum


"""
--------------------------------------------------------------------------------
Deterministic Finite Automata (DFA) table to manage string parsing
--------------------------------------------------------------------------------
"""

_q_0 =   {IE.separator: SE.q_sep, IE.dash: SE.q_1,     IE.digit: SE.q_num,   IE.character: SE.q_ident, IE.invalid: SE.q_err}
_sep =   {IE.separator: SE.q_err, IE.dash: SE.q_err,   IE.digit: SE.q_err,   IE.character: SE.q_err,   IE.invalid: SE.q_err}
_q_1 =   {IE.separator: SE.q_err, IE.dash: SE.q_ident, IE.digit: SE.q_num,   IE.character: SE.q_ident, IE.invalid: SE.q_err}
_num =   {IE.separator: SE.q_err, IE.dash: SE.q_ident, IE.digit: SE.q_num,   IE.character: SE.q_ident, IE.invalid: SE.q_err}
_ident = {IE.separator: SE.q_err, IE.dash: SE.q_ident, IE.digit: SE.q_ident, IE.character: SE.q_ident, IE.invalid: SE.q_err}

DFA_TABLE = {SE.q_0: _q_0, SE.q_sep: _sep, SE.q_1: _q_1, SE.q_num: _num, SE.q_ident: _ident}


"""
--------------------------------------------------------------------------------
Character class definitions
--------------------------------------------------------------------------------

Setting char input indexes
"""
CHAR_INPUT = {chr(i): -1 for i in xrange(256)}

""" Separators """
CHAR_INPUT[':'] = InputEnum.separator
CHAR_INPUT[';'] = InputEnum.separator

""" Digits """
for x in xrange(10):
    CHAR_INPUT[str(x)] = InputEnum.digit

""" Dash """
CHAR_INPUT['-'] = InputEnum.dash

""" Alphabet """
for x in xrange(ord("z") - ord("a") + 1):
    CHAR_INPUT[chr(ord("A") + x)] = InputEnum.character
    CHAR_INPUT[chr(ord("a") + x)] = InputEnum.character


"""
--------------------------------------------------------------------------------
Functions
--------------------------------------------------------------------------------
"""

def get_object(input_str):
    i = 0
    state = SE.q_0
    out_str = ""
    while i < len(input_str) and state != SE.q_err:
        symbol = input_str[i]
        state = DFA_TABLE[state][CHAR_INPUT[symbol]]
        out_str += symbol
        i += 1
    if state == SE.q_err:
        out_str = out_str[:-1]
    return out_str
