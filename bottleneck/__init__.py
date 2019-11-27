# try:
#     from dopplerlidarpy.bottleneck.bottleneck.slow.reduce import (
#         nansum,
#         nanmean,
#         nanstd,
#         nanvar,
#         nanmin,
#         nanmax,
#         median,
#         nanmedian,
#         ss,
#         nanargmin,
#         nanargmax,
#         anynan,
#         allnan,
#     )
#     from dopplerlidarpy.bottleneck.bottleneck.slow.nonreduce import replace
#     from dopplerlidarpy.bottleneck.bottleneck.slow.nonreduce_axis import partition, argpartition, rankdata, nanrankdata, push
#     from dopplerlidarpy.bottleneck.bottleneck.slow.move import (
#         move_sum,
#         move_mean,
#         move_std,
#         move_var,
#         move_min,
#         move_max,
#         move_argmin,
#         move_argmax,
#         move_median,
#         move_rank,
#     )
#
#     from dopplerlidarpy.bottleneck.bottleneck import slow
#
# except ImportError:
#     raise ImportError(
#         "bottleneck modules failed to import, likely due to a "
#         "mismatch in NumPy versions. Either upgrade numpy to "
#         "1.16+ or install with:\n\t"
#         "pip install --no-build-isolation --no-cache-dir "
#         "bottleneck"
#     )
#
# from dopplerlidarpy.bottleneck.bottleneck.benchmark.bench import bench
# from dopplerlidarpy.bottleneck.bottleneck.benchmark.bench_detailed import bench_detailed
# from dopplerlidarpy.bottleneck.bottleneck.tests.util import get_functions
#
# from dopplerlidarpy.bottleneck.bottleneck._pytesttester import PytestTester
#
# test = PytestTester(__name__)
# del PytestTester
#
# from dopplerlidarpy.bottleneck.bottleneck._version import get_versions  # noqa: E402
#
# __version__ = get_versions()["version"]
# del get_versions
