import { useState } from 'react'
import './index.css'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Landing from './features/Landing';
const App = ()=> {


  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Landing></Landing>} />
        <Route path='*' element={<h1>404</h1>} />
      </Routes>

    </BrowserRouter>

  )
}

export default App
