import {
  useState,
  useCallback,
  useEffect,
  useMemo,
  useRef,
  MouseEvent,
  KeyboardEvent,
} from "react";

interface User {
  id: number;
  username: string;
}

type fibFunc = (n: number) => number;

const fib: fibFunc = (n) => {
  if (n < 2) return n;
  return fib(n - 1) + fib(n - 2);
};

const myNumber: number = 20;

function App() {
  const [count, setCount] = useState<number>(0);
  const [users, setUsers] = useState<User[] | null>(null);

  const inputRef = useRef<HTMLInputElement>(null);

  console.log(inputRef?.current);
  console.log(inputRef?.current?.value);

  useEffect(() => {
    console.log("Component did mount");
    console.log("Users: ", users);

    return () => console.log("Component will unmount");
  }, [users]);

  const adder = useCallback(
    (
      e: MouseEvent<HTMLButtonElement> | KeyboardEvent<HTMLButtonElement>
    ): void => setCount((prev) => prev + 1),
    []
  );

  // use when you want to memoize the result of a function
  // which could be expensive to run. It will only re-run
  // when the value of the dependencies change.
  const result = useMemo<number>(() => fib(myNumber), [myNumber]);

  return (
    <div className="App">
      <h1>{count}</h1>
      <button onClick={adder}>+++</button>
      <h1>{result}</h1>
      <input ref={inputRef} type="text" />
    </div>
  );
}

export default App;
