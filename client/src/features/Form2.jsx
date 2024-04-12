import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import RightArrow from '@mui/icons-material/ChevronRightRounded';

const Form2 = () => {
  const [personalityType, setPersonalityType] = useState('');
  const [yesNoSelection, setYesNoSelection] = useState('');

  const handlePersonalityChange = (event) => {
    setPersonalityType(event.target.value);
  };

  const handleYesNoChange = (event) => {
    setYesNoSelection(event.target.value);
  };

  return (
    <div className='bg-back-pattern bg-no-repeat bg-cover flex justify-center text-xl h-[100vh]'>
      <div className=''></div>
      <div className='bg-form-pattern bg-no-repeat bg-contain w-[40vw] flex items-center justify-center'>
        <div className='flex flex-col gap-4 '>
          <p className='font-bold'>Personality and Job Outlook</p>
          <div>
            <label htmlFor="selectPersonality">Select your personality type:</label>
            <select id="selectPersonality" value={personalityType} onChange={handlePersonalityChange}>
              <option value="">idk</option>
              <option value="workingWithPeople">Working with People</option>
              <option value="workingAlone">Working Alone</option>
              {/* Add more personality types as needed */}
            </select>
          </div>
          <div>
            <label>Job Outlook?</label>
            <div>
                <input
                type="radio"
                id="yes"
                value="yes"
                checked={yesNoSelection === "yes"}
                onChange={handleYesNoChange}
                />
                <label htmlFor="yes">Yes</label>
            </div>
            <div>
                <input
                type="radio"
                id="no"
                value="no"
                checked={yesNoSelection === "no"}
                onChange={handleYesNoChange}
                />
                <label htmlFor="no">No</label>
            </div>
            </div>

          <div>
            <Link to='/form3'> 
              <span className='flex justify-center items-center bg-primaryPurple text-secondaryPurple rounded-full w-8 h-8 hover:opacity-90 '><RightArrow /></span>
            </Link>
          </div>
          <p>Selected personality type: {personalityType}</p>
          <p>Selected yes/no: {yesNoSelection}</p>
        </div>
      </div>
    </div>
  );
};

export default Form2;
