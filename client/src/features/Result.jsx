import { useState , useEffect} from 'react'
import '../index.css'
import { Link } from 'react-router-dom';
const Result = ()=> {

  const [majors , setMajors] = useState(['law' , 'teaching'])
  useEffect(()=>{
    fetchMajors()
  },[])

 const fetchMajors = ()=>{

 }

 const handleHover = (major) => {
    const paragraph = document.getElementById(`${major}-paragraph`);
    paragraph.style.display = 'block';
    paragraph.style.visibility = 'visible';
  };

  const handleLeave = (major) => {
    const paragraph = document.getElementById(`${major}-paragraph`);
    paragraph.style.display = 'none';
  };
  return (
    <div className='bg-back-pattern bg-no-repeat bg-cover flex justify-center text-xl h-[100vh]'>
      <div className='bg-result-pattern bg-no-repeat bg-contain w-[40vw] flex items-center justify-center'>
        <div className='flex flex-col gap-4 items-center justify-center'>
          <p className='font-extrabold'>Your Results !</p>
          <p className='text-lg w-72 text-center'>You have a great potential to succeed in the following majors: </p>              
          <ol className='list-decimal'>
            { majors.map((major)=>
                    ( 
                    <div className='flex flex-col items-center'>
                        <li onMouseEnter={() => handleHover(major)} onMouseLeave={() => handleLeave(major)} >{major}</li>
                        {major.toUpperCase() === 'LAW' && (<p className='text-xs text-center w-[350px] ' id={`${major}-paragraph`}>With a good understanding of history or ethics and strong debate skills, coupled with critical thinking abilities, you exhibit the traits necessary for a successful career in law. Your desire to serve society adds to your suitability for this field.</p>)}
                        {major.toUpperCase() === 'LITERATURE' && (<p>Your excellence in English or French, along with a passion for reading and writing, indicates a strong inclination towards literature. Your preference for working alone aligns with the independent nature of literary studies.</p>)}
                        {major.toUpperCase() === 'CS' && (<p className='text-xs text-center w-[350px] ' id={`${major}-paragraph`}>you have shown a strong knowledge in problem solving, reinforced by a very good base in mathematics and physics. Your critical thinking skills and ability to work alone make you well-suited for this field.</p>)}
                        {major.toUpperCase() === 'BUSINESS' && (<p className='text-xs text-center w-[350px] ' id={`${major}-paragraph`}>Your proficiency in entrepreneurship and marketing, coupled with critical thinking abilities, positions you well for success in the dynamic field of business.</p>)}
                        {major.toUpperCase() === 'TEACHING' && (<p className='text-xs text-center w-[350px] ' id={`${major}-paragraph`}>Your excellence in subjects like physics or mathematics, paired with mentoring abilities and critical thinking skills, suggests teaching as a fitting career path for you. Your inclination towards working with people and serving society enhances your potential as an educator</p>)}
                        {major.toUpperCase() === 'MEDECINE' && (<p className='text-xs text-center w-[350px] ' id={`${major}-paragraph`}>Your proficiency in chemistry and biology, along with interests in science and teamwork skills, point towards a promising career in medicine. Your attention to detail and communication skills are assets in this field, and your inclination towards serving society is well-aligned with the values of healthcare professionals.</p>)}
                        {major.toUpperCase() === 'PHARMACY' && (<p className='text-xs text-center w-[350px] ' id={`${major}-paragraph`}>Your excellence in chemistry and biology, coupled with research interests and strong communication skills, make you a suitable candidate for pharmacy. Your ability to work with people and adapt to different situations adds to your potential success in this field.</p>)}
                        {major.toUpperCase() === 'PSYCHOLOGY' && (<p className='text-xs text-center w-[350px] ' id={`${major}-paragraph`}>Your excellence in psychology, along with proficiency in statistics and biology, indicates a strong inclination towards this field. Your analytical thinking skills, coupled with effective communication abilities and a desire to serve society, make you well-suited for a career in psychology.</p>)}
                    </div>

                    )
                )
            }
          </ol>
        </div>
      </div>
    </div>
  )
}

export default Result
