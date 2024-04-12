import { useState } from 'react'
import './index.css'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Landing from './features/Landing';
import Result from './features/Result';
import Form1 from './features/Form1';
import Form2 from './features/Form2';
import Form3 from './features/Form3';
const App = ()=> {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Landing></Landing>} />
        <Route path='/result' element={<Result></Result>} />
        <Route path='/form1' element={<Form1/>} />
        <Route path='/form2' element={<Form2/>} />
        <Route path='/form3' element={<Form3/>} />
        <Route path='*' element={<h1>404</h1>} />
      </Routes>

    </BrowserRouter>

  )
}

export default App
