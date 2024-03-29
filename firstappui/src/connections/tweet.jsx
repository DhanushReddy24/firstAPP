import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Logout from '../authentication/logout';

function Tweet() {

  const [TweetData, setTweetData] = useState([]);
  //let [authTokens, setAuthTokens] = useState(()=> localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null)
  //setAuthTokens(localStorage.getItem('authTokens'))
  
  const handleLogout = (event) => {
    localStorage.getItem('authTokens') ? localStorage.removeItem('authTokens') : console.log('No User to logout')
  };

  let getTweets = async() => {
    //console.log(authTokens.access)
    let response =await axios.get('http://127.0.0.1:8000/connections/tweet/',{
      'headers': { 
        'Content-Type':'application/json',
        'Access-Control-Allow-Origin' : '*',
        'Access-Control-Allow-Credentials' : 'false',
        'Access-Control-Allow-Methods':'PUT, POST, GET, DELETE, PATCH, OPTIONS',      
      }
    })
    let data = await response
    {console.log('response')}
    {console.log(response)}
    if(data.status===200){
      setTweetData(data.data)
      
      //console.log(response.data)
    }
  }

  useEffect(()=> {
    getTweets()
  }, [])

  //getTweets()

  return (
    <div>
      <h1>Tweets Page</h1>
      {console.log(TweetData)}
      {TweetData?.map(row => {
        {console.log(TweetData, "data", typeof TweetData)}
        return (
          <li key={row.id}>
            <tr key={row.id}>
              <td>{row.id}</td> 
              <td>{row.tweet}</td>
              <td>{row.user}</td>
              <td>{row.created_at} hrs</td>
            </tr>
          </li>
          
        )
      }
      )}
      <Logout/>
    </div>
  );
  }
  
  export default Tweet;