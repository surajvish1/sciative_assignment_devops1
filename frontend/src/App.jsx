import { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState("");

  useEffect(() => {
    fetch("/api1")
      .then(res => res.json())
      .then(d => setData(d.message));
  }, []);

  return <h1>{data}</h1>;
}

export default App;
