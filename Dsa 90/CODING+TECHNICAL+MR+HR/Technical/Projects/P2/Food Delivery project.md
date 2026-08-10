My Food Delivery application follows a client-server architecture using the MERN stack with TypeScript. The frontend and backend are completely separated and communicate through REST APIs.

On the frontend, I used React.js with TypeScript to build the user interface. The application uses React Router for navigation, Zustand for global state management, Axios for API communication, and Tailwind CSS with shadcn/ui for designing reusable UI components.

On the backend, I used Node.js and Express.js to develop REST APIs. The backend follows a modular architecture where each feature, such as User, Restaurant, Menu, and Order, has its own routes, controllers, and models. This separation makes the project easier to maintain and scale.

For the database, I used MongoDB with Mongoose. The main collections are Users, Restaurants, Menus, and Orders. These collections are connected using ObjectId references, allowing me to retrieve related data efficiently using Mongoose's populate() method.

For authentication, I implemented JWT-based authentication with cookies. After a successful login, the server generates a JWT token and stores it in a cookie. Every protected request passes through authentication middleware, which verifies the token before allowing access.

For image management, restaurant and menu images are uploaded using Multer and stored in Cloudinary, while only the image URLs are saved in MongoDB.

The application also integrates Stripe for online payments. When a customer places an order, the backend creates a Stripe Checkout Session. After payment, Stripe sends a webhook to the backend, which verifies the payment and updates the order status in the database. Additionally, Mailtrap is used to send email notifications for actions such as account verification.

Overall, the architecture separates the presentation layer, business logic, and database operations, making the application modular, scalable, and easier to maintain.