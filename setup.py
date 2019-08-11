from setuptools import setup,find_packages

setup(
    name='sailist',
    version='0.4.dev1',
    description='convert markdown 2 latex code perfactly,support Chinese Language',
    url='https://github.com/sailist/colorprint',
    author='sailist',
    author_email='sailist@outlook.com',
    license='MIT',
    include_package_data = True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='colored text print terminal',
    packages=find_packages(),
)