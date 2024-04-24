import { useState } from "react";
import Form1 from "./Form1";
import Form2 from "./Form2";
import Form3 from "./Form3";

const Form = () => {
  const [page, setPage] = useState(1);
  const [data, setData] = useState({
    interests : '',
    skill :'',
    personalityType:'',
    yesNoSelection:'',
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

  const handleData = (formData) => {
    setData({ ...data, ...formData });
  };
  console.log(data)

  const goNext = (formData) => {
    handleData(formData);
    setPage(page + 1);
  };

  const goBack = () => {
    setPage(page - 1);
  };
  const handleSubmit = async (e, formData) => {
    handleData(formData)
    console.log(data)
    e.preventDefault()
    try {
        const response = await fetch ('http://127.0.0.1:8000/myapp/form/', {
            method : 'POST',
            headers : {
                'Content-Type' : 'application/json'
            }, 
            body : JSON.stringify(data), 
        })
        if (!response.ok) { 
            throw new Error ('network response was not ok')
        }
    } catch (error) {
        console.log(error)
    }
  };

  return (
    <div>
      {page === 1 && <Form1 goNext={(formData) => goNext(formData)}></Form1>}
      {page === 2 && (
        <Form2
        goNext={(formData) => goNext(formData)}
          goBack={goBack}
        ></Form2>
      )}
      {page === 3 && (
        <Form3
        handleSubmit={(formData) => {
            handleSubmit(formData);
          }}
          data={data}
        ></Form3>
      )}
    </div>
  );
};

export default Form;

  