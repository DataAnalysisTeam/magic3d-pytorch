from setuptools import setup, find_packages

setup(
  name = 'magic3d-pytorch',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Magic3D - Nvidia\'s Text-to-3D',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/magic3d-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'text-to-3d',
    'denoising diffusion',
    'progressive refinement'
  ],
  install_requires=[
    'einops>=0.6',
    'torch>=1.6',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
