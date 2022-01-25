# Testing

The following describes the testing steps taken during the development of [Druids Grove Dice](LINK TO FOLLOW).

Full details of the development of the site can be found in the [README](README.md).

# Table of Contents
> 1.  [Validators](#validation)
> 2.  [User Stories](#user-stories)
> 3.  [Manual Testing](#manual-testing)
> 4.  [Bugs](#bugs)

# Validators
## HTML
The site's HTML was validated using the [W3 Validator](https://validator.w3.org/nu/). The only issues raised were with elements created by the Stripe integration, particularly the `iframe`. 
## CSS
The site's CSS was validated with the [W3C CSS Validation](http://jigsaw.w3.org/css-validator/validator) service, and no errors were found.

## JS
The site's JavaScript was validated using [JSHint](https://jshint.com/), and no issues were found.

# User Stories
### **1. Navigation**
| ID         | As a…    | I want to…                             | So I can...                                        |
|------------|----------|----------------------------------------|----------------------------------------------------|
| US101      | Customer | View all available products            | Select products to purchase                        |
| US102      | Customer | Search products by name or description | Find a specific product to purchase                |
| US103      | Customer | View individual product details        | Learn more about it and decide if I want to buy it |
| US104      | Customer | View my order history                  | Refer back to my previous purchases                |
| US105      | Customer | Order and filter products              | Find a specific product to purchase                |

- Users can view all products by navigating to the Catalog page (US101).
- While on this page, they can order the products based on price or name (ascending or descending), and can filter by categories (US105).
- A search modal is available via the navbar at all times, with which a user can search the catalog. Search terms are checked against the product's name and description (US102).
- Users can view the details of any individual product by clicking on the corresponing 'More Info' button on the Catalog page (US102).
- Users (while logged in) can view their Order History on their Profile page (US104).

### **2. User Accounts**
| ID            | As a…     | I want to…                 | So I can...                                                                                 |
|---------------|-----------|----------------------------|--------------------------------------------------------------------------------------------|
| US201         | Site User | Register for an account    | Have a personalised account, and access different parts of the site   depending on my role |
| US202         | Site User | Login and logout           | Access my account securely                                                                 |
| US203         | Site User | Reset my password          | Securely regain access to my account if I forget my password                               |
| US204         | Customer  | Have a unique profile page | View my order history and saved delivery address, and update the address   if needed       |

- Users can create an account for the site by clicking the Register link in the navbar, and filling in the simple registration form (US201).
- Users can log in and out by following the corresponding links in the navbar (US202).
- Users can reset their password by clicking the 'Forgot Password' link on the Login page. They can then provide their email address and be sent a secure link to reset the password (US203).
- Users have unique Profile pages, where they can view their Order History and view and update their default delivery address (US204).

### **3. Purchasing**
| ID         | As a…    | I want to…                                                     | So I can...                                               |
|------------|----------|----------------------------------------------------------------|----------------------------------------------------------|
| US301      | Customer | Easily add the desired type and number of items to the cart    | Select the correct items for purchase                    |
| US302      | Customer | View the items and their quantities in my cart before purchase | Make sure that I have selected the correct items         |
| US303      | Customer | Change the quantities of items in my cart before purchase      | Make changes to the cart's contents before checkout      |
| US304      | Customer | Enter payment and delivery information                         | Checkout easily, securely and with confidence            |
| US305      | Customer | View an order confirmation page on checkout                    | Confirm my order has gone through and is correct         |
| US306      | Customer | Receive a confirmation email on checkout                       | Keep a copy of the order confirmation for my own records |

- Customers can add a chosen quantity of items to their cart on the Product Details page (US301).
- They can then see the items and their quantities on the Shopping Cart page before checkout. The quantities can again be adjusted at this point (US302, US303).
- Users can enter their payment and delivery info on the Checkout page (US304)
- Upon successfully completing a purchase, the user is shown an Order Confirmation page (US305), and is sent an Order Confirmation email (US306).

### **4. Product Management**
| ID                 | As a…      | I want to…             | So I can...                                                      |
|--------------------|------------|------------------------|-----------------------------------------------------------------|
| US401              | Site Owner | Add products           | Make new products available for site users to view and purchase |
| US402              | Site Owner | Edit & update products | Change product names and descriptions as needed                 |
| US403              | Site Owner | Delete products        | Remove products from the store front as needed                  |

- The site owner (and only the site owner) can add, edit update and delete products by following the clearly marked links on the Catalog and Product Details pages. These links are not displayed to users who do not have the adequate permissions to use them (US401, US402, US403).


### **5. Communication**
| ID                 | As a…      | I want to…             | So I can...                                                   |
|--------------------|------------|------------------------|---------------------------------------------------------------|
| US501              | Site User  | View Blog Posts                    | Keep up to date with the latest news and products |
| US502              | Site Owner | Make Blog Posts                    | Provide updates on the business and new products  |
| US503              | Site Owner | Edit, Update and Delete Blog Posts | Provide more information, correct typos and mistakes and remove older posts|
| US504              | Site User | Leave comments on Blog Posts | Engage with the posted content, and interact with other users |

- All Users can see a list of the most recentblog posts on the Blog page, and can clickthrough for more information (US501).
- The site owner can add, edit and delete blog posts by following the clearly marked links on the Blog and Post Details pages. These links are not displayed to users who do not have the adequate permissions to use them (US502, US503).
- Logged in Users can leave comment on an individual blog post by submitting the form at the bottom of each post (US504). Logged out users are instead encouraged to log in, and will be redirected back to the post should they do so.

# Manual Testing
## Testing Environments

Development and initial testing took place on a HP 250 G6 Laptop (Windows 10) in Chrome. Subsequent testing took place across the following devices, operating systems and browsers:

- Devices:

  - HP 250 G6 Laptop (Windows 10)
  - MacBook Pro 2013 (MacOS)
  - OnePlus 6T (Oxygen OS)
  - Samsung Galaxy S9 (Android)
  - Apple iPad (iPadOS 14)
- Browsers:

  - Chrome
  - Firefox
  - Edge
  - Safari

## Functionality
The basic functionality of the site (user onboarding and purchasing items) was manually tested extensively, per the User Story tests above. Additionaly, the following points were checked.
### CRUD Functions
- Users can Create accounts.
- Users can change (Update) their passwords via password reset.
- Users can change (Update) their default delivery address.
- All products can be viewed on the Catalog page (Read).
- The site owner can add (Create), edit (Update), and Delete products from the storefront.
### Links
- All internal links are functioning correctly.
- All external links open in a new tab.
- There are no references or links to pages that do not exist.
- There are no broken links.
### Forms
- All forms submit correctly.
- All forms validate the users input and provide clear feedback when there is an issue.
### Email
- Email Verification, Forgot Password and Order Confirmation emails were all checked and found to be working.

## Usability
### Navigation
- The navigation bar is always present, allowing users to move around the site with ease.
- A link to the home page is always present.
- The sites buttons and form inputs are easily identified and interacted with.
- The purpose of all pages of the site can be easily understood.
### Content
- The content of the site has been checked for spelling and grammar mistakes in an attempt to ensure it is as easy to parse as possible.
- Any instructions for the user, seen during the account creation or purchase processes, are clear and easy to follow.

## Security
The site's security features were tested, with the following findings:
- Logged out Users were not able to access a Profile page
- Only the current logged in user can access their Order History
- Only users with the appropriate permissions can see and use the options to add, edit and delete products.

## Compatability & Responsiveness
- The site was checked at a variety of screen sizes and in different browsers.
- All testing steps listed were taken on all devices and browsers outlined above, unless otherwise stated.

# Bugs
## Fixed
- Bug: Toasts not disappearing when dismissed.
    - Solution: Added custom JS to change the element's `display` to `none` when the close (x) is clicked.
- Bug: Users could access each others Order Histories via the URL.
    - Solution: Added a check to the order history view that confirmed that the current user matches the user on the order, and if not redirects them away.