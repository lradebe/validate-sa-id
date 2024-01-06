from setuptools import setup


setup(
    name="validate_sa_id",
    version="0.1.0",
    author="Lwazi Radebe",
    author_email="lwaziradebe100@gmail.com",
    python_requires=">=3.8",
    description="Validates all parts of an SA ID",
    py_modules=["validate_sa_ids"],
    package_dir={"": "validate_sa_id"},
)
