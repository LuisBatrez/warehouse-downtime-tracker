# Warehouse Downtime Tracker

A Flask-based warehouse operations dashboard used to track equipment downtime, monitor active issues, and analyze operational trends through interactive data visualizations.

## Overview

This application was inspired by real warehouse production environments where equipment failures and downtime directly impact operational efficiency. The system allows users to report machine issues, monitor open incidents, search historical records, and visualize downtime statistics through dashboards and graphs.

## Features

### Dashboard
- View warehouse downtime statistics
- Monitor currently open issues
- Display downtime trends using interactive charts
- Track operational metrics in real time

### Issue Management
- Submit new equipment issue reports
- Update issue statuses
- Track downtime duration
- Store issue history in SQLite database

### Database Search
- Search reports by:
  - Machine name
  - Issue category
  - Shift
  - Status
- Filter historical downtime records
- View detailed issue information

### Navigation
- Top navigation bar for page routing
- Separate dashboard and database pages
- Dedicated issue submission page

## Planned Visualizations

- Downtime by machine
- Downtime by issue category
- Open vs resolved issues
- Downtime trends over time
- Shift performance comparisons

## Tech Stack

- Python
- Flask
- SQLite
- Pandas
- Plotly
- HTML/CSS

## Project Structure

```bash
warehouse-downtime-tracker/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   ├── style.css
│   ├── dashboard.css
│   └── scripts.js
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_issue.html
│   ├── database.html
│   ├── search.html
│   ├── issue_detail.html
│   └── edit_issue.html
│
├── charts/
│   └── chart_generator.py
│
├── utils/
│   ├── filters.py
│   └── statistics.py
│
├── data/
│   └── database.db
│
└── screenshots/
    └── dashboard-preview.png
```

## Installation

Clone the repository:

```bash
git clone https://github.com/LuisBatrez/warehouse-downtime-tracker.git
cd warehouse-downtime-tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open in browser:

```bash
http://127.0.0.1:5000
```

## Future Improvements

- Authentication system
- CSV export functionality
- Real-time issue tracking
- Maintenance scheduling
- Mobile responsive layout
- Role-based access control

## Author

Luis Batrez