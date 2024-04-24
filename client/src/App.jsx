import { useState } from 'react'
import './index.css'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Landing from './features/Landing';
import Result from './features/Result';
import Form from './features/Form';
const App = ()=> {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Landing></Landing>} />
        <Route path='/result' element={<Result></Result>} />
        <Route path='/form' element={<Form/>} />
        <Route path='*' element={<h1>404</h1>} />
      </Routes>

    </BrowserRouter>

  )
}

export default App
