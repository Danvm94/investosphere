# **Investosphere**

## **Overview**

Investosphere is a virtual investment platform that allows users to simulate and plan their cryptocurrency investments without using real money. It provides a safe and risk-free environment for users to practice and experiment with various investment strategies in the cryptocurrency market.

![home-page](/README/home-page.gif)
[Investosphere Live Website](https://investosphere-d74500c2a8ca.herokuapp.com/) (Right-click to open in a new tab)

## **Project Goals**

This is my fourth  portfolio project, showcasing my proficiency in web development frameworks like Bootstrap and Django. My objective with this project is to demonstrate how I can leverage these skills effectively. I have chosen to create a cryptocurrency-focused website that integrates with real-time market data using external APIs.

The website will serve as a platform for users to explore, simulate, and plan cryptocurrency investments without using real money. It aims to provide a safe and educational environment for users to develop and refine their investment strategies. This project reflects my commitment to combining technical expertise with real-world applications, offering users a valuable tool for cryptocurrency investment planning and education.

## **Contents**

## **UX**

## **The Strategy Plane**
Investosphere aims to unite cryptocurrency enthusiasts, providing them with a platform to explore the world of cryptocurrencies comprehensively. Users will have the opportunity to simulate cryptocurrency investments, access market data, and refine their investment strategies. They can review and analyze crypto trends, create and manage virtual portfolios, and gain insights into the cryptocurrency market.

The platform's user-friendly design and visually appealing interface ensure an engaging and educational experience for users as they navigate the world of cryptocurrency investments. The primary goal is to empower users with the knowledge and tools they need to make informed investment decisions, all in a risk-free and supportive environment.

### **The Ideal User**
- Enthusiasts of cryptocurrencies and blockchain technology.
- Individuals interested in exploring cryptocurrency investments.
- Users looking to gain practical experience in cryptocurrency trading without using real money.
- Those who want to build and refine their cryptocurrency investment strategies.
- Users seeking to access market data and stay informed about cryptocurrency trends.
- Investors who value a secure and risk-free environment for investment planning and education.
- Individuals who want to create and manage virtual cryptocurrency portfolios.
- Users who enjoy analyzing crypto market data and making informed investment decisions.
- Anyone looking to engage with a community of like-minded cryptocurrency enthusiasts for sharing insights and experiences.

### **Site Goals**

- To offer users a platform to explore cryptocurrencies, both familiar and new.
- To enable users to simulate cryptocurrency investments and gain hands-on experience.
- To empower users with the tools to refine their cryptocurrency investment strategies.
- To provide users with access to real-time cryptocurrency market data.
- To create a secure and risk-free environment for cryptocurrency investment planning and education.
- To facilitate the creation and management of virtual cryptocurrency portfolios.
- To support users in making informed investment decisions based on data and analysis.

- [Back to top &uarr;](#contents)

## **Agile Planning**

This project was developed using agile methodologies, focusing on delivering small features across the project's duration. User Stories were prioritized under the labels "Must Have," "Should Have," and "Could Have."

This approach ensured that all essential requirements were addressed initially, providing a comprehensive foundation for the project. In certain cases, some "Could Have" features were implemented ahead of schedule, particularly if they were straightforward, such as Trending/Top Rated Movies. Other features were integrated based on available capacity and timing.

The project utilized a Kanban board created on Github projects, which can be accessed [here](https://github.com/users/Danvm94/projects/4). This board provided detailed information about project cards. All User Stories included a set of acceptance criteria to define the functionality required for story completion.
![home-page](/README/agile-project.png)

## **The Skeleton Plane**
#### **Wireframes**
For this project, wireframes were created using Balsamiq. While wireframes were developed primarily for the home page, the design for other pages naturally evolved from the base.html template and certain elements of the home webpage.

The wireframes served as a visual guide to outline the layout and structure of the home page, providing a clear representation of the overall design and user interface. This approach allowed for flexibility in designing additional pages, ensuring consistency in the user experience throughout the project.
<details><summary>Desktop</summary>

![desktop-home-wireframe](/README/desktop-home-wireframe.png)

</details>

<details><summary>mobile</summary>

![mobile-home-wireframe](/README/mobile-home-wireframe.png)

</details>

#### **Database Schema**

The database schema for this project includes the following models:

- The **Crypto** model stores information about cryptocurrencies.
  - Fields:
    - `name`: CharField for storing the name of the cryptocurrency (unique).
- The **Wallet** model represents user wallets, linked to the built-in User model. Each wallet contains information about the user's available dollars, and a timestamp of creation.
  - Fields:
    - `user`: One-to-One relationship with the User model.
    - `dollars`: Decimal field for storing dollar amounts.
    - `created_at`: Timestamp for creation.

- The **Cryptos** model represents cryptocurrency holdings of users, linked to the User model and the Crypto model. It stores information about the user's cryptocurrency holdings and the specific cryptocurrency's symbol.
  - Fields:
    - `user`: ForeignKey relationship with the User model.
    - `crypto`: ForeignKey relationship with the Crypto model.
    - `amount`: Decimal field for storing the cryptocurrency amount.
  - Additional Methods:
    - `formatted_amount`: Formats the cryptocurrency amount for display.
    - `symbol`: Property for retrieving the cryptocurrency's name.

- The **Transactions** model tracks user transactions, including deposits and withdrawals. It contains information about the user, transaction type, symbol, amount, and creation timestamp.
  - Fields:
    - `user`: ForeignKey relationship with the User model.
    - `type`: CharField for the transaction type.
    - `symbol`: CharField for the symbol (e.g., 'dollar').
    - `amount`: Decimal field for storing the transaction amount.
    - `created_at`: Timestamp for creation.
  - Additional Methods:
    - `formatted_amount`: Formats the transaction amount for display.

This schema defines the structure of your project's database, facilitating the management of user wallets, cryptocurrency holdings, and transaction records.

<iframe width="560" height="315" src='https://dbdiagram.io/embed/651c1404ffbf5169f0f1af91'> </iframe>