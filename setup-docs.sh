#!/bin/bash

# Create main project directory structure
mkdir -p docs/{getting-started,accounts,quick-deploy,custom-build,how-it-works,tutorials,troubleshooting,reference}

# Create getting-started section
mkdir -p docs/getting-started
touch docs/getting-started/{overview,prerequisites,deployment-options}.md

# Create accounts section
mkdir -p docs/accounts
touch docs/accounts/{aws-setup,stripe-setup,emqx-setup}.md

# Create quick-deploy section
mkdir -p docs/quick-deploy
touch docs/quick-deploy/{overview,docker-pull,aws-config,testing}.md

# Create custom-build section
mkdir -p docs/custom-build
touch docs/custom-build/{overview,code-overview,modifications,deployment}.md

# Create how-it-works section
mkdir -p docs/how-it-works
touch docs/how-it-works/{architecture,payment-flow,game-control,cloud-services}.md

# Create tutorials section
mkdir -p docs/tutorials
touch docs/tutorials/{basic-setup,payment-integration,game-integration}.md

# Create troubleshooting section
mkdir -p docs/troubleshooting
touch docs/troubleshooting/{common-issues,getting-help}.md

# Create reference section
mkdir -p docs/reference
touch docs/reference/{api-docs,config-options,glossary}.md

# Create index.md in root docs directory
touch docs/index.md

# Make script executable
chmod +x setup-docs.sh
