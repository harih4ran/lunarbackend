import React from 'react';
import './App.css';
import logo2 from './logo 2.png'
function login(){
    return(
        <div className="main">
            <div className='sub-main'>
                <div>
               <div className='imgs'>
                  <div className='container-image'>
                  <img src={logo2} alt="profile" className="profile"/>
        </div>
        </div>
        <div>
       <h1>Lunar Project</h1>
        <div>
            <input type="text" placeholder="Email or ID number" className="name"/>
        </div>
        <div className="secondinput">
            <input type="password" placeholder="Password" className="name"/>
        </div>
        <button type="button">Log In</button>
        <p>or</p>
        <p><a href="signup">Create Account</a></p>
      </div>
     </div>

  </div>
 </div>
);
}
export default login;
