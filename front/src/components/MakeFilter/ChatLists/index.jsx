import React from "react";
import style from "./index.module.css";

function ChatLists({ chatIds, checkedIds, setCheckedIds }) {
  const handleCheckboxChange = (id) => {
    setCheckedIds((prevCheckIds) => {
      if (prevCheckIds.includes(id)) {
        return prevCheckIds.filter((checkedId) => checkedId !== id);
      } else {
        return [...prevCheckIds, id];
      }
    });
  };

  return (
    <div className={style.lists}>
      {chatIds.map((chatId) => (
        <div key={chatId.id}>
          <input
            type="checkbox"
            checked={checkedIds.includes(chatId.id)}
            onChange={() => handleCheckboxChange(chatId.id)}
          />
          {chatId.name}
        </div>
      ))}
    </div>
  );
}

export default ChatLists;
