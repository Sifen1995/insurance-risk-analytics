# insurance-risk-analytics



## Data Pipeline Replication & Version Control

This project utilizes Data Version Control (DVC) to ensure complete auditability of data assets. The underlying datasets are stored outside of Git version tracking to protect repository size.

### How to Retrieve the Data
To reproduce the working environment and extract the specific version of the data tied to this commit stage:

1. Ensure your local storage pathway is correctly linked or modify the remote configuration if working across environments.
2. Run the checkout command to sync your workspace file structures to match the tracked git pointers:
   ```bash
   dvc checkout