# fullstack_developer_capstone - Dealerships Review Portal

**Repository Name**: xrwvm-fullstack_developer_capstone  
**Project Name**: fullstack_developer_capstone  
**Developer**: Syukur  

---

## 🧭 Project Overview

This repository contains the complete implementation for the **Full Stack Cloud Developer Capstone Project** ("Cars Dealership Application"). The web application is built for a nationwide automotive dealership network with branches across the United States, enabling customers to browse branch locations, view detailed customer reviews with real-time sentiment analysis, and submit their own verified vehicle reviews.

The system is architected as an integrated cloud-native microservices solution combining **Django**, **React**, **Node.js/Express**, **MongoDB**, **SQLite**, and automated **GitHub Actions CI/CD**.

---

## 🌟 Architecture & Component Breakdown

1. **Dealerships Web Application (Django & React)**:
   - Django backend managing user authentication (Login, Register, Logout), SQLite persistence for Car Makes & Models, and rendering responsive templates.
   - React frontend components for interactive dealership browsing, state filtering, and review submissions.

2. **Dealerships & Reviews Service (Node.js / Express / MongoDB)**:
   - Dedicated microservice handling CRUD operations for dealership branches (`/fetchDealers`, `/fetchDealer/:id`, `/fetchDealers/:state`) and customer reviews (`/fetchReviews/dealer/:id`, `/insertReview`).
   - Backed by MongoDB for non-relational document storage.

3. **Sentiment Analyzer Microservice (Python Flask / NLTK / VADER)**:
   - Analyzes review sentiment (`positive`, `neutral`, `negative`) to provide automated customer feedback insights.

4. **DevOps & Continuous Integration**:
   - Automated GitHub Actions workflow (`.github/workflows/ci.yml`) performing automated Python (flake8) and JavaScript (ESLint/JSHint) linting on every push and pull request.

---

## 📁 Repository Structure

```text
xrwvm-fullstack_developer_capstone/
├── README.md                                          # Task 1: Project overview & metadata
├── django_server                                      # Task 2: Terminal log of active Django server
├── loginuser                                          # Task 5: cURL login command and output
├── logoutuser                                         # Task 6: cURL logout command and output
├── getdealerreviews                                   # Task 8: cURL dealer reviews command and output
├── getalldealers                                      # Task 9: cURL all dealers command and output
├── getdealerbyid                                      # Task 10: cURL dealer by ID command and output
├── getdealersbyState                                  # Task 11: cURL dealers by state command and output
├── getallcarmakes                                     # Tasks 14-15: cURL car makes & models output
├── analyzereview                                      # Task 16: cURL sentiment analyzer output
├── CICD                                               # Task 23: GitHub Actions CI/CD terminal log
├── deploymentURL                                      # Task 24: Deployed application URL
├── admin_login.png                                    # Task 12: Admin login screenshot
├── admin_logout.png                                   # Task 13: Admin logout screenshot
├── get_dealers.png                                    # Task 17: Dealers list before login
├── get_dealers_loggedin.png                           # Task 18: Dealers list after login
├── dealersbystate.png                                 # Task 19: Dealers filtered by state
├── dealer_id_reviews.png                              # Task 20: Dealer details & reviews
├── dealership_review_submission.png                   # Task 21: Review submission form
├── added_review.png                                   # Task 22: Posted review verification
├── deployed_landingpage.png                           # Task 25: Deployed landing page
├── deployed_loggedin.png                              # Task 26: Deployed logged-in page
├── deployed_dealer_detail.png                         # Task 27: Deployed dealer details
├── deployed_add_review.png                            # Task 28: Deployed added review
├── server/
│   ├── djangoproj/                                    # Django root configuration
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── djangoapp/                                     # Django dealership core application
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   └── frontend/
│       ├── static/
│       │   ├── About.html                             # Task 3: About Us page
│       │   └── Contact.html                           # Task 4: Contact Us page
│       └── src/
│           └── components/
│               └── Register/
│                   └── Register.jsx                   # Task 7: Registration component
└── LICENSE                                            # MIT License
```

---

## 🚀 Setup & Local Execution

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SyukurGit/xrwvm-fullstack_developer_capstone.git
   cd xrwvm-fullstack_developer_capstone
   ```

2. **Start Django Backend**:
   ```bash
   cd server
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver 8000
   ```

3. **Start Node.js & MongoDB Database Service**:
   ```bash
   cd server/database
   npm install
   node app.js
   ```

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
