import { isEditableInput } from '@testing-library/user-event/dist/utils';

import './Second.css';
function Person(props){
  return(
    <div className='subcomponent'>
    <h1>Name: {props.name}</h1>
    <h1>Age:{props.age}</h1>
    <h1>gender :{props.gender}</h1>
    <hr></hr>
    </div>
  );
}

function Second(){
    const fruits =['Apple','Orange','Banana','Grapes'];
    return(
      <>
        <div className="secondcomponent">
         <Person name="Rama" age={34} gender="M"/>
         <Person name = "Krishna" age={33} gender = "M" />
         
         </div>
      </>
        );
}
export default Second;