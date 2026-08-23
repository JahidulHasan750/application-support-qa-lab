# 20-Week Technical Support & Manual QA Progress Tracker

## Every Week Routine (Portfolio Habit)
- [ ] Push all weekly scripts, reports, and query files to GitHub
- [ ] Update the section `README.md` explaining key concepts and findings
- [ ] Add new CLI commands, HTTP headers, or SQL queries to your personal troubleshooting cheat sheet

---

## Phase 1: Foundation, DevTools & Freelance Launch (Weeks 1–9)

### Weeks 1–3: Web Networking, APIs, DevTools & Git Setup
* **Learning:**
  - [ ] Watched/read material on IP addressing, DNS, TCP/UDP, and Ports
  - [ ] Learned HTTP/HTTPS protocols, request methods (GET/POST), and status codes
  - [ ] Studied JSON structure, request headers, cookies, and authentication tokens
* **Practice:**
  - [ ] Used Chrome/Edge DevTools (Network and Console tabs) on a live site
  - [ ] Ran CLI commands (`ping`, `traceroute`, `nslookup`, `curl`) to diagnose connection issues
  - [ ] Practiced sending requests and checking response payloads in Postman
* **Evidence:**
  - [ ] Initialized local repository with `git init`, `git add`, `git commit -m`
  - [ ] *(Optional)* Earned Postman Student Expert Badge
  - [ ] Pushed initial API bug report to `application-support-qa-lab/api-testing/`

---

### Weeks 4–5: Linux System Administration & Server Logs
* **Learning:**
  - [ ] Learned and practiced CLI navigation (`cd`, `ls`, `pwd`) and file permissions (`chmod`, `chown`)
  - [ ] Understood server log formats (Apache/Nginx/Syslog) and process tracking
* **Practice:**
  - [ ] Filtered server log entries using `grep`, `tail -f`, and `less`
  - [ ] Isolated server-side issues vs client-side browser errors via log inspection
  - [ ] Worked through OverTheWire Bandit challenges
* **Evidence:**
  - [ ] Created a Linux Log Command Cheat Sheet
  - [ ] Uploaded 5 log-based bug reports to `application-support-qa-lab/linux/`

---

### Week 6: Cloud Infrastructure & VM Connectivity
* **Learning:**
  - [ ] Studied AWS EC2 basics, Security Groups, IAM roles, and CloudWatch log features
  - [ ] Learned multi-stage isolation flow (Host -> Network -> Security Group -> Port -> Service)
* **Practice:**
  - [ ] Investigated unreachable VM scenarios (simulated or documented sandbox tests)
  - [ ] Practiced checking/configuring basic inbound and outbound rules in a lab environment
* **Evidence:**
  - [ ] Uploaded a Cloud VM Incident Isolation Flowchart to `application-support-qa-lab/troubleshooting/`

---

### Weeks 7–8: SQL Databases & Data Validation Testing
* **Learning:**
  - [ ] Learned SQL syntax: `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`, and `COUNT`
  - [ ] Studied backend relational data structures (Users, Orders, Transactions)
* **Practice:**
  - [ ] Executed queries on SQLBolt / PostgreSQL Tutorial environments
  - [ ] Cross-referenced missing UI elements against backend database tables
* **Evidence:**
  - [ ] Created SQL query test suite and backend validation bug report in `application-support-qa-lab/sql/`

---

### Week 9: ITSM Workflows, Jira & QA Capstone
* **Learning:**
  - [ ] Understood Jira ticket lifecycles, SLAs, priorities, and escalation paths
  - [ ] Learned and practiced QA testing taxonomy (Functional, Negative, Boundary, Regression)
* **Practice:**
  - [ ] Executed complete end-to-end test suite on a live target web application
  - [ ] Filed standardized bug tickets containing Title, Steps, Expected vs Actual, and Severity
* **Evidence:**
  - [ ] Finalized main `README.md` and published full public `application-support-qa-lab` repository
  - [ ] **MILESTONE:** Applied for Remote L2/Support roles, optimized existing Fiverr website testing gig, and added API testing capabilities

---

## Phase 2: Enterprise Systems, Cloud Support & Career Acceleration (Weeks 10–20)

### Week 10: Identity, M365 Sync & PowerShell Fundamentals
* **Learning:**
  - [ ] Studied Entra ID (Azure AD) user objects, directory sync, and MFA policies
  - [ ] Learned basic PowerShell commands (`Get-Service`, `Test-NetConnection`)
* **Practice:**
  - [ ] Diagnosed account lockout, bad credential, and single sign-on (SSO) failures
* **Evidence:**
  - [ ] Uploaded M365 & Entra ID Troubleshooting Guide to repository

---

### Weeks 11–12: Endpoint & Access Support
* **Learning:**
  - [ ] Studied M365 licensing structures, device registration, and conditional access concepts
  - [ ] Learned Intune policy sync behavior and compliance status logs
* **Practice:**
  - [ ] Documented steps to resolve device compliance and software deployment blocks
* **Evidence:**
  - [ ] Created an Endpoint Access Escalation Ticket Template

---

### Weeks 13–15: Cloud Support & Gateway Troubleshooting
* **Learning:**
  - [ ] Studied HTTP 502/503 Bad Gateway errors, reverse proxy routing, and load balancing
  - [ ] Learned CloudWatch alerting thresholds and metric logging
* **Practice:**
  - [ ] Isolated network layer blocks from application service crashes
* **Evidence:**
  - [ ] Documented a Cloud Metric Alert Rules & Gateway Incident Report

---

### Weeks 16–18: Multi-Tier Incident Labs
* **Learning:**
  - [ ] Reviewed full-stack dependency flow: Browser -> Network -> API -> App -> DB -> Infra
* **Practice:**
  - [ ] Investigated and documented 5 distinct multi-layer incident scenarios:
    1. Authentication / SSO failure
    2. API functional failure
    3. HTTP 502/503 Bad Gateway issue
    4. Database / Data mismatch problem
    5. Network / Infrastructure port block
* **Evidence:**
  - [ ] Published 5 detailed Root Cause Analysis (RCA) reports to repository

---

### Weeks 19–20: Portfolio Optimization & Technical Career Launch
* **Learning:**
  - [ ] Studied technical interview question patterns and ATS resume parsing
* **Practice:**
  - [ ] Ran technical mock interview drills and formatted resume keywords
* **Evidence:**
  - [ ] Deployed GitHub Pages portfolio site showcasing the lab repository
  - [ ] Completed ATS-optimized technical resume and scaled active job applications
