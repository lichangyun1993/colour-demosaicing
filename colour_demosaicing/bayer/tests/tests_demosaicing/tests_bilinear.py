# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines unit tests for :mod:`colour_demosaicing.bayer.demosaicing.bilinear`
module.
"""

from __future__ import division, unicode_literals

import numpy as np
import os
import unittest

import colour
from colour_demosaicing.bayer import demosaicing_CFA_Bayer_bilinear

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['RESOURCES_DIRECTORY',
           'TestDemosaicing_CFA_Bayer_bilinear']

RESOURCES_DIRECTORY = os.path.join(
    os.path.dirname(__file__), '..', 'resources')


class TestDemosaicing_CFA_Bayer_bilinear(unittest.TestCase):
    """
    Defines
    :func:`colour_demosaicing.bayer.demosaicing.bilinear.demosaicing_CFA_Bayer_bilinear`  # noqa
    definition unit tests methods.
    """

    def test_demosaicing_CFA_Bayer_bilinear(self):
        """
        Tests
        :func:`colour_demosaicing.bayer.demosaicing.bilinear.demosaicing_CFA_Bayer_bilinear`  # noqa
        definition.
        """

        for pattern in ('RGGB', 'BGGR', 'GRBG', 'GBRG'):
            np.testing.assert_almost_equal(
                demosaicing_CFA_Bayer_bilinear(
                    colour.read_image(
                        str(os.path.join(
                            RESOURCES_DIRECTORY,
                            'Lighthouse_CFA_{0}.exr'.format(pattern)))),
                    pattern),
                colour.read_image(
                    str(os.path.join(
                        RESOURCES_DIRECTORY,
                        'Lighthouse_Bilinear_{0}.exr'.format(pattern)))),
                decimal=7)


if __name__ == '__main__':
    unittest.main()