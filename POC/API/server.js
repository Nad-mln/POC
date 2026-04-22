const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();

app.use(express.json());
app.use(cors());

mongoose.connect("mongodb://127.0.0.1:27017/avion")
  .then(() => console.log("MongoDB connecté"))
  .catch((err) => console.error("Erreur MongoDB :", err));

// Import du modèle
const Avion = require("./models/Avion");

// Route test
app.get("/", (req, res) => {
  res.json({ message: "API avion opérationnelle" });
});

// POST : enregistrer une nouvelle position
app.post("/api/avion", async (req, res) => {
  try {
    const { altitude, orientation } = req.body;

    if (altitude == null || orientation == null) {
      return res.status(400).json({ message: "Altitude et orientation sont requis" });
    }

    const altitudeNumber = Number(altitude);
    const orientationNumber = Number(orientation);

    if (Number.isNaN(altitudeNumber) || Number.isNaN(orientationNumber)) {
      return res.status(400).json({ message: "Altitude et orientation doivent être numériques" });
    }

    if (altitudeNumber < 0) {
      return res.status(400).json({ message: "L'altitude doit être positive ou nulle" });
    }

    if (orientationNumber < 0 || orientationNumber > 360) {
      return res.status(400).json({ message: "L'orientation doit être comprise entre 0 et 360" });
    }

    const data = new Avion({
      altitude: altitudeNumber,
      orientation: orientationNumber
    });

    await data.save();

    res.status(201).json(data);
  } catch (err) {
    console.error("Erreur POST :", err);
    res.status(500).json({ error: err.message });
  }
});

// GET : récupérer la dernière position
app.get("/api/avion", async (req, res) => {
  try {
    const data = await Avion.findOne().sort({ _id: -1 });

    if (!data) {
      return res.json(null);
    }

    res.json(data);
  } catch (err) {
    console.error("Erreur GET :", err);
    res.status(500).json({ error: err.message });
  }
});

// GET : mise à jour via paramètres URL
app.get("/api/avion/update", async (req, res) => {
  try {
    const { altitude, orientation } = req.query;

    if (altitude == null || orientation == null) {
      return res.status(400).json({ message: "Paramètres altitude et orientation requis" });
    }

    const altitudeNumber = Number(altitude);
    const orientationNumber = Number(orientation);

    if (Number.isNaN(altitudeNumber) || Number.isNaN(orientationNumber)) {
      return res.status(400).json({ message: "Altitude et orientation doivent être numériques" });
    }

    if (altitudeNumber < 0) {
      return res.status(400).json({ message: "L'altitude doit être positive ou nulle" });
    }

    if (orientationNumber < 0 || orientationNumber > 360) {
      return res.status(400).json({ message: "L'orientation doit être comprise entre 0 et 360" });
    }

    const data = new Avion({
      altitude: altitudeNumber,
      orientation: orientationNumber
    });

    await data.save();

    res.status(201).json(data);
  } catch (err) {
    console.error("Erreur GET update :", err);
    res.status(500).json({ error: err.message });
  }
});

app.listen(5000, () => {
  console.log("Serveur lancé sur http://localhost:5000");
});