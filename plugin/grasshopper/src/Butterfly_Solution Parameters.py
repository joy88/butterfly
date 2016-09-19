# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Set parameters for runDict

    Args:
        _startTime_: Start timestep (default: 0)
        _endTime_: End timestep (default: 1000)
        _writeInterval_: Number of intervals between writing the results (default: 100)
        _writeCompression_: Set to True if you want the results to be compressed
            before being written to your machine (default: False).
    Returns:
        controlDict: Butterfly controlDict.
"""
ghenv.Component.Name = "Butterfly_Solution Parameters"
ghenv.Component.NickName = "solutionParams"
ghenv.Component.Message = 'VER 0.0.01\nSEP_18_2016'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "07::Solver"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
     from butterfly.solution import SolutionParameters
except ImportError as e:
    msg = '\nFailed to import butterfly. Did you install butterfly on your machine?' + \
            '\nYou can download the installer file from github: ' + \
            'https://github.com/mostaphaRoudsari/Butterfly/tree/master/plugin/grasshopper/samplefiles' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/mostaphaRoudsari/Butterfly/issues'
        
    raise ImportError('{}\n{}'.format(msg, e))


if runtimeParams_:
    raise NotImplementedError('NotImplemented > Runtime parameters will be applied in the coming releases.')

solutionParams = SolutionParameters(controlDict_, residualControl_, probes_)