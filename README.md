# E-commerce Store

A clean, responsive, and functional e-commerce web application built using Django. This project features a robust product management system and straightforward order tracking.

## 🚀 Features

- **Product Catalog**: Browse products beautifully displayed by category with a carousel interface.
- **Shopping Cart System**: Add to cart, adjust quantities, and manage your items via a dynamic popup cart before checkout.
- **Express Checkout**: Simple, frictionless checkout process that captures customer metadata and generates reliable order tracking codes.
- **Order Tracker**: Follow the journey of your order live by using your Order ID and Email.
- **Contact Us Portal**: Get in touch directly with the store via a built-in messaging form.
- **Fully Responsive Design**: Optimized for mobile, tablet, and desktop viewing utilizing Bootstrap.
- **Vercel Ready**: Pre-configured for seamless Serverless deployments on Vercel.

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Database**: SQLite (Default) 
- **Deployment**: Vercel

## 📦 Local Installation

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python ecommerce/manage.py migrate
   ```
4. Run the local development server:
   ```bash
   python ecommerce/manage.py runserver
   ```
   Navigate to `http://localhost:8000/` in your browser.

## 🌐 Deploy to Vercel

1. Push this repository to your GitHub account.
2. Link the repository to your Vercel account.
3. Vercel will automatically detect the settings in `vercel.json` and build the Django app securely.
