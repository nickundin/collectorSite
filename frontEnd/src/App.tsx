import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import NotFoundPage from './Components/NotFoundPage';
import HomePage from './Components/HomePage';
import './App.css';

export default function App() {
  return (
    <div className="App">
          React Routing -- No reload every time page changes.
          Currently a test, will likely move to Routing component.
          <Router>
            <Switch>
                <Route exact path="/" component={HomePage} />
                <Route component={NotFoundPage} />
            </Switch>
          </Router>
    </div>
  );
}
