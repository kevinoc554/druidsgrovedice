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

# Manual Testing

# Bugs