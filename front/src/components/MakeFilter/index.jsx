import { useState, useEffect } from "react";
import style from "./styles/makeFilter.module.css";
import WordLists from "./WordLists";
import ChatId from "./index.chatIds";
import Name from "components/Name";

import { getAllChatId } from "api/chat_id";

function MakeFilter() {
  const [name, setName] = useState("");
  const [words, setWords] = useState([]);
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
      <div className={style.contents}>
        <div className={style.items}>
          <Name designation={"Filter Name"} name={name} setName={setName} />
          <h2>choose words</h2>
          <WordLists words={words} setWords={setWords} />
        </div>
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
