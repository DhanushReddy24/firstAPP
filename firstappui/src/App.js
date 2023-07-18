import logo from './logo.svg';
import './App.css';
import {Routes, Route, useNavigate} from 'react-router-dom';
import Login from './authentication/login.jsx'
import Register from './authentication/signup.jsx'
import Welcome from './authentication/welcome.jsx'
import Tweet from './connections/tweet.jsx'


function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<Welcome />} />
        <Route path='/login' element={<Login />} />
        <Route path='/signup' element={<Register />} />
        <Route path='/tweet' element={<Tweet />} />
        <Route path='/tweet-new' element={<><Sidebar /><Feed /><Widgets /></>} />
    </Routes>
    </div>
  );
}

export default App;
