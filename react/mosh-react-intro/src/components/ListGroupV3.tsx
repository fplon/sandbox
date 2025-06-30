// showing event handling

import { MouseEvent } from "react";

function ListGroup() {
  let items: string[] = [
    "New York",
    "San Francisco",
    "Tokyo",
    "London",
    "Paris",
  ];

  // Event handler: convention naming is handle + event name
  const handleClick = (event: MouseEvent) => {
    console.log(event);
  };

  // items = [];

  // in react, each element has a property called onClick
  return (
    <>
      <h1>List</h1>
      {items.length === 0 && <p>No items</p>}
      <ul className="list-group">
        {items.map((item: string, index: number) => (
          <li className="list-group-item" key={item} onClick={handleClick}>
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
