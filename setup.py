from setuptools import setup, find_packages


setup(
    name='plonetheme.unilluminated',
    version='0.1.0',
    description='An installable Diazo theme for Plone 4.1',
    long_description=open("README.rst", "rb").read(),
    author='Alex Clark',
    author_email='aclark@aclark.net',
    url='https://github.com/aclark4life/plonetheme.unilluminated',
    classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python',
    ],
    keywords='web zope plone theme diazo',
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=[
        'plonetheme',
    ],
    install_requires=[
        'setuptools',
        'plone.app.theming',
    ],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
)
