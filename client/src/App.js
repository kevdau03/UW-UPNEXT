import './App.css';
import React, { useState } from 'react';
import axios from 'axios';
import ChatWindow from './components/ChatBox';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ChatWindow/>
      </header>
    </div>
  );
}

export default App;
