import React from 'react'
 
function Sidebar(){
    return (
        <div>
                <div className="sidenav active">
        <div className="div">The Lunar Project</div>
        <img src={logo} alt="logo"
        className='logo'/>
        <ul className='list'>
            <li>
               <a href="/home">Home</a>
            </li>
            <li>
               <a href="/calendar">Calendar</a>
            </li>
            <li>
               <a href="/classes">Classes</a>
            </li>
            <li>         
               <a href="/appointment">Appointments</a>
            </li>
            <li>
               <a href="/assignments">Assignments</a>
            </li>
            <li>
               <a href="/announcements">Announcements</a>
            </li>
            <li>
               <a href="/">Settings</a>
            </li>
            <li className='red'>
               <a href="/">Log Out</a>
            </li>
        </ul>
        </div>
    );
 
        </div>
    )
}

export default Sidebar