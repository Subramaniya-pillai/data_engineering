# Azure DevOps Participant Assignment – Banking Application

##  Objective
To simulate the breakdown and setup of a simple Banking Application in Azure DevOps, including:
- Epics → Features → User Stories → Tasks
- Git Repository setup with basic code structure
- CI/CD pipeline using Azure Pipelines or GitHub Actions
- Use of self-hosted agent due to hosted parallelism restrictions

---

##  Project Setup

###  Organization & Project
- Created a new Azure DevOps organization: `subramaniya-devops`
- Created a new project named: `BankingApp`

###  Repository
- Git repository: `banking-app`
- Structure:
- 
banking-app/

├── README.md

├── src/

│ └── app.py

└── .azure-pipelines.yml

### azure-pipeline.yml
```
trigger:
  - main
pool:
  name: MySelfHosted
steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.x'
  - script: python src/app.py
    displayName: 'Run Banking Application Placeholder'

```

### Azure Boards – Work Item Hierarchy

## Epics Created

![image](https://github.com/user-attachments/assets/d96ad823-7cb3-4dc6-a3ef-e2f134e101e8)


## Features under Each Epic

![image](https://github.com/user-attachments/assets/cb714057-bf01-4830-9d82-98952c3ef647)

##  User Stories 

![image](https://github.com/user-attachments/assets/6396fad8-272a-4609-849b-6f06380e755f)

##  Tasks


![image](https://github.com/user-attachments/assets/a85b78a5-aba5-4608-9863-13dbfdc47661)

