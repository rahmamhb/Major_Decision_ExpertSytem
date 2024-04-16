import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import RightArrow from '@mui/icons-material/ChevronRightRounded';
import './inputs3.css'; 

const Form3 = () => {
  const [marks, setMarks] = useState({
    history: '',
    ethics: '',
    arabic: '',
    philosophy: '',
    french: '',
    english: '',
    economics: '',
    accounting: '',
    math: '',
    chemistry: '',
    biology: '',
    psychology: '',
    statistics: '',
  });

  const handleMarksChange = (event) => {
    const { name, value } = event.target;
    setMarks((prevMarks) => ({
      ...prevMarks,
      [name]: value,
    }));
  };

  return (
    <div className='bg-back-pattern bg-no-repeat bg-cover flex justify-center text-xl h-[100vh]'>
      <div className=''></div>
      
      <div className='bg-form-pattern bg-no-repeat bg-contain w-[40vw] flex items-center justify-center'>
        <div className='grid-container'>
        <p className='font-bold hello'>Enter Marks for Each Subject</p> 
          {Object.entries(marks).map(([subject, mark]) => (
            <div key={subject} className='input-container'>
              <label htmlFor={subject}>{subject.charAt(0).toUpperCase() + subject.slice(1)}:</label>
              <input type="number" id={subject} name={subject} value={mark} onChange={handleMarksChange} required className='input' />
            </div>
          ))}
           <div>
        <Link to='/result'> 
          <span className='flex justify-center items-center bg-primaryPurple text-secondaryPurple rounded-full w-8 h-8 hover:opacity-90 next'><RightArrow /></span>
        </Link>
      </div>
        </div>
        
      </div>
     
    </div>
  );
};

export default Form3;
