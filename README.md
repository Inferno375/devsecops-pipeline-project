# DevSecOps CI/CD Pipeline: Automated SAST & Secret Scanning

## 📌 Overview
This project demonstrates a fully functional DevSecOps CI/CD pipeline built with GitHub Actions. The pipeline is designed to automatically intercept and block code commits that contain security vulnerabilities or exposed secrets before they can be merged or deployed.

## 🏗️ Architecture & Workflow
The pipeline acts as an automated security checkpoint in the CI/CD assembly line. Every `git push` triggers the following workflow:
1. **Source Code Checkout:** GitHub Actions spins up an Ubuntu environment and fetches the latest commit.
2. **Static Application Security Testing (SAST):** Semgrep analyzes the code's logic and structure to identify dangerous programming practices.
3. **Secret Scanning:** Gitleaks scans the commit history for high-entropy strings and known credential patterns.
4. **Build Enforcement:** If a critical vulnerability or secret is detected, the pipeline automatically fails the build, preventing compromised code from reaching production.

## 🛠️ Tools & Technologies Used
* **GitHub Actions:** CI/CD automation and workflow orchestration.
* **Semgrep:** SAST tool utilized to detect code-level logic flaws.
* **Gitleaks:** Secret scanning tool utilized to catch hardcoded credentials.
* **Python:** The language used to write the deliberately vulnerable application.

## 🚨 Vulnerabilities Demonstrated & Mitigated
To test the pipeline, a deliberately vulnerable Python application (`vulnerable_app.py`) was created containing two critical flaws:

1. **SQL Injection (CWE-89):** 
   * *The Flaw:* User input is directly concatenated into a SQLite query using string formatting.
   * *The Mitigation:* Caught by **Semgrep**, which flags the dangerous logic structure that could allow database manipulation.
2. **Exposed Cloud Credentials (CWE-798):** 
   * *The Flaw:* A simulated, high-entropy AWS Access Key was hardcoded directly into the script.
   * *The Mitigation:* Caught by **Gitleaks**, which identifies the credential pattern and fails the build to prevent the key from being permanently exposed in the public Git history.

## 💡 Key Learnings
Building this pipeline highlighted the critical distinction between different automated security tools:
* **SAST** is necessary for identifying structural logic errors (like SQLi) that make an application fundamentally insecure. 
* **Secret Scanning** is necessary for identifying sensitive data leaks (like API keys) that would instantly compromise external infrastructure if pushed to a public repository. 

---
*Created by Raphael Rodricks S J*
