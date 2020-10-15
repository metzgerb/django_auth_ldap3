from setuptools import find_packages, setup

from django_auth_ldap3 import __version__ as version

setup(
    name='django_multiauth_ldap3',
    version=version,
    license='BSD',
    author='Brian Metzger',
    author_email='bdmetzger33@gmail.com',
    description='A library for connecting Django\'s authentication system to an LDAP directory using multiple DNs',
    url='https://github.com/metzgerb/django_auth_ldap3',
    install_requires=[
        'Django >= 1.6.10',
        'ldap3 >= 0.9.7.1',
    ],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP',
    ],
)
