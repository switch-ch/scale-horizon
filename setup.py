from distutils.core import setup

setup(name='switch',
      version='0.1.3',
      author = 'Jens-Christian Fischer',
      author_email= 'jens-christian.fischer@switch.ch',
      url = 'http://switch.ch',
      description = 'OpenStack Horizon customizations',
      long_description = open('README.txt').read(),
      package_dir= { 'switch' : 'lib'},
      py_modules=['switch.scale-horizon'],
)


