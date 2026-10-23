
import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [status, setStatus] = useState("Checking connection...");

  useEffect(() => {
    const apiUrl =
      import.meta.env.VITE_API_URL || "http://localhost:8000";

    fetch(`${apiUrl}/health`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Backend request failed");
        }
        return response.json();
      })
      .then((data) => {
        setStatus(
          `Backend: ${data.status} | Database: ${data.database}`
        );
      })
      .catch(() => {
        setStatus("Unable to connect to backend");
      });
  }, []);

  return (
    <main>
      <h1>Field Service Management</h1>
      <p>Full-Stack Application</p>

      <h2>System Status</h2>
      <p>{status}</p>
    </main>
  );
}

export default App;
