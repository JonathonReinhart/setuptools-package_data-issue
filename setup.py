from setuptools import setup, Command
from distutils.command.build import build

class build_data(Command):
    description = "Build data"

    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass

    def run(self):
        with open('mypkg/generated_data', 'w') as f:
            f.write('Data generated during setup.py build')


class build_hook(build):
    def run(self):
        self.run_command('build_data')
        build.run(self)

setup(
    name = 'mypkg',
    version = '1.2.3',
    packages = ['mypkg'],
    package_data = {
        'mypkg': [
            'generated_data',
        ],
    },
    zip_safe = False,   # http://stackoverflow.com/q/24642788/119527
    cmdclass = {
        'build_data':   build_data,
        'build':        build_hook,
    },
)
