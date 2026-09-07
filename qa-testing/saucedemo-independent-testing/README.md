\# SauceDemo Independent Manual QA Testing



\## Project Overview



I independently tested SauceDemo, a demo e-commerce web application, to evaluate its core functionality and identify reproducible issues. I executed 23 scripted test scenarios covering both positive and negative cases, followed by exploratory testing across multiple provided user accounts. The goal of this project was to verify whether key application features behaved as expected and to practice identifying, reproducing, investigating, and documenting software defects.


## Test Coverage

Testing covered the following areas:

- Login with valid, invalid, and missing credentials
- Product listing and product details
- Adding and removing products from the cart
- Cart state and behavior across different user accounts
- Checkout and order completion
- PDF order generation
- Product sorting
- Menu navigation and logout
- Reset App State functionality
- Social and footer elements
- Browser navigation and session-related behavior
- Multiple provided user accounts with different application behavior
- Basic UI, performance, and DevTools investigation


## Testing Approach

I used a combination of scripted and exploratory manual testing.

The testing process included:

- Understanding the application's main user flow before formal testing
- Defining the test scope and environment
- Designing and executing 23 scripted test scenarios
- Performing positive and negative testing
- Exploring different provided user accounts and application states
- Reproducing suspicious behavior multiple times before reporting it
- Comparing behavior between different users where relevant
- Using Chrome DevTools to investigate selected UI, network, HTML, and performance observations
- Collecting screenshot evidence for reproducible findings
- Separating confirmed defects from observations or behavior with unclear requirements

## Execution Summary

- **Scripted test scenarios executed:** 23
- **Passed:** 19
- **Failed:** 2
- **Recorded as observations:** 2
- **Detailed findings documented:** 7

Exploratory testing was also performed beyond the scripted scenarios, including cross-user state testing, special user-account behavior, browser navigation, UI consistency, and selected DevTools investigation.


## Test Environment

- **Operating System:** Windows 11
- **Browser:** Google Chrome 152.0.7977.76
- **Application:** SauceDemo
- **Testing Type:** Manual functional, exploratory, usability, and basic performance testing
- **Tools:** Google Chrome DevTools


## Project Structure

- `README.md` - Project overview, scope, environment, and testing approach
- `test-cases.md` - Scripted test scenarios and execution results
- `bug-report.md` - Validated defects with reproduction details
- `evidence/` - Screenshot evidence supporting selected findings


## Project Files

- [View Test Cases](test-cases.md)
- [View Bug Report](bug-report.md)
- [View Evidence](evidence/)

