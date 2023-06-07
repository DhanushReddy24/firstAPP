import React, { useState } from 'react';

function LoginForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Perform login logic or API call with username and password
    console.log('Username:', username);
    console.log('Password:', password);
    // Reset form fields
    setUsername('');
    setPassword('');
  };

  return (
  <div>
    <p>Hello</p>
  </div>
  );
}

export default LoginForm;