import React from 'react';
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import Navbar from './component/Navbar';

import {
  BrowserRouter as Router,
  
} from "react-router-dom";
import Navigation from "./component/route/Navigation";

function App() {
  return (
    <Router>
      <Navbar/>
      
      <Navigation />
    </Router>
  );
}

export default App;