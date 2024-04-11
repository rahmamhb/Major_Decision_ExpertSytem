import { useState } from 'react'
import '../index.css'
import { Link } from 'react-router-dom';
const Result = ()=> {

  const [majors , setMajors] = useState(['law' , 'computer Science'])
  useEffect(()=>{
    fetchMajors()
  },[])

 const fetchMajors = ()=>{

 }
  return (
    <div className='bg-back-pattern bg-no-repeat bg-cover flex justify-center text-xl h-[100vh]'>
      <div className=''></div>
      <div className='bg-result-pattern bg-no-repeat bg-contain w-[40vw] flex items-center justify-center'>
        <div className='flex flex-col gap-4 items-center justify-center'>
          <p className='font-extrabold'>Your Results !</p>
          <p className='text-lg w-72 text-center'>You have a great potential to succeed in the following majors: </p>              
          <ol className='list-decimal'>
            { majors.map((major)=>
                    (
                        <li>{major}</li>
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
