# -*- coding: utf-8 -*-
# Copyright 2019 The LumiSpy developers
#
# This file is part of LumiSpy.
#
# LumiSpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# LumiSpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with LumiSpy.  If not, see <http://www.gnu.org/licenses/>.

"""Signal class for cathodoluminescence spectral data acquired in STEM.

"""

from lumispy.signals.cl_spectrum import CLSpectrum
from hyperspy._signals.lazy import LazySignal


class CLSTEMSpectrum(CLSpectrum):

    _signal_type = "CL_STEM"

    pass


class LazyCLSTEMSpectrum(LazySignal, CLSTEMSpectrum):

    _lazy = True

    pass
