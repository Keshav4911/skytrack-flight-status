few of the files are too large to be commited through simple basic commands
SkyTrack: Real-time Flight Status and Notifications System
SkyTrack is a comprehensive web application that provides real-time flight status updates and notifications to users. It allows users to search for flights, view their current status, and set up personalized notifications for flight changes.
Features

Real-time flight status display
Flight search functionality
User-customizable notification preferences (email, SMS, push notifications)
Interactive 3D globe visualization of flight paths (concept)

Tech Stack
Frontend

React.js
React Router for navigation
Axios for API requests
Tailwind CSS for styling
Firebase Cloud Messaging for push notifications

Backend

Node.js
Express.js
MongoDB for database
Mongoose as ODM (Object Document Mapper)
Aviation Stack API for flight data

Additional Tools and Libraries

dotenv for environment variable management
cors for handling Cross-Origin Resource Sharing
Three.js for 3D globe visualization (concept)
tensorflow

Project Structure
Copyflight-status-app/
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── App.js
│       ├── index.js
│       └── firebase.js
└── backend/
    ├── models/
    ├── routes/
    ├── services/
    ├── .env
    └── server.js
Key Components

Flight Status Display: Utilizes the Aviation Stack API to fetch and display real-time flight information.
Search Functionality: Allows users to search for specific flights by flight number.
Notification System: Supports email, SMS, and push notifications (using Firebase Cloud Messaging) for flight updates.
User Preferences: Users can set and manage their notification preferences.
3D Globe Visualization: (Concept) An interactive 3D globe showing flight paths using Three.js.

Setup and Installation

Clone the repository
Set up the frontend:
Copycd frontend
npm install
npm start

Set up the backend:
Copycd backend
npm install
npm start

Set up environment variables:

Create a .env file in the backend directory
Add necessary variables (MongoDB URI, Aviation Stack API key, etc.)



Future Enhancements:
Add more detailed flight information
Enhance 3D globe visualization
Add unit and integration tests
Set up CI/CD pipeline

Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page] if you want to contribute.
License
[MIT]
This project was developed as part of the Hack to Hire 2024 case study for full stack developers.
