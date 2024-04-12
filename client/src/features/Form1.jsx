import React, { useState } from 'react';
import '../index.css';
import RightArrow from '@mui/icons-material/ChevronRightRounded';
import { Link } from 'react-router-dom';

const Form1 = () => {
  const [selectedOption, setSelectedOption] = useState('');
  const [selectedSkill, setSelectedSkill] = useState('');

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  const handleSkillChange = (event) => {
    setSelectedSkill(event.target.value);
  };

  return (
    <div className='bg-back-pattern bg-no-repeat bg-cover flex justify-center text-xl h-[100vh]'>
    <div className=''></div>
    <div className='bg-form-pattern bg-no-repeat bg-contain w-[40vw] flex items-center justify-center'>
      <div className='flex flex-col gap-4 items-center justify-center'>
          <p className='font-bold'>Hi Bassmala! Please fill the following form attentively 
          <br></br>
          to get accurate results!</p>
          <div>
            <label htmlFor="selectOption">Select an interest:</label>
            <select id="selectOption" value={selectedOption} onChange={handleOptionChange}>
              <option value="">What are you interested in?</option>
              <option value="option1">Reading</option>
              <option value="option2">Art</option>
              <option value="option3">Entrepreneurship</option>
              <option value="option4">Mentoring</option>
              <option value="option5">Teaching</option>
              <option value="option6">Expertise</option>
              <option value="option7">Psychology</option>
              <option value="option8">Science</option>
              <option value="option9">Research</option>
              <option value="option10">Cultures</option>
              <option value="option11">Debate</option>
            </select>
          </div>
          <div>
            <label htmlFor="selectSkill">Select a skill:</label>
            <select id="selectSkill" value={selectedSkill} onChange={handleSkillChange}>
              <option value="">What skill do you have?</option>
              <option value="skill1">Public speaking</option>
              <option value="skill2">Critical thinking</option>
              <option value="skill3">Writing</option>
              {/* Add more skills as needed */}
            </select>
          </div>
          <div>
            <Link to='/form2'> 
              <span className='flex justify-center items-center bg-primaryPurple text-secondaryPurple rounded-full w-8 h-8 hover:opacity-90 '><RightArrow /></span>
            </Link>
          </div>
          <p>Selected option: {selectedOption}</p>
          <p>Selected skill: {selectedSkill}</p>
        </div>
      </div>
    </div>
  );
};

export default Form1;
