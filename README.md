# E-commerce Store

A clean, responsive, and functional e-commerce web application built using Django. This project features a robust product management system and straightforward order tracking.

## 🚀 Features

- **Product Catalog**: Browse products beautifully displayed by category with a carousel interface.
- **Shopping Cart System**: Add to cart, adjust quantities, and manage your items via a dynamic popup cart before checkout.
- **Express Checkout**: Simple, frictionless checkout process that captures customer metadata and generates reliable order tracking codes.
- **Order Tracker**: Follow the journey of your order live by using your Order ID and Email.
- **Contact Us Portal**: Get in touch directly with the store via a built-in messaging form.
- **Fully Responsive Design**: Optimized for mobile, tablet, and desktop viewing utilizing Bootstrap.
- 

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Database**: SQLite (Default) 
  This project is a fully functional E-commerce web application built primarily with Python (Django) on the backend and HTML/CSS/Bootstrap on the frontend.

It's designed to simulate a real-world online store where users can browse products, add them to a shopping cart, and place orders.

Here is a breakdown of its core features and what the project does:

🚀 Core Features
Product Catalog & Display:
Products are stored in the database and displayed dynamically on the homepage (/).
They are grouped by categories and showcased using an interactive sliding carousel.
Dynamic Shopping Cart:
Users can add items to their cart without leaving the page.
It features a popup cart that keeps track of the selected items and quantities before heading to checkout.
Checkout System:
A straightforward checkout page (/checkout/) where users can review their cart items, total amount, and enter their shipping details (Address, City, State, ZIP, Phone).
Order Tracking System:
After placing an order, users can go to the Tracker page (/tracker/). By entering their Order ID and Email address, they can see exactly where their order is (e.g., "the order has been placed").
Contact Us Portal:
A built-in messaging form (/contactus/) where visitors can send questions or feedback directly to the database.
User Authentication (Newly Added by Us):
Users can now create accounts (/signup/), log into the platform (/login/), and log out.
Admin Dashboard:
Powered by Django’s built-in admin panel, allowing store owners to add/edit/delete products, view orders, and manage order statuses without touching the code.


