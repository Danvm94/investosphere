# **Investosphere Testing**

## **Testing Overview**

Extensive testing was conducted throughout the development process, involving
both individual and peer assessments. This rigorous testing approach ensured
the reliability and functionality of the Investosphere platform.

## **Contents**

## **Automated Testing**

### **Unit Testing**

#### **investo_hub/tests/test_chart**

- Command: `python3 manage.py test investo_hub.tests.test_chart`
- Found 3 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ...
- Ran 3 tests in 0.001s
- **Result:** OK
- Destroying test database for alias 'default'...

[Back to top &uarr;](#contents)

#### **investo_hub/tests/test_cryptos**

- Command: `python3 manage.py test investo_hub.tests.test_cryptos`
- Found 11 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ...........
- Ran 11 tests in 25.282s
- **Result:** OK
- Destroying test database for alias 'default'...

[Back to top &uarr;](#contents)

#### **investo_hub/tests/test_forms**

- Command: `python3 manage.py test investo_hub.tests.test_forms`
- Found 14 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- .....15.0 > 10 = True
- .5.0 > 10 = False
- .....1000.0
- .1000.0
- .1000.0
- .
- Ran 14 tests in 0.614s
- **Result:** OK
- Destroying test database for alias 'default'...

[Back to top &uarr;](#contents)

#### **investo_hub/tests/test_models**

- Command: `python3 manage.py test investo_hub.tests.test_models`
- Found 11 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ...........
- Ran 11 tests in 0.011s
- **Result:** OK
- Destroying test database for alias 'default'...

[Back to top &uarr;](#contents)

#### **investo_hub/tests/test_transactions**

- Command: `python3 manage.py test investo_hub.tests.test_transactions`
- Found 16 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ..........1
- ...0
- .2
- .1
- .
- Ran 16 tests in 0.036s
- **Result:** OK
- Destroying test database for alias 'default'...

[Back to top &uarr;](#contents)

#### **investo_hub/tests/test_views**

- Command: `python3 manage.py test investo_hub.tests.test_views`
- Found 10 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ..1
- .1.00 > 200.00000000000000000000 = False
- .Exception occurred: Cryptocurrency "nonexistent_crypto" not found in the
  cache.
- ..1000.00
- .1000.00
- .1000.00
- 1200.00
- .1000.00
- 1
- 800.00
- .
- Ran 10 tests in 6.948s
- **Result:** OK
- Destroying test database for alias 'default'...

[Back to top &uarr;](#contents)

#### **user_management/tests/test_crypto**

- Command: `python3 manage.py test user_management.tests.test_crypto`
- Found 2 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ..
- Ran 2 tests in 0.002s
- **Result:** OK
- Destroying test database for alias 'default'...

[Back to top &uarr;](#contents)

#### **user_management/tests/test_forms**

- Command: `python3 manage.py test user_management.tests.test_forms`
- Found 4 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ....
- Ran 4 tests in 0.813s
- **Result:** OK
- Destroying test database for alias 'default'...

[Back to top &uarr;](#contents)

#### **user_management/tests/test_models**

- Command: `python3 manage.py test user_management.tests.test_models`
- Found 1 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- .
- Ran 1 test in 0.001s
- **Result:** OK
- Destroying test database for alias 'default'...

[Back to top &uarr;](#contents)

#### **user_management/tests/test_newsapi**

- Command: `python3 manage.py test user_management.tests.test_newsapi`
- Found 2 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ..
- Ran 2 tests in 0.002s
- **Result:** OK
- Destroying test database for alias 'default'...

[Back to top &uarr;](#contents)

#### **user_management/tests/test_views**

- Command: `python3 manage.py test user_management.tests.test_views`
- Found 13 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- .............
- Ran 13 tests in 6.730s
- **Result:** OK
- Destroying test database for alias 'default'...

[Back to top &uarr;](#contents)

### **Site Coverage Report**

The test coverage for this project currently stands at 68%. While automated
testing has covered a significant portion of the codebase, additional testing
through manual methods will be conducted to ensure comprehensive coverage.

| Name                                                        | Stmts | Miss | Cover |
|-------------------------------------------------------------|-------|------|-------|
| env.py                                                      | 10    | 0    | 100%  |
| investo_hub/__init__.py                                     | 0     | 0    | 100%  |
| investo_hub/admin.py                                        | 0     | 0    | 100%  |
| investo_hub/apps.py                                         | 4     | 0    | 100%  |
| investo_hub/chart.py                                        | 14    | 10   | 29%   |
| investo_hub/cryptos.py                                      | 64    | 34   | 47%   |
| investo_hub/forms.py                                        | 66    | 20   | 70%   |
| investo_hub/migrations/0001_initial.py                      | 8     | 0    | 100%  |
| investo_hub/migrations/0002_rename_symbol_cryptos_crypto.py | 4     | 0    | 100%  |
| investo_hub/migrations/__init__.py                          | 0     | 0    | 100%  |
| investo_hub/models.py                                       | 35    | 12   | 66%   |
| investo_hub/transactions.py                                 | 61    | 46   | 25%   |
| investo_hub/urls.py                                         | 3     | 0    | 100%  |
| investo_hub/views.py                                        | 110   | 92   | 16%   |
| investosphere/__init__.py                                   | 0     | 0    | 100%  |
| investosphere/asgi.py                                       | 4     | 4    | 0%    |
| investosphere/settings.py                                   | 32    | 1    | 97%   |
| investosphere/urls.py                                       | 4     | 0    | 100%  |
| investosphere/wsgi.py                                       | 4     | 4    | 0%    |
| manage.py                                                   | 12    | 2    | 83%   |
| user_management/__init__.py                                 | 0     | 0    | 100%  |
| user_management/admin.py                                    | 1     | 0    | 100%  |
| user_management/apps.py                                     | 4     | 0    | 100%  |
| user_management/crypto.py                                   | 7     | 1    | 86%   |
| user_management/forms.py                                    | 21    | 1    | 95%   |
| user_management/migrations/0001_initial.py                  | 5     | 0    | 100%  |
| user_management/migrations/__init__.py                      | 0     | 0    | 100%  |
| user_management/models.py                                   | 3     | 0    | 100%  |
| user_management/newsapi.py                                  | 14    | 0    | 100%  |
| user_management/registration.py                             | 7     | 0    | 100%  |
| user_management/tests/test_crypto.py                        | 13    | 0    | 100%  |
| user_management/tests/test_forms.py                         | 22    | 0    | 100%  |
| user_management/tests/test_models.py                        | 6     | 0    | 100%  |
| user_management/tests/test_newsapi.py                       | 19    | 0    | 100%  |
| user_management/tests/test_views.py                         | 106   | 0    | 100%  |
| user_management/urls.py                                     | 3     | 0    | 100%  |
| user_management/views.py                                    | 64    | 8    | 88%   |
| TOTAL                                                       | 730   | 235  | 68%   |

[Back to top &uarr;](#contents)

## **Manual Testing**

Several features on the site are exclusively accessible to registered users.
These features include:

- Viewing the chart page for crypto price history
- Accessing the wallet page for deposits, withdrawals, and transaction history
- Exploring the crypto page for buying, selling, and viewing transaction
  history

Please note that if you plan to evaluate the project, an admin username and
password have been provided during project submission. These credentials are
intended to facilitate the verification of the tests that have been conducted
on the 'Manage' page for adding new crypto support through the website

### **User Story Testing**

#### **Homepage**

`
As a user, I want to see a welcoming home page when I visit the platform to understand its purpose and navigate its features.
`

The homepage of this website is designed with three main sections, each serving
a specific purpose:

1. **Welcome Message**: A warm welcome message greets visitors to the site,
   creating a user-friendly and inviting atmosphere.
    - [x] Welcome message is displayed correctly.
      ![welcome-section](./README/welcome-section.png)
2. **Crypto Market Cap**: The homepage prominently displays the current
   cryptocurrency market capitalization, providing visitors with up-to-date
   financial information.
    - [x] The cryptocurrency market cap is accurately shown.
      ![market-cap-section](./README/market-cap-section.png)
3. **Crypto News**: The latest cryptocurrency news articles are featured on the
   homepage, ensuring that visitors have access to the most recent and relevant
   information in the crypto world.
    - [x] Crypto news articles are presented correctly.
      ![crypto-news-section](./README/crypto-news-section.png)

#### **Navbar**

`
As a user, I want a top navigation bar on the website for easy access to different sections.
`

1. **Responsive Design**: The navigation bar is displayed at the top of every
   page and is responsive to different screen sizes.
    - [x] Implemented and responsive on all screen sizes.

2. **Navigation Links**: The navigation bar includes links to relevant
   sections, such as Home, About, Services, and Contact.
    - [x] Links to Home, About, Services, and Contact sections are included.

3. **Mobile Menu**: On smaller screens, the navigation bar collapses into a "
   hamburger" menu for improved mobile usability.
    - [x] "Hamburger" menu is implemented for smaller screens.

4. **Active Link Highlighting**: The active link is visually distinguished from
   other links.
    - [x] Active link is highlighted for better user experience.

5. **Consistent Design**: The navigation bar maintains a consistent design
   throughout the site.
    - [x] Design is consistent across all pages.

![navbar-desktop-out](./README/navbar-desktop-out.png)
![navbar-desktop-in](./README/navbar-desktop-in.png)
![navbar-mobile-out](./README/navbar-mobile-out.png)
![navbar-mobile-in](./README/navbar-mobile-in.png)

#### **User Registration**

`As a user, I want the option to register for an account so that I can access the platform's features.`

1. **Registration Form**: A user-friendly registration form is available on the
   website.
    - [x] Registration form is designed and accessible.

   ![get-started](./README/get-started.png)

2. **Form Fields**: The registration form includes fields for username, email,
   and password.
    - [x] Fields for username, email, and password are present.

   ![register](./README/register.png)

3. **Submission**: Users can submit the registration form by clicking the "
   Register" button.
    - [x] "Register" button is provided for form submission.

4. **Success Message**: Upon successful registration, the user receives a
   confirmation message.
    - [x] Success message is displayed after successful registration.
      ![register-success](./README/register-success.png)

5. **Prevent Duplicates**: Users cannot register with an already existing
   username or email.
    - [x] System prevents registration with existing username or email.
      ![register-warn](./README/register-warn.png)

6. **Password Security**: Passwords are securely hashed before being stored for
   enhanced security.
    - [x] Passwords are securely hashed during registration.

#### **User Login**

As a user, I want the option to log in to my account so that I can access the
platform's personalized features.

1. **Login Form**: A user-friendly login form is available on the website.
    - [x] Login form is designed and accessible.
      ![login-link](./README/login-link.png)

2. **Form Fields**: The login form includes fields for username and password.
    - [x] Fields for username and password are present.
      ![login](./README/login.png)

3. **Submission**: Users can submit the login form to access their accounts.
    - [x] "Login" button is provided for form submission.

4. **Redirect to Dashboard**: Upon successful login, the user is redirected to
   the platform's main dashboard.
    - [x] Successful login redirects the user to the home page.
      ![login-success](./README/login-success.png)

5. **Access Control**: Users can't access authenticated features without
   logging in.
    - [x] Unauthorized access to authenticated features is restricted.

6. **Password Validation**: Passwords are securely compared and validated
   during the login process.
    - [x] Passwords are securely validated during login.

#### **Website Footer**

`As a user, I expect an informative and easily accessible footer to provide me
with essential links and information about the website.`

The website footer meets the following criteria:

1. **Consistent Display**: The footer is consistently displayed at the bottom
   of every page on the website.
    - [x] Footer is present on all pages.

2. **Social Media Links**: Social media icons with links to official social
   media profiles are included in the footer.
    - [x] Social media icons are displayed with functional links.

3. **Copyright Information**: The footer displays the copyright information for
   the website, including the copyright symbol (©), current year, and website
   name.
    - [x] Copyright information is visibly presented.

4. **Responsive Design**: The footer is designed responsively to adapt to
   different screen sizes.
    - [x] Footer layout adapts to various screen sizes.

![footer](./README/footer.png)

#### **Heroku Deployment**

`As a Developer, my goal is to ensure a seamless deployment of the website to
Heroku at an early stage. This will allow me to validate the functionality and
verify that all components are operational before proceeding with full-fledged
development. Additionally, this deployment will facilitate ongoing testing
within the production environment.`

1. **Create a New Heroku App**: Set up a new Heroku app to serve as the hosting
   platform for the website.
    - [x] Heroku app is created and configured.
      ![heroku-investosphere](./README/heroku-investosphere.png)

2. **Add the Database to the App Resources**: Incorporate the database into the
   app's resources on Heroku.
    - [x] Database is added and configured on Heroku.

3. **Update Heroku Config Vars with Secret Keys**: Configure the Heroku
   environment by adding the required secret keys to the configuration
   variables.
    - [x] Heroku config vars are updated with secret keys.

4. **Enable Automatic Deployment from GitHub**: Establish a connection between
   the Heroku app and the GitHub repository to enable automated deployments.
    - [x] Automated deployments from GitHub to Heroku are set up.

5. **Configure settings.py for Environment Variations**: In the settings.py
   file, set up conditional configurations: use the env.py file for
   development, switch to the OS for deployment, and adjust the database
   section to align with the accurate database URL provided by Heroku.
    - [x] Settings.py is properly configured for environment variations.

#### **Wallet Feature**

As a user, I want to have a digital wallet where I can manage my balance, add
funds, and withdraw funds as needed.

The Wallet feature meets the following criteria:

1. **Dedicated Wallet Section**: A dedicated section for managing the user's
   wallet is available on the website.
    - [x] The wallet section is accessible.

2. **Display Balance**: The wallet section displays the current balance of the
   user's account.
    - [x] The current wallet balance is visible.
![wallet](./README/wallet.png)

3. **Add Funds**: Users can add funds to their wallet using a specified amount.
    - [x] Users can input an amount and successfully add funds to their wallet.
![deposit](./README/deposit.gif)

4. **Withdraw Funds**: Users can withdraw funds from their wallet, subject to
   available balance.
    - [x] Users can request withdrawals, and the amount is deducted correctly
      from their wallet.
![withdraw](./README/withdraw.gif)

5. **Transaction Logging**: Wallet transactions are logged and displayed for
   user reference.
    - [x] Wallet transactions, including deposits and withdrawals, are logged
      and accessible.
![wallet-transactions](./README/wallet-transactions.png)