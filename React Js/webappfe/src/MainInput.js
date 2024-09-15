import { useState,useEffect } from "react";
import axios from "axios";

function MainInput(){
    const[data,setData] = useState('');
    
    useEffect(()=>{
        axios.get('http://127.0.0.1:8000/api/getemployees/').then(
            (res)=>{setData(res.data);}
        ).catch((error)=>{console.log(error);})
    },[]);
function createEmployee(){
    axios.post('http://127.0.0.1:8000/api/getemployees/',
    [{'empno':5,'empname':'Ramakrishna','salary':600000}]).catch((error)=>{
        console.log(error)
    })
}
return(
    <div>
        <button onClick={createEmployee}>Create Employee</button>
    </div>
);
}
export default MainInput;