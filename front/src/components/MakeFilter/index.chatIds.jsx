import React, { useState, useEffect } from "react";

import style from "./styles/chatId.module.css";
import ChatLists from "./ChatLists";
import { getAllChatId, reloadChatIds, getGroupNames } from "api/chat_id";

function ChatId({ checkedIds, setCheckedIds }) {
  const [chatIds, setChatIds] = useState([]);
  const [groupNames, setGroupNames] = useState([]);
  const [current, setCurrent] = useState("ALL");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchChatIds = async () => {
      const ids = await getAllChatId();
      setChatIds(ids);
    };

    const fetchGroupNames = async () => {
      const names = await getGroupNames();
      setGroupNames(names);
    };

    fetchChatIds();
    fetchGroupNames();
  }, []);

  const handleSelectAll = () => {
    if (checkedIds.length === chatIds.length) {
      setCheckedIds([]);
    } else {
      setCheckedIds(chatIds.map((chatId) => chatId));
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
        <div key="ALL">ALL</div>
        {groupNames.map((groupName) => (
          <div key={groupName}>{groupName}</div>
        ))}
        <div>add group</div>
      </div>
      <ChatLists
        chatIds={chatIds}
        checkedIds={checkedIds}
        setCheckedIds={setCheckedIds}
      />
      <div className={style.bottomButton}>
        <button className={style.createNewGroup}>create group</button>
        <button className={style.selectAllButton} onClick={handleSelectAll}>
          select all
        </button>
      </div>
    </div>
  );
}

export default ChatId;
