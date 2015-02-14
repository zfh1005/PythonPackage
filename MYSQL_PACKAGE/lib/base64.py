#! /usr/bin/env python

"""RFC 3548: Base16, Base32, Base64 Data Encodings"""

import re
import struct
import binascii


__all__ = [
    # Legacy interface exports traditional RFC 1521 Base64 encodings
    'encode', 'decode', 'encodestring', 'decodestring',
    # Generalized interface for other encodings
    'b64encode', 'b64decode', 'b32encode', 'b32decode',
    'b16encode', 'b16decode',
    # Standard Base64 encoding
    'standard_b64encode', 'standard_b64decode',
    # Some common Base64 alternatives.  As referenced by RFC 3458, see thread
    # starting at:
    #
    # http://zgp.org/pipermail/p2p-hackers/2001-September/000316.html
    'urlsafe_b64encode', 'urlsafe_b64decode',
    ]

_translation = [chr(_x) for _x in range(256)]
EMPTYSTRING = ''


def _translate(s, altchars):
    translation = _translation[:]
    for k, v in altchars.items():
        translation[ord(k)] = v
    return s.translate(''.join(translation))



# Base64 encoding/decoding uses binascii

def b64encode(s, altchars=None):
    """Encode a string using Base64.

    s is the string to encode.  Optional altchars must be a string of at least
    length 2 (additional characters are ignored) which specifies an
    alternative alphabet for the '+' and '/' characters.  This allows an
    application to e.g. generate url or filesystem safe Base64 strings.

    The encoded string is returned.
    """
    # Strip off the trailing newline
    encoded = binascii.b2a_base64(s)[:-1]
    if altchars is not None:
        return _translate(encoded, {'+': altchars[0], '/': altchars[1]})
    return encoded


def b64decode(s, altchars=None):
    """Decode a Base64 encoded string.

    s is the string to decode.  Optional altchars must be a string of at least
    length 2 (additional characters are ignored) which specifies the
    alternative alphabet used instead of the '+' and '/' characters.

    The decoded string is returned.  A TypeError is raised if s were
    incorrectly padded or if there are non-alphabet characters present in the
    string.
    """
    if altchars is not None:
        s = _translate(s, {altchars[0]: '+', altchars[1]: '/'})
    try:
        return binascii.a2b_base64(s)
    except binascii.Error, msg:
        # Transform this exception for consistency
        raise TypeError(msg)


def standard_b64encode(s):
    """Encode a string using the standard Base64 alphabet.

    s is the string to encode.  The encoded string is returned.
    """
    return b64encode(s)

def standard_b64decode(s):
    """Decode a string encoded with the standard Base64 alphabet.

    s is the string to decode.  The decoded string is returned.  A TypeError
    is raised if the string is incorrectly padded or if there are non-alphabet
    characters present in the string.
    """
    return b64decode(s)

def urlsafe_b64encode(s):
    """Encode a string using a url-safe Base64 alphabet.

    s is the string to encode.  The encoded string is returned.  The alphabet
    uses '-' instead of '+' and '_' instead of '/'.
    """
    return b64encode(s, '-_')

def urlsafe_b64decode(s):
    """Decode a string encoded with the standard Base64 alphabet.

    s is the string to decode.  The decoded string is returned.  A TypeError
    is raised if the string is incorrectly padded or if there are non-alphabet
    characters present in the string.

    The alphabet uses '-' instead of '+' and '_' instead of '/'.
    """
    return b64decode(s, '-_')

