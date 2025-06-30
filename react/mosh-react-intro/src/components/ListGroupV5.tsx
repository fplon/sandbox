// Passing Data via Props

import { useState } from "react";

// Props is the naming convention for the object that contains the properties of a component
interface Props {
  items: string[];
  heading: string;
}

function ListGroup({ items, heading }: Props) {
  // Hook: useState
  const [selectedIndex, setSelectedIndex] = useState(-1);

  // in react, each element has a property called onClick
  return (
    <>
      <h1>{heading}</h1>
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
