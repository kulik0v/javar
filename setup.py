from setuptools import setup

setup(
    name='javar',
    version='0.0.6',
    description='Javar allows you to generate java cli with a set of options easily.',
    long_description='Run java binary from python',
    long_description_content_type='text/plain',
    url='https://github.com/nagolos/javar',
    # download_url='https://github.com/nagolos/javar/archive/master.zip',
    author='Alexander Kulikov',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable

    # packages=find_packages(),
    packages=['javar'],
    install_requires=[],
)
