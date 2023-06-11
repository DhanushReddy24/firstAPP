import React, { useState } from 'react';
import {useNavigate} from 'react-router-dom';
import Cookies from 'js-cookie';


function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();
  const csrfToken = Cookies.get('csrftoken');

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

    fetch("http://127.0.0.1:8000/login",{
      method:"POST",
      credentials: 'include',
      headers:{
        'Accept':'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
      body: JSON.stringify({
        'data_options': {
          'email': username,
          'password': password,
        }
      })
    })

    // Reset form fields
    //setUsername('');
    //setPassword('');

    let path = '/tweet/'; 
    //navigate(path);
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