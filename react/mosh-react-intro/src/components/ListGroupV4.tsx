// using useState hook to change the color of the selected item in a list

import { useState } from "react";

function ListGroup() {
  let items: string[] = [
    "New York",
    "San Francisco",
    "Tokyo",
    "London",
    "Paris",
  ];
  // Hook: useState
  const [selectedIndex, setSelectedIndex] = useState(-1);

  // in react, each element has a property called onClick
  return (
    <>
      <h1>List</h1>
      {items.length === 0 && <p>No items</p>}
      <ul className="list-group">
        {items.map((item: string, index: number) => (
          <li
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            key={item}
            onClick={() => setSelectedIndex(index)}
          >
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
