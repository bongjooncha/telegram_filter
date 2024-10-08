import React, { useState } from "react";

import style from "./styles/chatId.module.css";
import ChatLists from "./ChatLists";
import { reloadChatIds } from "api/chat_id";

function ChatId({ chatIds, checkedIds, setCheckedIds }) {
  const [loading, setLoading] = useState(false);

  const handleSelectAll = () => {
    if (checkedIds.length === chatIds.length) {
      setCheckedIds([]);
    } else {
      setCheckedIds(chatIds.map((chatId) => chatId.id));
    }
  };

  const handleReloadChatIds = async () => {
    setLoading(true);
    try {
      await reloadChatIds();
    } catch (error) {
      console.error("채팅 ID를 동기화하는 중 오류 발생");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={style.ChatId}>
      <button className={style.syncronizeButton} onClick={handleReloadChatIds}>
        {loading ? "syncronizing..." : "syncronize"}
      </button>
      <div className={style.menu}>
        <div>ALL</div>
        <button>+</button>
      </div>
      <ChatLists
        chatIds={chatIds}
        checkedIds={checkedIds}
        setCheckedIds={setCheckedIds}
      />
      <div className={style.bottomButton}>
        <button className={style.createNewGroup}>그룹 생성</button>
        <button className={style.selectAllButton} onClick={handleSelectAll}>
          전체 선택
        </button>
      </div>
    </div>
  );
}

export default ChatId;
