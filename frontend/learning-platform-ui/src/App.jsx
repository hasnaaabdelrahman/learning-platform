import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import Home from './pages/Home'
import NavBar from './components/NavBar'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'


function App() {

  return (
    <>
        <NavBar />
        <Routes>
          <Route path='/' element={<Home />} />
        </Routes>
    </>
  )
}

export default App
