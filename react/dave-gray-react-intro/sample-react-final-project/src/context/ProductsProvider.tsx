// ProductsProvider acts as a data provider for its descendants, ensuring that they
// have access to the products data without needing to pass it down through props manually.
// This pattern is particularly useful in large React applications where passing props
// through multiple layers of components can become cumbersome.

import {
  createContext,
  ReactElement,
  // useContext,
  useState,
  useEffect,
} from "react";

export type ProductType = {
  sku: string;
  name: string;
  price: number;
};

// const initState: ProductType[] = [];

const initState: ProductType[] = [
  {
    sku: "item0001",
    name: "Widget",
    price: 9.99,
  },
  {
    sku: "item0002",
    name: "Premium Widget",
    price: 19.99,
  },
  {
    sku: "item0003",
    name: "Deluxe Widget",
    price: 29.99,
  },
];

export type UseProductsContextType = { products: ProductType[] };

const initContextState: UseProductsContextType = { products: [] };

// initialises a context object with a default value
const ProductsContext = createContext<UseProductsContextType>(initContextState);

type ChildrenType = {
  children?: ReactElement | ReactElement[];
};

// responsible for managing the state of the products
export const ProductsProvider = ({ children }: ChildrenType): ReactElement => {
  // useState mananges the state of the products array
  const [products, setProduct] = useState<ProductType[]>(initState);

  // mixed opinions on using async in useEffect...
  // fetches the data asynchronously when the component mounts and updates the state
  // useEffect(() => {
  //   const fetchProducts = async (): Promise<ProductType[]> => {
  //     const data = await fetch("http://localhost:3500/products")
  //       .then((res) => {
  //         return res.json();
  //       })
  //       .catch((err) => {
  //         if (err instanceof Error) console.log(err.message);
  //       });
  //     return data;
  //   };
  //   fetchProducts().then((products) => setProduct(products));
  // }, []);

  // ProductsProvider renders ProductsContext.Provider which wraps its children.
  // It passes the products state as the value to the context provider.
  // This makes products available to all components that consume the context.
  return (
    <ProductsContext.Provider value={{ products }}>
      {children}
    </ProductsContext.Provider>
  );
};

export default ProductsContext;
