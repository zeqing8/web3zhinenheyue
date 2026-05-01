# SmartAudit-Agent

An AI-powered Smart Contract Security Audit and Auto-Repair Agent.

## Overview
This project demonstrates a multi-agent workflow for auditing Ethereum smart contracts (Solidity). It identifies common vulnerabilities like reentrancy, integer overflow, and access control issues, then suggests and implements fixes.

## Features
- **Security Audit**: Deep analysis of Solidity source code.
- **Auto-Fix**: Generates patched versions of the vulnerable code.
- **Report Generation**: Outputs a detailed security assessment.

## Setup
1. Clone the repository.
2. Install dependencies:
   pip install -r requirements.txt
3. Set your OpenAI API Key in the `audit_agent.py` file or as an environment variable.

## Usage
Run the audit script on the provided sample:
python audit_agent.py --file contracts/vulnerable.sol
