import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import Home from './pages/Home'
import Courses from './pages/Courses'
import NavBar from './components/NavBar'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Login from './pages/Login'
import Signup from './pages/Signup'


function App() {

  return (
    <>
        <NavBar />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/courses' element={<Courses />}/>
          <Route path='/login' element={<Login />}/>
          <Route path='/signup' element={<Signup />}/>

        </Routes>
    </>
  )
}

export default App
