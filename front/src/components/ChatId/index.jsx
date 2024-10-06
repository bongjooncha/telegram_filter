import React from "react";
import style from "./chatId.module.css";

function ChatId() {
  return (
    <div className={style.ChatId}>
      <button className={style.syncronize}>syncronize</button>
      <div>
        <div>ALL</div>
      </div>
    </div>
  );
}

export default ChatId;
