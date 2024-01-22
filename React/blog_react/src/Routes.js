// Routes.js

import React from 'react';
import { Route, Routes } from 'react-router-dom';
import App from './App'; // Import your App component

const MyRoutes = () => {
  return (
    <Routes>
      <Route path="/app/:name" element={<App/>} />
      {/* Add other routes if needed */}
    </Routes>
  );
};

export default MyRoutes;
