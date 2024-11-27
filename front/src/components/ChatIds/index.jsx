import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

import style from "./index.module.css";
import ChatLists from "../MakeFilter/ChatLists";
import {
  getAllChatId,
  reloadChatIds,
  getGroupNames,
  getChatGroups,
  getBotTokens,
} from "api/chat_id";

function ChatId({ rerender, useage, checkedIds, setCheckedIds }) {
  const [chatIds, setChatIds] = useState([]);
  const [groupNames, setGroupNames] = useState([]);
  const [loading, setLoading] = useState(false);
  const [current, setCurrent] = useState("ALL");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchChatIds = async () => {
      if (current === "ALL") {
        const ids = await getAllChatId();
        setChatIds(ids);
      } else if (current === "BOT") {
        const tokens = await getBotTokens();
        setChatIds(tokens);
      } else {
        const ids = await getChatGroups(current);
        setChatIds(ids);
      }
    };

    const fetchGroupNames = async () => {
      const names = await getGroupNames();
      setGroupNames(names);
    };

    fetchChatIds();
    fetchGroupNames();
  }, [rerender, current]);

  const handleGroupClick = (group) => {
    setCurrent(group);
  };

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
      const ids = await getAllChatId();
      setChatIds(ids);
      const names = await getGroupNames();
      setGroupNames(names);
    } catch (error) {
      console.error("채팅 ID를 동기화하는 중 오류 발생");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={style.ChatId}>
      <div className={style.topButton}>
        <button onClick={handleReloadChatIds}>
          {loading ? "syncronizing..." : "syncronize"}
        </button>
      </div>
      <div className={style.menu}>
        <div
          key="ALL"
          onClick={() => handleGroupClick("ALL")}
          className={`${style.menuItem}  ${
            current === "ALL" ? style.active : ""
          }`}
        >
          ALL
        </div>
        <div
          key="BOT"
          onClick={() => handleGroupClick("BOT")}
          className={`${style.menuItem}  ${
            current === "BOT" ? style.active : ""
          }`}
        >
          BOT
        </div>
        {groupNames.map((groupName) => (
          <div
            key={groupName}
            onClick={() => handleGroupClick(groupName)}
            className={`${style.menuItem}  ${
              current === groupName ? style.active : ""
            }`}
          >
            {groupName}
          </div>
        ))}
      </div>
      <ChatLists
        chatIds={chatIds}
        checkedIds={checkedIds}
        setCheckedIds={setCheckedIds}
      />
      <div className={style.bottomButton}>
        {useage === "editGroup" ? (
          <button
            className={style.createNewGroup}
            onClick={() => navigate("/")}
          >
            edit filter
          </button>
        ) : (
          <button
            className={style.createNewGroup}
            onClick={() => navigate("/edit_group")}
          >
            edit group
          </button>
        )}
        <button className={style.selectAllButton} onClick={handleSelectAll}>
          select all
        </button>
      </div>
    </div>
  );
}

export default ChatId;
