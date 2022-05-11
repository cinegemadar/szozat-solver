// Author: Gergo Nyarai
// This script solves the daily quiz on https://szozat.miklosdanka.com/ (Hungarian port of Wordle)
// using the solver server https://szozat-wordle-solver.herokuapp.com/
// HOWTO:
// 1. navigate to https://szozat.miklosdanka.com/
// 2. Open JS console
// 3. Copy & Paste the JS code snipet
// 4. Wait for your daily solution
{
    async function postRequest(url = "", data = {}) {
      const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
      });
      return response.json();
    }
    const buttons = document.querySelectorAll("button");
    const buttonMapping = {};
    for (const button of buttons) {
      buttonMapping[button.textContent.toLowerCase()] = button;
    }
    function wordNotContainsChar(element) {
      for (const clazz of element.classList) {
        if (clazz.includes("bg-slate")) {
          return true;
        }
      }
      return false;
    }
    function charAtWrongPlace(element) {
      for (const clazz of element.classList) {
        if (clazz.includes("bg-yellow")) {
          return true;
        }
      }
      return false;
    }
    let guessed = false;
    let guessCount = 0;
    const play = async () => {
      const rows = document.querySelectorAll(".grid-cols-5");
      let lastRow;
      let postData = [];
      for (let row of rows) {
        const rowFilled = row.querySelectorAll(".text-white").length > 0;
        if (!rowFilled) {
          break;
        }
        lastRow = row;
        const rowData = [];
        guessed = true;
        for (let child of lastRow.children) {
          let character = child.textContent;
          let status;
          if (wordNotContainsChar(child)) {
            // DOESN'T CONTAINS
            status = 3;
            guessed = false;
          } else if (charAtWrongPlace(child)) {
            // WRONG PLACE
            status = 2;
            guessed = false;
          } else {
            // RIGHT PLACE
            status = 1;
          }
          rowData.push(character.toLowerCase());
          rowData.push(status);
        }
        postData.push(rowData);
      }
      if (postData.length === 0) {
        postData.push([]);
      }
      guessCount++;
      const response = await postRequest(
        "https://szozat-wordle-solver.herokuapp.com/guess",
        postData
      );
      const letters = response[0].toLowerCase().split(",");
      for (const letter of letters) {
        buttonMapping[letter].click();
      }
      buttonMapping["beküld"].click();
      if (!guessed && guessCount < 8){
        setTimeout(play, 5000);
      } else if (guessed){
        alert('NYERTÉL!!!');
      } else {
        alert('Vesztettél... :\'(');
      }
    }
    await play();
  }