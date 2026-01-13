# Testing Documentation

[Automated Testing](#automated-testing)

- [Lighthouse Scores](#lighthouse-scores)
- [Running Tests](#running-tests)

[Manual Testing](#manual-testing)

<!--## Automated Testing

- **HTML Validation**: Used the [W3C HTML Validator](https://validator.w3.org/) which returned the following results:
  <div style="text-align: center; margin: 10px 0;">
      <img src="images_documentation/lighthouse_scores/html_validator.png" alt="HTML Validator Results" style="max-width: 50%; height: auto;">
  </div>

- **CSS Validation**: Used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) which returned the following results:
  <div style="text-align: center; margin: 10px 0;">
      <img src="images_documentation/lighthouse_scores/css_validator.png" alt="CSS Validator Results" style="max-width: 50%; height: auto;">
  </div>

- **JavaScript Validation**: Used [JSHint](https://jshint.com/) to validate JavaScript code. The validation process returned a clean report compliant with ES6+ standards.

<!-- ### Code Validation

#### CSS -->
<!--<img src="" alt="CSS Validation Result" style="width: 100%;"><br>

#### HTML
<img src="" alt="HTML Validation Result" style="width: 100%;"><br>

#### Python
<img src="" alt="Python Validation Result" style="width: 100%;"><br>

[Back to Top](#ux)

### Google Lighthouse
#### Landing Page
<img src="" alt="Landing Page Lighthouse Result" style="width: 100%;"><br>

#### Sign Up Page
<img src="" alt="Signup Page Lighthouse Result" style="width: 100%;"><br>

#### Login Page
<img src="" alt="Login Page Lighthouse Result" style="width: 100%;"><br>

#### About Page
<img src="" alt="About Page Lighthouse Result" style="width: 100%;"><br>

#### Search Page
<img src="" alt="About Page Lighthouse Result" style="width: 100%;"><br>

#### Account Page
<img src="" alt="My Account Page Lighthouse Result" style="width: 100%;"><br>

#### All Products Page
<img src="" alt="All Products Page Lighthouse Result" style="width: 100%;"><br>

#### Body Scrubs Page
<img src="" alt="Body Scrubs Page Lighthouse Result" style="width: 100%;"><br>

#### Body Butters Page
<img src="" alt="Body Butters Page Lighthouse Result" style="width: 100%;"><br>

#### New Arrivals Page
<img src="" alt="New Arrivals Page Lighthouse Result" style="width: 100%;"><br>

#### Checkout Page
<img src="" alt="Checkout Page Lighthouse Result" style="width: 100%;"><br>-->

[Back to Top](#automated-testing)

### Automated Testing

- **Jest**: A JavaScript testing framework used for unit and integration tests.
- **Django Test Framework**: The built-in testing framework for Django applications.

### Running Tests

Make sure to include the correct versions for both JavaScript & Django testing.

JavaScript -> `package.json`

Django -> `requirements.txt`

On the terminal write the commands below:

```bash
# For javascript
npm test

# For Django
python3 manage.py test
```

- **JavaScript Testing**: The JavaScript tests returned the following results:
  <!-- <div style="text-align: center; margin: 10px 0;">
      <img src="images_documentation/lighthouse_scores/js_tests.png" alt="JavaScript Tests Results" style="max-width: 50%; height: auto; margin: 0 10px;">
  </div> -->

<!-- - **Django Testing**: The Django tests for the application returned the following results:

<table style="width: 100%; margin: 20px 0; border-collapse: collapse; text-align: center;">
    <tr>
        <td>
            <h2>Bar App Tests</h2>
            <img src="images_documentation/lighthouse_scores/bar_app_tests.png" 
                 alt="Bar App Test Results" 
                 style="max-width: 50%; height: auto; margin: 10px 0;">
        </td>
        <td>
            <h2>Testimonial App Tests</h2>
            <img src="images_documentation/lighthouse_scores/testimonial_app_tests.png" 
                 alt="Testimonial App Test Results" 
                 style="max-width: 50%; height: auto; margin: 10px 0;">
        </td>
    </tr>
</table> -->

## Manual Testing

<!--### User Testing - Manual

<!--<details>
    <summary>Experience</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Test</th>
                    <th>Expectation</th>
                    <th>Outcome</th>
                </tr>
                <tr>
                    <td>Shopper can click a product to view full details</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Shopper once logged in, can leave a product review on previous purchase</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Shopper once logged in, can update a previous review</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Shopper when logged in, can delete previous review</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Shopper when logged in, can submit a newsletter subscription</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Shopper if not logged in, cannot leave a product review</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Shopper is redirected to Product page if login or signup is from another page</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Shopper receives link to validate email address and confirm wish to signup to website</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Shopper receives message to confirm status of all activities on site</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>->>

<!--<details>
    <summary>Navigation</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Test</th>
                    <th>Expectation</th>
                    <th>Outcome</th>
                </tr>
                <tr>
                    <td>Shopper can view product and details without signing in</td>
                    <td>Pass</td>
                    <th>Pass</th>
                </tr>
                <tr>
                    <td>Navigation links lead to their intended pages</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>Shopper is made aware via navigation links where they are on the website</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>Shopper can signup for an account to keep track of past purchases</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>Shopper can navigate to Home Page at any time by clicking Logo or Home </td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Signing Up</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Test</th>
                    <th>Expectation</th>
                    <th>Outcome</th>
                </tr>
                <tr>
                    <td>Shopper can create an account on the website</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>Shopper can login to existing account</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>Shopper is informed once account has successfully been created</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>Shopper can view past purchases under 'My Account'</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Responsiveness</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Test</th>
                    <th>Expectation</th>
                    <th>Outcome</th>
                </tr>
                <tr>
                    <td>Home, about, register and login pages display correctly on mobiles and tablets (769px and lower)</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Home, about, register, and login pages display correctly on laptops and desktops (992px and higher - up to 1200px)</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Content is layered when viewed on smaller devices</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Experience</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Test</th>
                    <th>Expectation</th>
                    <th>Outcome</th>
                </tr>
                <tr>
                    <td>Shopper can click a product to view full details</td>
                    <td>Pass</td>
                    <td>...</td>
                </tr>
                <tr>
                    <td>Shopper when logged in and previously purchased a product can leave a review</td>
                    <td>Pass</td>
                    <td>...</td>
                </tr>
                <tr>
                    <td>Shopper whether logged in or not cannot delete previous review</td>
                    <td>Pass</td>
                    <td>...</td>
                </tr>
                <tr>
                    <td>Shoppers when logged in can view purchase history</td>
                    <td>Pass</td>
                    <td>...</td>
                </tr>
                <tr>
                    <td>Shopper receives message to confirm status of all activities on site</td>
                    <td>Pass</td>
                    <td>...</td>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Authentication</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Test</th>
                    <th>Expectation</th>
                    <th>Outcome</th>
                </tr>
                <tr>
                    <td>Shopper can create an account on website</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>Shopper is sent link to validate email when attempting to create an account on website</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>Shopper can login to existing account</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>Shopper is informed once account has successfully been created</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>Shopper is unable to leave review on unauthorised purchase</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
            </table>
        </div>
    </div>
</details>-->

#### Stripe Payment
To test Stripe payment, use the following details:
- Card number - 4242 4242 4242 4242
- CVC - any 3 digit number
- Postal Code - any 5 digit number
- Expiry date - any future date