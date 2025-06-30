// import { Fragment } from "react";

//// you don't even need to import Fragment - just use empty tags
function ListGroup() {
  return (
    <>
      <h1>List</h1>
      <ul className="list-group">
        <li className="list-group-item">Item 1</li>
        <li className="list-group-item">Item 2</li>
        <li className="list-group-item">Item 3</li>
        <li className="list-group-item">Item 3</li>
        <li className="list-group-item">Item 3</li>
      </ul>
    </>
  );
}

//// you can have multiple elements in a component by wrapping in a Fragment
// function ListGroup() {
//   return (
//     <Fragment>
//       <h1>List</h1>
//       <ul className="list-group">
//         <li className="list-group-item">Item 1</li>
//         <li className="list-group-item">Item 2</li>
//         <li className="list-group-item">Item 3</li>
//         <li className="list-group-item">Item 3</li>
//         <li className="list-group-item">Item 3</li>
//       </ul>
//     </Fragment>
//   );
// }

//// you can have multiple elements in a component by wrapping in a div as well
// function ListGroup() {
//   return (
//     <div>
//       <h1>List</h1>
//       <ul className="list-group">
//         <li className="list-group-item">Item 1</li>
//         <li className="list-group-item">Item 2</li>
//         <li className="list-group-item">Item 3</li>
//         <li className="list-group-item">Item 3</li>
//         <li className="list-group-item">Item 3</li>
//       </ul>
//     </div>
//   );
// }

export default ListGroup;
