from setuptools import setup, find_packages

setup(
    name='miyuki',
    version='0.6.8',
    packages=find_packages(include=['miyuki_src', 'miyuki_src.*']),
    install_requires=[
        'curl_cffi',
    ],
    entry_points={
        'console_scripts': [
            'miyuki=miyuki_src.main:main',
        ],
    },
    author='MiyukiQAQ',
    description='A tool for downloading videos from the "MissAV" website.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MiyukiQAQ/MissAV-Downloader',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
