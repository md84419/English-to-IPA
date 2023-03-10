from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="English-to-IPA",
    version="0.3.0b21",
    description="Take English text and convert it to IPA",
    description_content_type="text/markdown",
    author=["mphilli", "Mitchellpkt", "CanadianCommander", "timvancann", "md84419"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=["eng_to_ipa"],
)
