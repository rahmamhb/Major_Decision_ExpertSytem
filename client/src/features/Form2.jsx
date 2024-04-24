import React, { useState } from 'react';
import RightArrow from '@mui/icons-material/ChevronRightRounded';
import './inputs2.css';

const Form2 = ({ goNext, goBack }) => {
  const [data, setData] = useState({
    personalityType: '',
    yesNoSelection: '',
  });

  const handleData = (event) => {
    const { id, value } = event.target;
    setData({ ...data, [id]: value });
  };

  return (
    <div className='bg-back-pattern bg-no-repeat bg-cover flex justify-center text-xl h-[100vh]'>
      <div className=''></div>
      <div className='bg-form-pattern bg-no-repeat bg-contain w-[40vw] flex items-center justify-center'>
        <div className='flex flex-col gap-4 '>
          <p className='font-bold'>Personality and Job Outlook</p>
          <div>
            <label htmlFor="selectPersonality">Select your personality type:</label>
            <select id="personalityType" value={data.personalityType} onChange={handleData}>
              <option value="">Select personality type</option>
              <option value="Flexible">Flexible</option>
              <option value="WorkingWithPeople">Working with People</option>
              <option value="WorkingAlone">Working Alone</option>
              {/* Add more personality types as needed */}
            </select>
          </div>
          <div>
            <label className='job'>Job Outlook?</label>
            <br />
            <div className='yesno1'>
              <input
                type="radio"
                id="yesNoSelection"
                value="yes"
                checked={data.yesNoSelection === "yes"}
                onChange={handleData}
              />
              <label htmlFor="yes">Yes</label>
            </div>
            <div className='yesno2'>
              <input
                type="radio"
                id="yesNoSelection"
                value="no"
                checked={data.yesNoSelection === "no"}
                onChange={handleData}
              />
              <label htmlFor="no">No</label>
            </div>
          </div>
          <button onClick={() => goNext(data)}>
            <span className='flex justify-center items-center bg-primaryPurple text-secondaryPurple rounded-full w-8 h-8 hover:opacity-90 '><RightArrow /></span>
          </button>
          {/*<div>
            <Link to='/form3'> 
              <span className='flex justify-center items-center bg-primaryPurple text-secondaryPurple rounded-full w-8 h-8 hover:opacity-90 '><RightArrow /></span>
            </Link>
          </div>
          <p>Selected personality type: {data.personalityType}</p>
          <p>Selected yes/no: {data.yesNoSelection}</p> */}
        </div>
      </div>
    </div>
  );
};

export default Form2;
