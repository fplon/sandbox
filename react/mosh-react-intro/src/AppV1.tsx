import ListGroup from "./components/ListGroup";

function App() {
  let items: string[] = [
    "New York",
    "San Francisco",
    "Tokyo",
    "London",
    "Paris",
  ];

  const handleItemSelect = (item: string) => {
    console.log(item);
  };

  return (
    <div>
      <ListGroup
        items={items}
        heading="Cities"
        onItemSelect={handleItemSelect}
      />
    </div>
  );
}

export default App;
