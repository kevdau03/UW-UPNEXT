import './App.css';
import React from 'react';
import ChatWindow from './components/ChatBox';
import logo from './images/UPNEXT_LOGO.png'
function App() {
  return (
    <div className="App">
      <img src={logo} alt="Logo" className='logo' style={{width: "30", height: "50", alignContent: "left"}}/>
      <header className="App-header">
        <ChatWindow/>
      </header>
    </div>
  );
}

export default App;
