import style from "./styles/chatId.module.css";
import ChatLists from "./ChatLists";

function ChatId({ chatIds, checkedIds, setCheckedIds }) {
  const handleSelectAll = () => {
    if (checkedIds.length === chatIds.length) {
      setCheckedIds([]);
    } else {
      setCheckedIds(chatIds.map((chatId) => chatId.id));
    }
  };

  return (
    <div className={style.ChatId}>
      <button className={style.syncronizeButton}>syncronize</button>
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
