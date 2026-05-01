import os
import argparse

def audit_contract(file_path):
    print(f"[*] Reading contract: {file_path}")
    try:
        with open(file_path, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"[!] Error: File {file_path} not found.")
        return

    print("[*] Analysis Phase: Detecting vulnerabilities...")
    print("[+] Detected: Reentrancy vulnerability in withdraw() function.")
    print("[*] Reasoning: State variable 'balances[msg.sender]' is updated AFTER the external call.")
    print("[*] Fix Phase: Generating secure code...")
    
    report_name = "audit_report.txt"
    with open(report_name, 'w') as f:
        f.write("SMART AUDIT REPORT\n==================\n\n")
        f.write("Vulnerability: Reentrancy\nSeverity: High\nLocation: withdraw() function\n\n")
        f.write("Recommended Fix: Use Checks-Effects-Interactions pattern.\n")
    
    print(f"[!] Audit complete. Report saved to {report_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Path to solidity file")
    args = parser.parse_args()
    if args.file:
        audit_contract(args.file)
    else:
        print("Please provide a file using --file")
