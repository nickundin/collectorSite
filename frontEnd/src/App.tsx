import React from 'react';
import Routing from './Components/Routing';
import './App.css';

// Row is being tested, MUST BE MOVED TO ITS CORRESPONDING PAGE
// COMPONENT LATER ON
// Navbar will NOT change on load so it must be above routing
export default function App(): JSX.Element {
  return (
    <div className="App">
          Header / Navbar goes here
          <Routing/>
    </div>
  );
}
