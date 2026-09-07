\# SauceDemo Test Cases



\## Test Execution



\*\*Total scripted test scenarios:\*\* 23



| ID | Test Scenario | Expected Result | Actual Result | Status |

|----|---------------|-----------------|---------------|--------|

| TC-01 | Login with valid credentials | User logs in successfully and reaches the Products page | Login succeeded and Products page loaded | PASS |

| TC-02 | Login with incorrect username | Login is rejected with an appropriate error message | Login was rejected with an error message | PASS |

| TC-03 | Login with incorrect password | Login is rejected with an appropriate error message | Login was rejected with an error message | PASS |

| TC-04 | Login with empty username | Validation message indicates username is required | "Username is required" message displayed | PASS |

| TC-05 | Login with empty password | Validation message indicates password is required | "Password is required" message displayed | PASS |

| TC-06 | Open product details | The selected product's correct details are displayed | Correct product details were displayed | PASS |

| TC-07 | Add a product to the cart | Selected product is added to the cart and cart state updates | Product was added successfully | PASS |

| TC-08 | Remove a product from the cart | Selected product is removed from the cart | Product was removed successfully | PASS |

| TC-09 | Complete checkout with valid information | Checkout completes successfully | Checkout completed successfully | PASS |

| TC-10 | Generate PDF order after successful checkout | PDF is generated with relevant order information | PDF was generated with relevant order information | PASS |

| TC-11 | Use the All Items menu option | User is taken to the Products page | Products page opened successfully | PASS |

| TC-12 | Use the About menu option | User is taken to the intended About destination | Browser was redirected to saucelabs.com, which returned 403 Forbidden | FAIL |

| TC-13 | Log out from the application | User is returned to the Login page | Logout completed successfully | PASS |

| TC-14 | Use Reset App State | Cart is cleared and application state resets | Cart was cleared, but some product buttons remained in the Remove state until refresh | FAIL |

| TC-15 | Sort products by Name (A to Z) | Products are ordered alphabetically ascending | Products were sorted correctly | PASS |

| TC-16 | Sort products by Name (Z to A) | Products are ordered alphabetically descending | Products were sorted correctly | PASS |

| TC-17 | Sort products by Price (low to high) | Products are ordered by ascending price | Products were sorted correctly | PASS |

| TC-18 | Sort products by Price (high to low) | Products are ordered by descending price | Products were sorted correctly | PASS |

| TC-19 | Open X social link | Relevant X page opens | Relevant page opened successfully | PASS |

| TC-20 | Open Facebook social link | Relevant Facebook page opens | Relevant page opened successfully | PASS |

| TC-21 | Open LinkedIn social link | Relevant LinkedIn page opens | Relevant page opened successfully | PASS |

| TC-22 | Interact with Terms of Service text | Terms of Service opens if implemented as a link | Text was not interactive and contained no link element | OBSERVATION |

| TC-23 | Interact with Privacy Policy text | Privacy Policy opens if implemented as a link | Text was not interactive and contained no link element | OBSERVATION |

