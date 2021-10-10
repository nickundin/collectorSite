import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import './index.css';
import App from './App';
import { ItemProvider } from './Components/Context';

ReactDOM.render(
  <React.StrictMode>
    <ItemProvider>
        <Router>
            <App />
        </Router>
    </ItemProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
