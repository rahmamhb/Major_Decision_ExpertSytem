import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import RightArrow from '@mui/icons-material/ChevronRightRounded';
import './inputs.css'; // Import the CSS file

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
    setMarks({ ...marks, [name]: value });
  };

  return (
    <div className='bg-back-pattern bg-no-repeat bg-cover flex justify-center text-xl h-[100vh]'>
      <div className=''></div>
      <div className='bg-form-pattern bg-no-repeat bg-contain w-[40vw] flex items-center justify-center'>
        <div className='flex flex-col gap-4 '>
          <p className='font-bold'>Enter Marks for Each Subject</p>
          {Object.entries(marks).map(([subject, mark]) => (
            <div key={subject} className='input-container'>
              <label htmlFor={subject}>{subject.charAt(0).toUpperCase() + subject.slice(1)}:</label>
              <input type="number" id={subject} name={subject} value={mark} onChange={handleMarksChange} />
            </div>
          ))}
          <div className='button-container'>
            <Link to='/result'> 
              <button className='submit-button flex justify-center items-center bg-primaryPurple text-secondaryPurple rounded-full w-8 h-8 hover:opacity-90 '><RightArrow /></button>
            </Link>
          </div>
          {/* Display marks */}
          {/* <p>Marks:</p>
          <ul>
            {Object.entries(marks).map(([subject, mark]) => (
              <li key={subject}>{subject}: {mark}</li>
            ))}
          </ul> */}
        </div>
      </div>
    </div>
  );
};

export default Form3;
