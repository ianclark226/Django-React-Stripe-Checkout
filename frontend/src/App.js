import React from "react";
import HomePage from "./HomePage";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


const App = () => {
  return (
    <Router>
    
      <Routes>
      <Route path='/' element={<HomePage />}/> 
      </Routes>
    </Router>
  )
}

export default App;

  

 
