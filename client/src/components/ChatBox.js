import React, { useState } from 'react';
import axios from 'axios';

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState('');
  const backend_url = "http://localhost:5000"
  const sendMessage = async () => {
    if (!userInput) return;

    try {
      // Send user message to server-side API endpoint (replace with your endpoint URL)
      const response = await axios.post(`${backend_url}/api/user_prompt`, { message: userInput });

      // Update chat window with user message
      setMessages([...messages, { user: true, text: userInput }]);
      setUserInput('');

      // Handle Gemini response (implementation depends on your server-side logic)
      const geminiResponse = response.message; // Replace with actual response data structure
      if(geminiResponse !== undefined){ 
        setMessages([...messages, { user: false, text: geminiResponse }]);
      }else{
        setMessages([...messages, { user: false, text: "Error getting events" }]);
      }
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div className="chat-window">
      {messages.map((message) => (
        <div key={message.text} className={`message ${message.user ? 'user' : 'gemini'}`}>
          {message.text}
        </div>
      ))}
      <div className="input-container">
        <input
          type="text"
          value={userInput}
          onChange={(e) => {
            setUserInput(e.target.value)
        }}
          placeholder="Type your message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default ChatWindow;