# InnerSource Crawler
![.github/workflows/linter.yml](https://github.com/zkoppert/innersource-crawler/actions/workflows/linter.yml/badge.svg) ![CodeQL](https://github.com/zkoppert/innersource-crawler/actions/workflows/codeql-analysis.yml/badge.svg)

This project creates a `repos.json` that can be utilized by the [SAP InnerSource Portal][SAP-InnerSource-Portal]. The current approach assumes that the repos that you want to show in the portal are available in a GitHub organization, and that they all are tagged with a certain _topic_.

## Support
If you need support using this project or have questions about it, please [open up an issue in this repository](https://github.com/zkoppert/innersource-crawler/issues). Requests made directly to GitHub staff or support team will be redirected here to open an issue. GitHub SLA's and support/services contracts do not apply to this repository.

## Use as a GitHub Action

1. Create a repository to host this GitHub Action or select an existing repository.
1. Create the env values from the sample workflow below (GH_TOKEN, ORGANIZATION) with your information as repository secrets. More info on creating secrets can be found [here](https://docs.github.com/en/actions/security-guides/encrypted-secrets).
Note: Your GitHub token will need to have read/write access to all the repositories in the organization
1. Copy the below example workflow to your repository and put it in the `.github/workflows/` directory with the file extension `.yml` (ie. `.github/workflows/crawler.yml`)
1. Don't forget to do something with the resulting `repos.json` file. You can [move it to another repository](https://github.com/marketplace/actions/push-a-file-to-another-repository) if needed or [save it as a build artifact](https://github.com/actions/upload-artifact). This will all depend on what you are doing with it and what repository you are running this action out of.

### Example workflow
```yaml
name: InnerSource repo crawler

on:
  workflow_dispatch:
  schedule:
    - cron: '00 5 * * *'

jobs:
  build:
    name: InnerSource repo crawler
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2
    
    - name: Run crawler tool
      uses: docker://ghcr.io/zkoppert/innersource-crawler:v1
      env:
        GH_TOKEN: ${{ secrets.GH_TOKEN }}
        ORGANIZATION: ${{ secrets.ORGANIZATION }}
        TOPIC: inner-source
```

## Local usage without Docker

1. Copy `.env-example` to `.env`
1. Fill out the `.env` file with a _token_ from a user that has access to the organization to scan (listed below). Tokens should have admin:org or read:org access.
1. Fill out the `.env` file with the exact _topic_ name you are searching for
1. Fill out the `.env` file with the exact _organization_ that you want to search in
1. (Optional) Fill out the `.env` file with the exact _URL_ of the GitHub Enterprise that you want to search in. Keep empty if you want to search in the  public `github.com`.
1. `pip install -r requirements.txt`
1. Run `python3 ./crawler.py`, which will create a `repos.json` file containing the relevant metadata for the GitHub repos for the given _topic_
1. Copy `repos.json` to your instance of the [SAP-InnerSource-Portal][SAP-InnerSource-Portal] and launch the portal as outlined in their installation instructions

[SAP-InnerSource-Portal]: https://github.com/sap/project-portal-for-InnerSource

## License
[MIT](LICENSE)
