import { useEffect, useState } from "react";
import avionhaut from "./avionhaut3.png";

function App() {
  const [altitude, setAltitude] = useState(0);
  const [orientation, setOrientation] = useState(0);
  const [status, setStatus] = useState("Connexion à l'API...");
  const [lastUpdate, setLastUpdate] = useState("");

  const fetchData = async () => {
    try {
      const res = await fetch("http://localhost:5000/api/avion");

      if (!res.ok) {
        throw new Error("Réponse API invalide");
      }

      const data = await res.json();

      if (data) {
        setAltitude(data.altitude);
        setOrientation(data.orientation);
        setLastUpdate(new Date().toLocaleTimeString());
        setStatus("Données mises à jour");
      } else {
        setStatus("Aucune donnée reçue pour le moment");
      }
    } catch (err) {
      console.error("Erreur API :", err);
      setStatus("Erreur de connexion à l'API");
    }
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 1000);
    return () => clearInterval(interval);
  }, []);

  // Plus l'altitude est grande, plus l'avion monte à l'écran
  const airplaneBottom = Math.max(20, Math.min(320, altitude / 20));

  return (
    <div
      style={{
        textAlign: "center",
        fontFamily: "Arial, sans-serif",
        backgroundColor: "#f4f7fb",
        minHeight: "100vh",
        padding: "20px"
      }}
    >
      <h1>✈️ Suivi de l'avion</h1>

      <div
        style={{
          margin: "20px auto",
          padding: "20px",
          width: "300px",
          background: "#ffffff",
          borderRadius: "15px",
          boxShadow: "0 4px 10px rgba(0,0,0,0.1)"
        }}
      >
        <h2>Altitude</h2>
        <p style={{ fontSize: "24px", fontWeight: "bold" }}>{altitude} m</p>

        <h2>Orientation</h2>
        <p style={{ fontSize: "24px", fontWeight: "bold" }}>{orientation}°</p>

        <p style={{ marginTop: "10px", color: "#555" }}>{status}</p>
        <p style={{ fontSize: "14px", color: "#777" }}>
          Dernière mise à jour : {lastUpdate || "--"}
        </p>
      </div>

      <div
        style={{
          position: "relative",
          margin: "30px auto",
          width: "800px",
          maxWidth: "90%",
          height: "400px",
          background: "linear-gradient(to bottom, #87ceeb, #dff6ff)",
          borderRadius: "20px",
          overflow: "hidden",
          border: "2px solid #c9dcec"
        }}
      >
        <div
          style={{
            position: "absolute",
            bottom: 0,
            width: "100%",
            height: "70px",
            background: "#4caf50"
          }}
        />

        <img
          src={avionhaut}
          alt="avion"
          style={{
            position: "absolute",
            left: "50%",
            bottom: `${airplaneBottom}px`,
            width: "220px",
            transform: `translateX(-50%) rotate(${orientation}deg)`,
            transition: "bottom 0.8s ease, transform 0.8s ease-in-out"
          }}
        />
      </div>
    </div>
  );
}

export default App;