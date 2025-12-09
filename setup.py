from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension(
        "pmesh._domain",
        ["pmesh/_domain.pyx"],
        include_dirs=["./", numpy.get_include()]
    ),
    Extension(
        "pmesh._window",
        ["pmesh/_window.pyx", "pmesh/_window_imp.c"],
        depends=[
            "pmesh/_window_imp.h",
            "pmesh/_window_tuned_pcs.h",
            "pmesh/_window_tuned_tsc.h",
            "pmesh/_window_tuned_cic.h",
            "pmesh/_window_tuned_nnb.h",
            "pmesh/_window_generics.h",
            "pmesh/_window_wavelets.h",
            "pmesh/_window_lanczos.h",
            "pmesh/_window_acg.h",
        ],
        libraries=["m"],
        include_dirs=["./", numpy.get_include()]
    ),
    Extension(
        "pmesh._invariant",
        ["pmesh/_invariant.pyx"],
        depends=["pmesh/_invariant_imp.c"],
        libraries=["m"],
        include_dirs=["pmesh", numpy.get_include()]
    ),
    Extension(
        "pmesh._whitenoise",
        [
            "pmesh/gsl/ranlxd.c",
            "pmesh/gsl/missing.c",
            "pmesh/gsl/rng.c",
            "pmesh/_whitenoise_imp.c",
            "pmesh/_whitenoise.pyx",
        ],
        depends=[
            "pmesh/gsl/config.h",
            "pmesh/gsl/gsl_errno.h",
            "pmesh/gsl/gsl_inline.h",
            "pmesh/gsl/gsl_rng.h",
            "pmesh/gsl/gsl_types.h",
            "pmesh/_whitenoise_imp.h",
            "pmesh/_whitenoise_generics.h",
        ],
        libraries=["m"],
        include_dirs=["pmesh/gsl", "pmesh", numpy.get_include()]
    ),
]

setup(ext_modules=cythonize(extensions))
