# InnerSource Crawler
![.github/workflows/linter.yml](https://github.com/zkoppert/innersource-crawler/actions/workflows/linter.yml/badge.svg) ![Integration Test](https://github.com/zkoppert/innersource-crawler/actions/workflows/integration_tests.yml/badge.svg)

This project creates a repos.json that can be utilized by the SAP InnerSource Portal.

## Installation
`pip -r requirements.txt`

## Usage
1. Fill out the .env file with a token from a machine user that only has access to the org to scan
1. Fill out the .env file with the exact topic name you are searching for 
1. Run `python3 ./crawler.py`
