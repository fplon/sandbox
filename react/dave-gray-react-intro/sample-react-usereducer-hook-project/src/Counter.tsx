import { ReactNode } from "react";
import { useCounter } from "./context/CounterContext";
import { useCounterText } from "./context/CounterContext";

type ChildrenType = {
  children: (num: number) => ReactNode;
};

const Counter = ({ children }: ChildrenType) => {
  const { count, increment, decrement } = useCounter();
  const { text, handleTextInput } = useCounterText();

  return (
    <>
      {/* <h1>{children(count)}</h1> */}
      <h1>{children(count)}</h1>
      <div>
        <button onClick={decrement}>-</button>
        <button onClick={increment}>+</button>
      </div>
      <input type="text" onChange={handleTextInput} />
      <h2>{text}</h2>
    </>
  );
};

export default Counter;
