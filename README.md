# InnerSource Crawler
![.github/workflows/linter.yml](https://github.com/zkoppert/innersource-crawler/actions/workflows/linter.yml/badge.svg) ![CodeQL](https://github.com/zkoppert/innersource-crawler/actions/workflows/codeql-analysis.yml/badge.svg)

This project creates a `repos.json` that can be utilized by the [SAP InnerSource Portal][SAP-InnerSource-Portal]. The current approach assumes that the repos that you want to show in the portal are available in a GitHub organization, and that they all are tagged with a certain _topic_.

## Installation

`pip install -r requirements.txt`

## Usage

1. Copy `.env-example` to `.env`
1. Fill out the `.env` file with a _token_ from a user that has access to the organization to scan (listed below). Tokens should have admin:org or read:org access.
1. Fill out the `.env` file with the exact _topic_ name you are searching for
1. Fill out the `.env` file with the exact _organization_ that you want to search in
1. (Optional) Fill out the `.env` file with the exact _URL_ of the GitHub Enterprise that you want to search in. Keep empty if you want to search in the  public `github.com`.
1. Run `python3 ./crawler.py`, which will create a `repos.json` file containing the relevant metadata for the GitHub repos for the given _topic_
1. Copy `repos.json` to your instance of the [SAP-InnerSource-Portal][SAP-InnerSource-Portal] and launch the portal as outlined in their installation instructions

[SAP-InnerSource-Portal]: https://github.com/sap/project-portal-for-InnerSource

## License
[MIT](LICENSE)
