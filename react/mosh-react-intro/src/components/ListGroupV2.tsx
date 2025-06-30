function ListGroup() {
  let items: string[] = [
    "New York",
    "San Francisco",
    "Tokyo",
    "London",
    "Paris",
  ];
  // items = [];

  // for loops are NOT how JSX works - instead, use the map function
  // && is a common implements of short-circuiting in JavaScript
  return (
    <>
      <h1>List</h1>
      {items.length === 0 && <p>No items</p>}
      <ul className="list-group">
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </>
  );

  // can make the code DRY by using a ternary operator below instead of this if statement
  // if (items.length === 0) {
  //   return (
  //     <>
  //       <h1>List</h1>
  //       <p>No items</p>
  //     </>
  //   );
  // }

  // const getMessage = () => {
  //   items.length === 0 ? "No items" : null;
  // };

  // return (
  //   <>
  //     <h1>List</h1>
  //     {getMessage()}
  //     <ul className="list-group">
  //       {items.map((item) => (
  //         <li key={item}>{item}</li>
  //       ))}
  //     </ul>
  //   </>
  // );
}

export default ListGroup;
