import { useState } from "react";
function Third(){
    let [x,setX] = useState(0);
    function increment(){
        setX(x+1);
    }
    function decrement(){
        setX(x-1);
    }
    return (
        <div className="ThirdComponent">
            <button onClick={increment}>+</button>
            <h1>{x}</h1>
            <button onClick={decrement}>-</button>
        </div>
    );
}
export default Third;