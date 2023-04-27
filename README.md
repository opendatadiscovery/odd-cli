## OpenDataDiscovery CLI
[![PyPI version](https://badge.fury.io/py/odd-cli.svg)](https://badge.fury.io/py/odd-cli)

Command line tool for working with OpenDataDiscovery.
It makes it easy to create token though console and ingest local dataset's metadata to OpenDataDiscovery platform.

## Installation
```bash
pip install odd-cli
```

#### Available commands
```text
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                              │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation        │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────╮
│ collect                       Collect and ingest metadata for local files from folder      │
│ dbt                           Run dbt tests and inject results to ODD platform             │
│ tokens                        Manipulate OpenDataDiscovery platform's tokens               │
╰────────────────────────────────────────────────────────────────────────────────────────────╯
```
## Env variables used for commands

`ODD_PLATFORM_HOST` - Location of OpenDataDiscovery Platform.

`ODD_PLATFORM_TOKEN` - Collector token, can be created using [UI](https://docs.opendatadiscovery.org/configuration-and-deployment/trylocally#create-collector-entity) or `odd tokens create` command.

## Commands
Create collector token.
```bash
odd tokens create <collector_name>
```

Parse and ingest local files
```bash
odd collect <path_to_folder_with_datasets>
```

Run dbt tests and inject results to ODD platform. It uses [odd-dbt](https://github.com/opendatadiscovery/odd-dbt) package.
```bash
odd dbt test <path_to_dbt_project>
```
