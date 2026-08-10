One of my major projects is a Full-Stack Job Portal application built using the MERN stack. The goal of the project is to connect recruiters and job seekers on a single platform. Recruiters can register their companies, post and manage job openings, view applicants, and update application statuses, while job seekers can browse jobs, view job details, and apply for relevant positions.

On the frontend, I used React.js along with Redux Toolkit for global state management, Redux Persist to retain selected Redux state across page refreshes, Axios for API communication, and React Router for client-side routing.

On the backend, I developed REST APIs using Node.js, Express.js, MongoDB, and Mongoose following the MVC architecture, with separate models, controllers, routes, and middleware to keep the code modular.

Authentication is implemented using JWT. After a successful login, the server generates a JWT and stores it in a cookie. For protected APIs, an authentication middleware verifies the token and attaches the authenticated user's ID to the request before passing control to the controller.

I implemented CRUD functionality for companies and jobs. Recruiters can create and update company profiles, upload company logos using Multer and Cloudinary, and post multiple jobs. Jobs are associated with companies using MongoDB ObjectId references.

<!-- For job search, I implemented case-insensitive searching using MongoDB regular expressions on fields such as job title and description. Since this is a learning project with moderate data, regex works well, though for large-scale applications I would consider text indexes or a dedicated search solution. -->

Job seekers can apply for jobs, and recruiters can review applicants and update their application status as Pending, Accepted, or Rejected. Relationships between users, companies, jobs, and applications are maintained using ObjectId references, while Mongoose Populate is used to retrieve related document details when needed.

Overall, this project gave me practical experience in designing REST APIs, implementing authentication, managing database relationships, handling file uploads, building protected routes, and developing a modular full-stack application.


<!-- overview -->
One of my major projects is a Full-Stack Job Portal application built using the MERN stack. The main objective is to connect recruiters and job seekers on a single platform. Recruiters can register their companies, post and manage jobs, and review applicants, while job seekers can search jobs, view job details, and apply online.

On the frontend, I used React.js with Redux Toolkit for state management, Redux Persist to retain selected Redux state after refresh, Axios for API communication, and React Router for navigation.

On the backend, I built REST APIs using Node.js, Express.js, MongoDB, and Mongoose following the MVC architecture. Authentication is implemented using JWT, where the token is stored in cookies, and protected APIs use middleware to verify the token before processing requests.

I also implemented CRUD operations for companies and jobs, file uploads using Multer and Cloudinary, and linked users, companies, jobs, and applications using MongoDB ObjectId references. Recruiters can update application statuses, and job seekers can search and apply for jobs. This project gave me practical experience in authentication, REST API development, database relationships, and full-stack application development.