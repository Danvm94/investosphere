# **Investosphere Testing**

## **Testing Overview**

Extensive testing was conducted throughout the development process, involving both individual and peer assessments. This rigorous testing approach ensured the reliability and functionality of the Investosphere platform.

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

#### **investo_hub/tests/test_models**

- Command: `python3 manage.py test investo_hub.tests.test_models`
- Found 11 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ...........
- Ran 11 tests in 0.011s
- **Result:** OK
- Destroying test database for alias 'default'...

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

#### **investo_hub/tests/test_views**

- Command: `python3 manage.py test investo_hub.tests.test_views`
- Found 10 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ..1
- .1.00 > 200.00000000000000000000 = False
- .Exception occurred: Cryptocurrency "nonexistent_crypto" not found in the cache.
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

#### **user_management/tests/test_crypto**

- Command: `python3 manage.py test user_management.tests.test_crypto`
- Found 2 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ..
- Ran 2 tests in 0.002s
- **Result:** OK
- Destroying test database for alias 'default'...

#### **user_management/tests/test_forms**

- Command: `python3 manage.py test user_management.tests.test_forms`
- Found 4 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ....
- Ran 4 tests in 0.813s
- **Result:** OK
- Destroying test database for alias 'default'...

#### **user_management/tests/test_models**

- Command: `python3 manage.py test user_management.tests.test_models`
- Found 1 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- .
- Ran 1 test in 0.001s
- **Result:** OK
- Destroying test database for alias 'default'...

#### **user_management/tests/test_newsapi**


- Command: `python3 manage.py test user_management.tests.test_newsapi`
- Found 2 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ..
- Ran 2 tests in 0.002s
- **Result:** OK
- Destroying test database for alias 'default'...

#### **user_management/tests/test_views**

- Command: `python3 manage.py test user_management.tests.test_views`
- Found 13 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- .............
- Ran 13 tests in 6.730s
- **Result:** OK
- Destroying test database for alias 'default'...

### **Site Coverage Report**

| Name                                                          | Stmts | Miss | Cover |
|---------------------------------------------------------------|-------|------|-------|
| env.py                                                        |   10  |   0  |  100% |
| investo_hub/__init__.py                                       |   0   |   0  |  100% |
| investo_hub/admin.py                                          |   0   |   0  |  100% |
| investo_hub/apps.py                                           |   4   |   0  |  100% |
| investo_hub/chart.py                                          |  14   |  10  |   29% |
| investo_hub/cryptos.py                                        |  64   |  34  |   47% |
| investo_hub/forms.py                                          |  66   |  20  |   70% |
| investo_hub/migrations/0001_initial.py                        |   8   |   0  |  100% |
| investo_hub/migrations/0002_rename_symbol_cryptos_crypto.py   |   4   |   0  |  100% |
| investo_hub/migrations/__init__.py                            |   0   |   0  |  100% |
| investo_hub/models.py                                         |  35   |  12  |   66% |
| investo_hub/transactions.py                                   |  61   |  46  |   25% |
| investo_hub/urls.py                                           |   3   |   0  |  100% |
| investo_hub/views.py                                          | 110   |  92  |   16% |
| investosphere/__init__.py                                     |   0   |   0  |  100% |
| investosphere/asgi.py                                         |   4   |   4  |    0% |
| investosphere/settings.py                                     |  32   |   1  |   97% |
| investosphere/urls.py                                         |   4   |   0  |  100% |
| investosphere/wsgi.py                                         |   4   |   4  |    0% |
| manage.py                                                     |  12   |   2  |   83% |
| user_management/__init__.py                                   |   0   |   0  |  100% |
| user_management/admin.py                                      |   1   |   0  |  100% |
| user_management/apps.py                                       |   4   |   0  |  100% |
| user_management/crypto.py                                     |   7   |   1  |   86% |
| user_management/forms.py                                      |  21   |   1  |   95% |
| user_management/migrations/0001_initial.py                    |   5   |   0  |  100% |
| user_management/migrations/__init__.py                        |   0   |   0  |  100% |
| user_management/models.py                                     |   3   |   0  |  100% |
| user_management/newsapi.py                                    |  14   |   0  |  100% |
| user_management/registration.py                               |   7   |   0  |  100% |
| user_management/tests/test_crypto.py                          |  13   |   0  |  100% |
| user_management/tests/test_forms.py                           |  22   |   0  |  100% |
| user_management/tests/test_models.py                          |   6   |   0  |  100% |
| user_management/tests/test_newsapi.py                         |  19   |   0  |  100% |
| user_management/tests/test_views.py                           | 106   |   0  |  100% |
| user_management/urls.py                                       |   3   |   0  |  100% |
| user_management/views.py                                      |  64   |   8  |   88% |
| TOTAL                                                         | 730   | 235  |   68% |

The test coverage for this project currently stands at 68%. While automated testing has covered a significant portion of the codebase, additional testing through manual methods will be conducted to ensure comprehensive coverage.
