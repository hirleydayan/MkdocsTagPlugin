from setuptools import setup, find_packages
setup(
    name='mdoctag',
    version='0.4.2',
    description='retrieve meta-data "tags"',
    packages=['mdoctag'],
    install_requires=['mkdocs'],
    entry_points={
        'mkdocs.plugins': [
            'mdoctag = mdoctag.tagplugin:TagPlugin',
        ]
    }
)
