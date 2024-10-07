import { useState, useEffect } from "react";
import style from "./styles/makeFilter.module.css";
import ChatId from "./index.chatIds";

import { getAllChatId } from "api/chat_id";

function MakeFilter() {
  const [chatIds, setChatIds] = useState([]);
  const [checkedIds, setCheckedIds] = useState([]);

  useEffect(() => {
    const fetchChatIds = async () => {
      const ids = await getAllChatId();
      setChatIds(ids);
    };
    fetchChatIds();
  }, []);

  return (
    <div className={style.MakeFilter}>
      <h1>Make Filter</h1>
      <div className={style.contents}>
        <div className={style.items}></div>
        <div className={style.chatrooms}>
          <ChatId
            chatIds={chatIds}
            checkedIds={checkedIds}
            setCheckedIds={setCheckedIds}
          />
        </div>
      </div>
    </div>
  );
}

export default MakeFilter;
