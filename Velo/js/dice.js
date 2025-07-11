import { apiRequest } from "./api.js";

export async function rollD10CWOD(dice, dificultad = 6) {
  // POST a CWOD20 dice roll
  return await apiRequest("/RitualRoll/CWoD20/tirada/", "POST", {
    dados: dice,
    dificultad,
  });
}

export async function rollNumericDice(caras) {
  return await apiRequest("/RitualRoll/dadoNumerico/", "POST", { caras });
}

export async function rollMultipleDice(dados, carasArr, dificultad = 0, bonus = 0, modoDificultad = true) {
  return await apiRequest("/RitualRoll/tiradaMultiple/", "POST", {
    dados,
    caras: carasArr,
    dificultad,
    bonus,
    modoDificultad,
  });
}