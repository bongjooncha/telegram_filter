import React, { useState } from "react";
import style from "./index.module.css";

function WordLists({ words, setWords }) {
  const [newWord, setNewWord] = useState("");

  const handleAddWord = () => {
    if (newWord.trim() === "") return;
    if (words.includes(newWord.trim())) {
      alert("이미 존재하는 단어입니다.");
      return;
    }
    setWords((prev) => [...prev, newWord]);
    setNewWord("");
  };
  const handleDeleteWord = (index) => {
    const updatedInputs = words.filter((_, i) => i !== index);
    setWords(updatedInputs);
  };

  return (
    <div className={style.WordLists}>
      <div className={style.inputsParents}>
        {words.map((word, index) => (
          <div className={style.inputs} key={index}>
            <input type="text" value={word} readOnly />
            <button
              className={style.inputButton}
              onClick={() => handleDeleteWord(index)}
            >
              삭제
            </button>
          </div>
        ))}

        <input
          className={style.addWord}
          type="text"
          value={newWord}
          onChange={(e) => setNewWord(e.target.value)}
          placeholder="choose word"
        />
      </div>
      <button className={style.addButton} onClick={handleAddWord}>
        단어 추가
      </button>
    </div>
  );
}

export default WordLists;
