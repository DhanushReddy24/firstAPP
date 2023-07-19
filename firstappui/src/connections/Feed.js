import React, { useState, useEffect } from "react";
import Post from "./Post";
import "./Feed.css";
import FlipMove from "react-flip-move";
import axios from 'axios';


function Feed() {
  const [TweetData, setTweetData] = useState([]);
  //let [authTokens, setAuthTokens] = useState(()=> localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null)
  //setAuthTokens(localStorage.getItem('authTokens'))

  let getTweets = async() => {
    //console.log(authTokens.access)
    let response =await axios.get('http://127.0.0.1:8000/connections/tweet/',{
      'headers': { 
        'Content-Type':'application/json',
        //'Authorization': 'JWT ' +String(authTokens.access) 
      }
    })
    let data = await response
    //{console.log(response)}
    if(data.status===200){
      setTweetData(data.data)
      
      //console.log(response.data)
    }
  }
  useEffect(()=> {
    getTweets()
  }, []);

  
  return (
    <div className="feed">
      <div className="feed__header">
        <h2>Home</h2>
      </div>

      <FlipMove>
        {TweetData.map((tweet) => (
          <Post
            key={tweet.id}
            username={tweet.user}
            tweet={tweet.tweet}
            time={tweet.created_at}
          />
        ))}
      </FlipMove>
    </div>
  );
}

export default Feed;
