import Heading from "./components/Heading";
import Section from "./components/Section";
import Counter from "./components/Counter";
import List from "./components/List";

import { useState } from "react";

function App() {
  const [count, setCount] = useState<number>(0);

  return (
    <>
      <Heading title={"Hello Findo"} />
      <Section title={"First Section"}>Children go between the tags</Section>
      <Counter setCount={setCount}>Count is {count}</Counter>
      <List
        items={["🐍 Python", "👨‍💻 Typescript", "💽 SQL"]}
        render={(item: string) => <span className="gold">{item}</span>}
      />
    </>
  );
}

export default App;
