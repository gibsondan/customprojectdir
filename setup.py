from setuptools import find_packages, setup

setup(
    name="quickstart_etl",
    version="0.0.1",
    packages=find_packages(),
    package_data={},
    install_requires=[
        "dagster==1.10.20",
        "dagster-dbt==0.26.20",
        "dagster-cloud",
        "dagster-gcp",
        "dagster-slack",
        "dbt-core<1.10",
        "dbt-bigquery<1.10",
        "sentry_sdk<=2.34.1",
        "pandas",
        "boto3",
        "matplotlib",
        "pandas",
        "textblob",
        "tweepy",
        "wordcloud",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)
