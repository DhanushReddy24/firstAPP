import React, { useState } from 'react';
import {useNavigate} from 'react-router-dom';
import axios from 'axios';


function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

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

    axios.post('http://127.0.0.1:8000/api/token/', {
      'email': username,
      'password': password

    }).then(function (response) {
      localStorage.setItem('authTokens', JSON.stringify(response.data))
      console.log(response.data);
    })

    // Reset form fields
    //setUsername('');
    //setPassword('');

    let path = '/tweet/'; 
    navigate(path);
  };

  return (
  <div>
    <p>Hello</p>

    <form onSubmit={handleSubmit}>
      <label>Username</label>
      <input type="text" name="email" onChange={handleUsernameChange }/><br/>

      <label>Password</label>
      <input type="password" name="password" onChange={handlePasswordChange} /><br/>

      <input type="submit" value="Login" /><a href="/signup/" class="ml-2">Register</a>
    </form>

  </div>
  );
}

export default Login;