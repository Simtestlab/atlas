# Issue #4: update xwiki version with all feature

**Repository:** xwiki_documentation  
**Status:** Closed  
**Created:** 2025-02-26  
**Updated:** 2025-03-13  
**Closed:** 2025-03-13  
**Author:** @nallasivamselvaraj  
**Assignees:** @nallasivamselvaraj  
**Labels:** `enhancement`  

[View on GitHub](https://github.com/Simtestlab/xwiki_documentation/issues/4)

## Description

DoD: As a DevOps engineer, Need to upgrade and redeploy the XWiki page with all features to ensure comprehensive  documentation and restucture the repo.

xwiki-backup/
│── backup/
│   ├── backup.sh            # Script to back up XWiki database and files
│   ├── restore.sh             # Script to restore XWiki from backup
│   ├── cronjob                # Optional: Cronjob configuration for automated backups
│   ├── logs/                     # Directory to store backup logs
│   ├── snapshots/           # Directory to store backup snapshots
│
│── docker/
│   ├── Dockerfile                      # Dockerfile for running backup script in a container
│   ├── docker-compose.yml    # Compose file for managing backup services
│   ├── entrypoint.sh                 # Entrypoint script for the backup container
│
│── config/
│   ├── .env                               # Environment variables for database and backup settings
│   ├── xwiki.properties            # XWiki configuration file 
│   ├── database.conf               # Database connection settings
│
│── docs/
│   ├── README.md          # Documentation about the backup process
│   ├── setup.md                # Steps to set up backup and restore
│   ├── cronjob.md            # Instructions for setting up automated backups
│
│── .gitignore                    # Ignore backup files and logs
│── LICENSE                     # License file (if applicable)
│── README.md              # Main repository documentation
