import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import RightArrow from '@mui/icons-material/ChevronRightRounded';
import './inputs1.css';

const Form1 = ({ goNext }) => {
  const [data, setData] = useState({
    interests : '',
    skill :'',
    personalityType:'',
    yesNoSelection:'',
  });

  const handleData = (event) => {
    const { id, value } = event.target;
    setData({ ...data, [id]: value });
  };

  return (
    <div className='bg-back-pattern bg-no-repeat bg-cover flex justify-center text-xl h-[100vh]'>
      <div className=''></div>
      <div className='bg-form-pattern bg-no-repeat bg-contain w-[40vw] flex items-center justify-center'>
        <form className='flex flex-col gap-4 items-center justify-center'>
          <p className='font-bold HI'>
            Hi Bassmala! Please fill the following form 
            <br />
            attentively to get accurate results!
          </p>
          <div>
            <label htmlFor="selectOption">Select an interest:</label>
            <select id="interests" value={data.interests} onChange={handleData}>
              <option value="">What are you interested in?</option>
              <option value="Reading">Reading</option>
              <option value="Art">Art</option>
              <option value="Entrepreneurship">Entrepreneurship</option>
              <option value="Mentoring">Mentoring</option>
              <option value="Teaching">Teaching</option>
              <option value="Expertise">Expertise</option>
              <option value="Psychology">Psychology</option>
              <option value="Science">Science</option>
              <option value="Research">Research</option>
              <option value="Cultures">Cultures</option>
              <option value="Debate">Debate</option>
            </select>
          </div>
          <div>
            <label htmlFor="selectSkill">Select a skill:</label>
            <select id="skill" value={data.skill} onChange={handleData} className='editinput'>
              <option value="">What skill do you have?</option>
              <option value="Public speaking">Public speaking</option>
              <option value="Critical thinking">Critical thinking</option>
              <option value="Writing">Writing</option>
            </select>
          </div>
          <button onClick={() => goNext(data)}>
            <span className='flex justify-center items-center bg-primaryPurple text-secondaryPurple rounded-full w-8 h-8 hover:opacity-90 '><RightArrow /></span>
          </button>
          {/*<div>
            <Link to='/form2'> 
              <span className='flex justify-center items-center bg-primaryPurple text-secondaryPurple rounded-full w-8 h-8 hover:opacity-90 '><RightArrow /></span>
            </Link>
          </div>
          <p>Selected option: {selectedOption}</p>
          <p>Selected skill: {selectedSkill}</p> */}
        </form>
      </div>
    </div>
  );
};

export default Form1;
