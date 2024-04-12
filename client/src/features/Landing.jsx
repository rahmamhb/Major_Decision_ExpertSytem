import { useState } from 'react'
import '../index.css'
import RightArrow from '@mui/icons-material/ChevronRightRounded';
import { Link } from 'react-router-dom';
const Landing = ()=> {

  const [name , setName] = useState('')
  return (
    <div className='bg-back-pattern bg-no-repeat bg-cover flex justify-center text-xl h-[100vh]'>
      <div className=''></div>
      <div className='bg-landing-pattern bg-no-repeat w-[75vw] flex items-center justify-end'>
        <div className='flex flex-col gap-4 '>
          <p className='font-bold'>Welcome to Your Pathway to Your Future Major!</p>
          <div className='flex flex-col gap-4 '>
            <span className='flex flex-col gap-6'>
              <p className='w-[550px] text-lg'>Our Expert System helps Students choose their future majors in university depending on their answers to a bunch of questions.</p>
              <p className='text-lg'>Before we delve into the questions, please enter your name:</p>
              <input type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primaryPurple focus:border-primaryPurple block p-2.5 w-[400px] " value={name} onChange={(e)=>setName(e.target.value)} placeholder="your name" required />
            </span>
            <Link to='/form1'> 
              <span className='flex justify-center items-center bg-primaryPurple text-secondaryPurple rounded-full w-8 h-8 hover:opacity-90 '><RightArrow></RightArrow></span>
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Landing
