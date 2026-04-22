const mongoose = require("mongoose");

const avionSchema = new mongoose.Schema({
  altitude: {
    type: Number,
    required: true
  },
  orientation: {
    type: Number,
    required: true
  },
  date: {
    type: Date,
    default: Date.now
  }
});

module.exports = mongoose.model("Avion", avionSchema);