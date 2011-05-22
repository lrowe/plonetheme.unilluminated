from setuptools import setup, find_packages


setup(
    name='plonetheme.unilluminated',
    description='A Diazo theme for Plone 4.1',
    long_description=open("README.txt", "rb").read(),
    author='Alex Clark',
    author_email='aclark@aclark.net',
    url='https://github.com/aclark4life/plonetheme.unilluminated',
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    packages=find_packages(),
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
