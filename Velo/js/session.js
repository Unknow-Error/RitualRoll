import { rollD10CWOD, rollNumericDice, rollMultipleDice } from "./dice.js";

// Example: dice buttons for session page
document.addEventListener("DOMContentLoaded", () => {
  // D10 CWOD
  document.getElementById("dice-cwod-btn").onclick = async () => {
    const dice = parseInt(document.getElementById("cwod-qty").value, 10) || 1;
    const dif = parseInt(document.getElementById("cwod-dif").value, 10) || 6;
    try {
      const res = await rollD10CWOD(dice, dif);
      alert(`Resultado: ${JSON.stringify(res.resultado)}`);
    } catch (err) {
      alert("Error en la tirada: " + err.message);
    }
  };

  // Numeric dice
  document.getElementById("dice-num-btn").onclick = async () => {
    const caras = parseInt(document.getElementById("num-cara").value, 10) || 6;
    try {
      const res = await rollNumericDice(caras);
      alert(`Resultado: ${JSON.stringify(res.resultado)}`);
    } catch (err) {
      alert("Error en la tirada: " + err.message);
    }
  };

  // Multiple dice (needs caras array)
  document.getElementById("dice-mult-btn").onclick = async () => {
    // Example: 3 dice, caras [6,8,10]
    const dados = parseInt(document.getElementById("mult-cant").value, 10) || 3;
    const caras = document.getElementById("mult-caras").value.split(",").map(x => parseInt(x, 10));
    try {
      const res = await rollMultipleDice(dados, caras);
      alert(`Resultado: ${JSON.stringify(res.resultado)}`);
    } catch (err) {
      alert("Error en la tirada: " + err.message);
    }
  };
});