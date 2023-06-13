import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Tweet() {

  const [TweetData, setTweetData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/connections/tweet/')
      .then(response => {
      
    if(response.status===200){
      setTweetData(response.data)
      
      //console.log(response.data)
    }
  }
      )}, []);

    return (
    <div>
      <h1>Tweets Page</h1>

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

    </div>
    );
  }
  
  export default Tweet;