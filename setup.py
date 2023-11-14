from setuptools import setup


setup(
    name='cldfbench_dplace-dataset-binford',
    py_modules=['cldfbench_dplace-dataset-binford'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'dplace-dataset-binford=cldfbench_dplace-dataset-binford:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
