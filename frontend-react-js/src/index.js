import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const el_main = document.getElementsByTagName('main')[0];
const root = ReactDOM.createRoot(el_main);
root.render(<App />);
