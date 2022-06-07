# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyRay(PythonPackage):
    """A system for parallel and distributed Python that unifies the ML
    ecosystem."""

    homepage = "https://github.com/ray-project/ray"
    url      = "https://github.com/ray-project/ray/archive/ray-0.8.7.tar.gz"

    version('0.8.7', sha256='2df328f1bcd3eeb4fa33119142ea0d669396f4ab2a3e78db90178757aa61534b')

    build_directory = 'python'

    depends_on('python@3.6:3.8', type=('build', 'run'))
    depends_on('bazel@3.2.0', type='build')
    depends_on('py-setuptools', type='build')
    depends_on('py-cython@0.29.14:', type='build')
    depends_on('py-wheel', type='build')
    depends_on('npm', type='build')
    depends_on('py-aiohttp', type=('build', 'run'))
    depends_on('py-aioredis', type=('build', 'run'))
    depends_on('py-click@7.0:', type=('build', 'run'))
    depends_on('py-colorama', type=('build', 'run'))
    depends_on('py-colorful', type=('build', 'run'))
    depends_on('py-filelock', type=('build', 'run'))
    depends_on('py-google', type=('build', 'run'))
    depends_on('py-gpustat', type=('build', 'run'))
    depends_on('py-grpcio@1.28.1:', type=('build', 'run'))
    depends_on('py-jsonschema', type=('build', 'run'))
    depends_on('py-msgpack@1.0:1', type=('build', 'run'))
    depends_on('py-numpy@1.16:', type=('build', 'run'))
    depends_on('py-protobuf@3.8.0:', type=('build', 'run'))
    depends_on('py-py-spy@0.2.0:', type=('build', 'run'))
    depends_on('py-pyyaml', type=('build', 'run'))
    depends_on('py-requests', type=('build', 'run'))
    depends_on('py-redis@3.3.2:3.4', type=('build', 'run'))
    depends_on('py-opencensus', type=('build', 'run'))
    depends_on('py-prometheus-client@0.7.1:', type=('build', 'run'))
    # If not guarded by SKIP_THIRDPARTY_INSTALL, those dependencies
    # would be automatically installed via pip by the setup.py script.
    depends_on('py-setproctitle', type=('build', 'run'))
    depends_on('py-psutil', type=('build', 'run'))
    # If not detected during install, the following dependency would
    # be automatically downloaded and installed by the setup.py script.
    depends_on('py-pickle5', when='^python@:3.8.1', type=('build', 'run'))

    def setup_build_environment(self, env):
        env.set('SKIP_THIRDPARTY_INSTALL', '1')

    # Compile the dashboard npm modules included in the project
    @run_before('install')
    def build_dashboard(self):
        with working_dir(join_path('python', 'ray', 'dashboard', 'client')):
            npm = which('npm')
            npm('ci')
            npm('run', 'build')
